<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">    <title>DEEPSHIELD</title>
    <link rel="stylesheet" href="static/style2.css">
    <title> Request Detection Scanner
    </title>
    <style>
        body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: rgb(128 0 0 / 66%);
            }
            header {
                background-color: #000;
                color: white;
                padding: 10px;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .logo {
                width: 80px;
                height: auto;
                margin-right: 10px;
                padding: 10px;
                border-radius: 50%;
            }
            nav {
                background-color: #333;
                padding: 10px 0;
                text-align: center;
            }
            nav a {
                text-decoration: none;
                color: white;
                padding: 10px;
                font-size: 18px;
            }
            nav a:hover{
            background-color: aliceblue;
            color: rgba(128, 0, 0, 0.726); 
            padding: 10px;
            }
            nav a.active {
            color: white;
            }
            .banner {
                background-image: url("banner.jpg");
                background-size: cover;
                background-position: center;
                height: 400px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
                text-align: center;
            }
            .banner h1 {
                font-size: 48px;
                margin-bottom: 20px;
            }
            .banner p {
                font-size: 24px;
                max-width: 600px;
                margin: 0 auto;
            }
            .container {
                /* max-width: 1200px;
                margin: 50px auto; */
                padding: 20px;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
            }
            .feature {
                display: flex;
                justify-content: space-around;
                margin-top: 50px;
            }
            .feature-item {
                text-align: center;
                flex: 1;
                padding: 20px;
            }
            .feature-item img {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                margin-bottom: 20px;
            }
            .footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 20px 0;
            }
            .social-icons {
                margin-top: 20px;
            }
            .social-icons a {
                color: white;
                text-decoration: none;
                font-size: 24px;
                margin: 0 10px;
            }
            .social-icons a:hover{
            color: rgba(128, 0, 0, 0.726); 
            }
    
        /* Contact Us CSS */
    button, select, textarea {
        width: 100%; 
        padding: 12px; 
        border: 1px solid #ccc; 
        border-radius: 4px; 
        box-sizing: border-box; 
        margin-top: 6px; 
        margin-bottom: 16px; 
        resize: vertical 
      }
      
      button {
        background-color: rgba(128, 0, 0, 0.726);
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      
      input[type=submit]:hover {
        background-color:rgb(128 0 0 / 66%);
      }
      
      .container {
        border-radius: 5px;
        background-color: #f2f2f2;
        padding: 20px;
        border-style: inset;
      }
    
      /* Home Dashboard cards */
      .card1 {
        background-color: #fff;
        border-radius: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
        width: calc(25% - 40px); /* 25% width with 20px gap */
        max-width: 300px;
        transition: all 0.3s ease;
    }
    .card1:hover {
        transform: translateY(-5px);
        box-shadow: 0 7px 15px rgba(0, 0, 0, 0.2);
    }
    .card1 h3 {
        margin-top: 0;
        font-size: 24px;
        color: #333;
    }
    .card1 p {
        font-size: 18px;
        color: #666;
    }
    
    /* Dashboard container */
    .container2 {
        background-color: #f2f2f2;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        background-color: #f2f2f2;
        padding: 20px;
        flex-wrap: wrap;
        justify-content: center;
        border-style: inset;
        padding: 10px;
        gap: 10px;
    }
    
    .dashboard-title {
        font-size: 28px;
        margin: 0;
    }
    
    .dashboard-description {
        font-size: 16px;
        color: #777;
        margin: 0;
    }
    .container h2{
        text-decoration: underline;
    }

    .container2 input{
        height: 25px;
        width: 200px;
    }
    
    /* Dashboard Page CSS */
    .card {
        background-color: #fff;
        border-radius: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
        width: calc(25% - 40px); /* 25% width with 20px gap */
        max-width: 300px;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 7px 15px rgba(0, 0, 0, 0.2);
    }
    .card h3 {
        margin-top: 0;
        font-size: 24px;
        color: #333;
    }
    .card .chart-container {
        margin-top: 20px;
        position: relative; /* Make position relative for absolute centering */
    }
    .center-number {
        position: absolute; /* Absolute position for centering */
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); /* Center horizontally and vertically */
        font-family: 'Arial Black', sans-serif; /* Specify font family */
        font-size: 36px; /* Specify font size */
        color: #333; /* Specify font color */
    }

    b:link{
        color: #fff;
    }
    </style>
    
</head>
<body>
    <header>
        <img  src="static/deepshield.jpg" href="WAFHome.html" alt="DEEPSHIELD Logo" class="logo">
        <h1>DEEPSHIELD</h1>
    </header>
    <nav>
        <a href="WAFHome.html">Home</a>
        <a href="Test.php">Demo</a>
        <a href="WAFDashboard.html">Dashboard</a>
        <a href="WAFContact.html">Contact</a>
    </nav>
    <div class="banner">
        <div>
            <h1>We Help Securing Businesses <br>to Grow and Succeed</h1>
            <p>With our security expertise, we provide secure solutions to meet your fears.</p>
        </div>
    </div>
    <div id="about" class="container2">
        <h1 style="text-decoration: underline;">Scan Request</h1>
        <p>Insert the URL -- Based on ML model -- it'll be either malicious or safe URL</p>
        <div class="section">
            <form action="result.php" method="POST">
            <label for="url">Enter URL to check:</label>
            <input class="textbox" type="text" placeholder="URL" id="url" required>
            <button class="button" type="submit"> <a href="result.php" class="b:link"> Is Malicious</button> 
            </form>
           
        </div>
    </div>
     <script>
        function handleSubmit(event) {
            event.preventDefault(); // Prevent the default form submission
            window.location.href = "templates/result.php"; // Replace with your target URL
        }
       </script>  -->

        <!-- </div>
    <div id="contact" class="footer">
        <p>Contact us at help@Deepshield.com</p>
        <div class="social-icons">
            <a href="https://www.facebook.com" class="fa fa-facebook"></a>
            <a href="https://www.twitter.com" class="fa fa-twitter"></a>
            <a href="https://www.linkedin.com"><i class="fa fa-linkedin"></i></a>
            <a href="https://www.instagram.com"><i class="fa fa-instagram"></i></a>
        </div>
    </div>
</body>
</html>   -->



<!-- // var url = document.getElementById('payload').value;
//        var maliciousWords = ['<script>', 'select', 'from', 'where', 'table', 'alert']; -->
<!-- //        var isMalicious = false;
//          for (var i = 0; i < maliciousWords.length; i++) {
//            if (payload.includes(maliciousWords[i])) {
//                isMalicious = true;
//                break;
//              }
//            }
//            if (isMalicious) {
//              alert('Error 403 Forbidden: ' + payload + ' is malicious', {color: 'red'});  
//      } else {
//             alert('Payload: ' + payload + ' is safe', {color: 'green'});
//           }
//           redirectToHome();
//        } -->






<!-- <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <title>DEEPSHIELD</title>
</head>
<body>
    <header>
        <img src="static/deepshield.jpg" href="WAFHome.html" alt="DEEPSHIELD Logo" class="logo">
        <h1>DEEPSHIELD</h1>
    </header>
    <nav>
        <a href="WAFHome.html">Home</a>
        <a href="Test.php">Demo</a>
        <a href="WAFDashboard.html">Dashboard</a>
        <a href="WAFContact.html">Contact</a>
    </nav>
    <div class="banner">
        <div>
            <h1>We Help Securing Businesses <br>to Grow and Succeed</h1>
            <p>With our security expertise, we provide secure solutions to meet your fears.</p>
        </div>
    </div>
    <div id="about" class="container2">
        <h1 style="text-decoration: underline;">Scan Request</h1>
        <p>Insert the URL -- Based on ML model -- it'll be either malicious or safe URL</p>
        <div class="section">
            <form action="http://127.0.0.1:9005/predict" method="POST">
                <label for="url">Enter URL to check:</label>
                <input class="textbox" type="text" name="url" placeholder="URL" id="url" required>
                <button class="button" type="submit">Check</button> 
            </form>
        </div>
    </div>
    <div id="contact" class="footer">
        <p>Contact us at help@Deepshield.com</p>
        <div class="social-icons">
            <a href="https://www.facebook.com" class="fa fa-facebook"></a>
            <a href="https://www.twitter.com" class="fa fa-twitter"></a>
            <a href="https://www.linkedin.com"><i class="fa fa-linkedin"></i></a>
            <a href="https://www.instagram.com"><i class="fa fa-instagram"></i></a>
        </div>
    </div>
</body>
</html> -->


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">    <title>DEEPSHIELD</title>
    <link rel="stylesheet" href="static/style2.css">
    <title> Request Detection Scanner</title>
    <style>
        body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: rgb(128 0 0 / 66%);
            }
            header {
                background-color: #000;
                color: white;
                padding: 10px;
                text-align: center;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .logo {
                width: 80px;
                height: auto;
                margin-right: 10px;
                padding: 10px;
                border-radius: 50%;
            }
            nav {
                background-color: #333;
                padding: 10px 0;
                text-align: center;
            }
            nav a {
                text-decoration: none;
                color: white;
                padding: 10px;
                font-size: 18px;
            }
            nav a:hover{
            background-color: aliceblue;
            color: rgba(128, 0, 0, 0.726); 
            padding: 10px;
            }
            nav a.active {
            color: white;
            }
            .banner {
                background-image: url("banner.jpg");
                background-size: cover;
                background-position: center;
                height: 400px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
                text-align: center;
            }
            .banner h1 {
                font-size: 48px;
                margin-bottom: 20px;
            }
            .banner p {
                font-size: 24px;
                max-width: 600px;
                margin: 0 auto;
            }
            .container {
                /* max-width: 1200px;
                margin: 50px auto; */
                padding: 20px;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 20px;
            }
            .feature {
                display: flex;
                justify-content: space-around;
                margin-top: 50px;
            }
            .feature-item {
                text-align: center;
                flex: 1;
                padding: 20px;
            }
            .feature-item img {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                margin-bottom: 20px;
            }
            .footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 20px 0;
            }
            .social-icons {
                margin-top: 20px;
            }
            .social-icons a {
                color: white;
                text-decoration: none;
                font-size: 24px;
                margin: 0 10px;
            }
            .social-icons a:hover{
            color: rgba(128, 0, 0, 0.726); 
            }
    
        /* Contact Us CSS */
    button, select, textarea {
        width: 100%; 
        padding: 12px; 
        border: 1px solid #ccc; 
        border-radius: 4px; 
        box-sizing: border-box; 
        margin-top: 6px; 
        margin-bottom: 16px; 
        resize: vertical 
      }
      
      button {
        background-color: rgba(128, 0, 0, 0.726);
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
      }
      
      input[type=submit]:hover {
        background-color:rgb(128 0 0 / 66%);
      }
      
      .container {
        border-radius: 5px;
        background-color: #f2f2f2;
        padding: 20px;
        border-style: inset;
      }
    
      /* Home Dashboard cards */
      .card1 {
        background-color: #fff;
        border-radius: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
        width: calc(25% - 40px); /* 25% width with 20px gap */
        max-width: 300px;
        transition: all 0.3s ease;
    }
    .card1:hover {
        transform: translateY(-5px);
        box-shadow: 0 7px 15px rgba(0, 0, 0, 0.2);
    }
    .card1 h3 {
        margin-top: 0;
        font-size: 24px;
        color: #333;
    }
    .card1 p {
        font-size: 18px;
        color: #666;
    }
    
    /* Dashboard container */
    .container2 {
        background-color: #f2f2f2;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        background-color: #f2f2f2;
        padding: 20px;
        flex-wrap: wrap;
        justify-content: center;
        border-style: inset;
        padding: 10px;
        gap: 10px;
    }
    
    .dashboard-title {
        font-size: 28px;
        margin: 0;
    }
    
    .dashboard-description {
        font-size: 16px;
        color: #777;
        margin: 0;
    }
    .container h2{
        text-decoration: underline;
    }

    .container2 input{
        height: 25px;
        width: 200px;
    }
    
    /* Dashboard Page CSS */
    .card {
        background-color: #fff;
        border-radius: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        padding: 20px;
        text-align: center;
        width: calc(25% - 40px); /* 25% width with 20px gap */
        max-width: 300px;
        transition: all 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 7px 15px rgba(0, 0, 0, 0.2);
    }
    .card h3 {
        margin-top: 0;
        font-size: 24px;
        color: #333;
    }
    .card .chart-container {
        margin-top: 20px;
        position: relative; /* Make position relative for absolute centering */
    }
    .center-number {
        position: absolute; /* Absolute position for centering */
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); /* Center horizontally and vertically */
        font-family: 'Arial Black', sans-serif; /* Specify font family */
        font-size: 36px; /* Specify font size */
        color: #333; /* Specify font color */
    }

    b:link{
        color: #fff;
    }
    </style>
</head>
<body>
    <header>
        <img src="static/deepshield.jpg" href="WAFHome.html" alt="DEEPSHIELD Logo" class="logo">
        <h1>DEEPSHIELD</h1>
    </header>
    <nav>
        <a href="WAFHome.html">Home</a>
        <a href="Test.php">Demo</a>
        <a href="WAFDashboard.html">Dashboard</a>
        <a href="WAFContact.html">Contact</a>
    </nav>
    <div class="banner">
        <div>
            <h1>We Help Securing Businesses <br>to Grow and Succeed</h1>
            <p>With our security expertise, we provide secure solutions to meet your fears.</p>
        </div>
    </div>
    <div id="about" class="container2">
        <h1 style="text-decoration: underline;">Scan Request</h1>
        <p>Insert the URL -- Based on ML model -- it'll be either malicious or safe URL</p>
        <div class="section">
            <!-- <form id="urlForm"> -->
            <form action = "result.php" method="get" id="urlForm">
                <label for="url">Enter URL to check:</label>
                <input class="textbox" type="text" name="url" placeholder="URL" id="url" required>
                <button class="button" type="submit">Is Malicious</button> 
            </form>
        </div>
    </div>
    <div id="contact" class="footer">
        <p>Contact us at help@Deepshield.com</p>
        <div class="social-icons">
            <a href="https://www.facebook.com" class="fa fa-facebook"></a>
            <a href="https://www.twitter.com" class="fa fa-twitter"></a>
            <a href="https://www.linkedin.com"><i class="fa fa-linkedin"></i></a>
            <a href="https://www.instagram.com"><i class="fa fa-instagram"></i></a>
        </div>
    </div>

    <script>
        document.getElementById('urlForm').addEventListener('submit', function(event) {
            event.preventDefault();
            const url = document.getElementById('url').value.trim();
            if (url !== '') {
                fetch('http://127.0.0.1:9005/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ url: url })
                })
                .then(response => response.json())
                .then(data => {
                    window.location.href = 'result.php'; // Redirect to result page
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    alert('Failed to fetch result.');
                });
            } else {
                alert('URL cannot be empty.');
            }
        });
    </script>
</body>
</html>

