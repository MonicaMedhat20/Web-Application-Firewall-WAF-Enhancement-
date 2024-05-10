<!-- result.php -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $url = $_POST["url"];
    $api_url = "http://127.0.0.1:5000/predict"; // Adjust based on your server address

    // Prepare data for the Python API
    $data = json_encode(['url' => $url]);

    // Initialize cURL
    $ch = curl_init($api_url);

    // Configure cURL for POST request
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

    // Execute the request and fetch the response
    $response = curl_exec($ch);
    curl_close($ch);

    // Decode the response
    $result = json_decode($response, true);
    $valid = $result['valid'] ? "valid" : "malicious";

    // // Display the result
    // echo "<h1>URL Check Result</h1>";
    // echo "<p>The URL '$url' is $valid.</p>";
    // echo "<a href='Test.php'>Check another URL</a>";
} else {
    // Redirect to form if accessed directly
    header('Location: Test.php');
    exit();
}
?>


<html>
<head>
<title> WAF Detection Result </title>
<style>
    table, td, th {
      border: 1px solid black;
    }
    table {
      border-collapse: collapse;
    }
    th {
      text-align: right;
      background-color: rgb(203, 240, 227);
    }
    th, td {
      padding: 10px;
    }
</style>

</head>
<body>
<h1>WAF Detection Result</h1>
<table>
<tr>
<th>Result</th>
<td> <?php echo $result['class_name'] ?></td>
</tr>
</table>
<p>
    Return to previous page <a href="Test.php"> Click here </a>
</p>
</body>
</html>