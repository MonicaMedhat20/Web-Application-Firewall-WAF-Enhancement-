<!-- result.php -->
<!-- 
// The URL of the Flask API
$api_url = 'http://127.0.0.1:9005/predict';

// The URL to check
$url_to_check = 'https://www.google.com/';

// Create an array with the URL to send in the POST request
$data = array('url' => $url_to_check);

// Convert the data array to JSON format
$data_json = json_encode($data);

// Initialize cURL session
$ch = curl_init($api_url);

// Set the options for the cURL request
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json);

// Execute the cURL request and capture the response
$response = curl_exec($ch);

// Check for cURL errors
if ($response === false) {
    $error = curl_error($ch);
    curl_close($ch);
    die('cURL error: ' . $error);
}

// Close the cURL session
curl_close($ch);

// Decode the JSON response
$response_data = json_decode($response, true);

// Output the response
if ($response_data) {
    echo 'Result: ' . $response_data['result'];
} else {
    echo 'Failed to parse response.';
} -->



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
            <td> Normal </td>
        </tr>
    </table>
    <p>
        Return to previous page <a href="Test.php"> Click here </a>
    </p>
</body>
</html>