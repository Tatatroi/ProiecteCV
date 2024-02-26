

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="stil.css">
    <script>
        function showInputs() {
            document.getElementById("bifa").style.display = "none";
            document.getElementById("input-uri").style.display = "block";
        }

        function hideBifa() {
            document.getElementById("bifa").style.display = "none";
        }
        
        setTimeout(hideBifa, 5000);
    </script>
</head>
<body>
    <header id="header">
        <div id="centered-text">
            <h3 id="text-titlu">Masini de vis</h3>
        </div>
        
    </header>

    <div id="content">
        <h1>Bun venit! Cu ce te putem ajuta?</h1>

         <div id = "cele3">

            <form action="index.php" class = "myform">
            <button class = "buton A">Acasa</button></form>

            <form action="autentificare.php" method="post" class = "myform">
                <button type="submit" class = "buton At">Autentificare</button>
            </form>

            <form action="crearecont.php" method="post" class = "myform">
                <button type="submit" class = "buton C">Creare cont</button>
            </form>

            <form action="autadmin.php" method="post" class = "myform">
                <button type="submit" class = "buton Ad">Administrator</button>
            </form>
        </div>
        
    </div>
    <div id="formular">

        <form method="POST" action="administrator.php" id = "formsub" enctype="multipart/form-data">
            <h2>Marca: </h2><input type="text" name="marca"><br><br>
            <h2>Pret: </h2><input type="text" name="pret"><br><br>
            <h2>Kilometri: </h2><input type="text" name="nrkm"><br><br>
            <h2>Combustibil: </h2><input type="text" name="combustibil"><br><br>
            <h2> Imagine: </h2><input type="file" name="imagine1" id="imagine1">
            <input type="submit" name="submit" value="Trimite" id = "input">
        </form>    

        <?php
    require('conexiune.php');
    if (!empty($_POST['marca']) && !empty($_POST['pret']) && !empty($_POST['nrkm']) && !empty($_POST['combustibil'])
    && isset($_FILES['imagine1'])) {
        
        $marca = $_POST['marca'];
        $pret = $_POST['pret'];
        $nrkm = $_POST['nrkm'];
        $combustibil = $_POST['combustibil'];

        $numeFisier = $_FILES['imagine1']['name'];
        $caleTemporara = $_FILES['imagine1']['tmp_name'];
        $folder = "imagini/pozemasini/". $numeFisier;
        $sql = "INSERT INTO masini (marca, pret, nrkm, combustibil, imagine) VALUES ('$marca', '$pret', '$nrkm', '$combustibil', '$numeFisier')";
            // Execute query
            mysqli_query($conn, $sql);
        
            // Now let's move the uploaded image into the folder: image
            if (move_uploaded_file($caleTemporara, $folder)) {
                echo "<h3>  Imagine incarcata cu succes!</h3>";
            } else {
                echo "<h3> Nu s-a reusit incarcarea imaginii!</h3>";
            }
        }
        $marca = null;
        $pret = null;
        $nrkm = null;
        $combustibil =null;
        mysqli_close($conn);
?> 

    </div>

        <footer>
                <div id = "contact">
                    <ul id = "mailtel">
                        <li><img src="imagini/tellogo.png"> :0732155588</li>
                        <li><img src="imagini/maillogo.png"> :masinidevis@yahoo.com</li>
                    </ul>
                    
                </div>

                <div id="adresa"><a href="https://www.google.com/maps/place/46%C2%B046'18.0%22N+23%C2%B036'33.9%22E/@46.7716586,23.6068341,17z/data=!3m1!4b1!4m4!3m3!8m2!3d46.771655!4d23.609409?entry=ttu"><img src="imagini/adresa.png"></a></div>

                <ul id="listalogo">
                    <li><a href="https://www.facebook.com/"><img class="logo" src="imagini/facebooklogo.png" ></a></li>
                    <li><a href="https://www.instagram.com/"><img class="logo" src="imagini/instalogo.png"></a></li>
                    <li><a href="https://twitter.com/home"><img class="logo" src="imagini/twitterlogo.png"></a></li>
                </ul>
            
            </footer>

</body>
</html>