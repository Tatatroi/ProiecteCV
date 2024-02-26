<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="stil.css">
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

    <div id="chenaradmin">
        <form action="autadmin.php" method="post">
            <h5>Cod-admin: </h5>
            <input type="text" name="numeaut" value="-->cod<--"><br><br>
            <button type="submit">Trimite</button>
        </form>
    </div>

    <div id = "infoadmin">
        <p>
            Ca si administrator aveti posibilitatea de a adauga in baza de date a masinilor noi anunturi, trebui sa adaugati imaginea(rezolutie),
            marca, kilometri si alte detalii necesare. Sunt obligatorii toate campurile pentru a putea fi vizibila pe site. Pentru lizibilitate adaugati imagini cu dimensiuni egale, ex (150x150).

        </p>
    </div>

    <?php
    if(isset($_POST['numeaut'])) {
        require_once('conexiune.php');

        $COD = $_POST['numeaut'];

        $sql = "SELECT * FROM admini WHERE codadmin = '$COD'";

        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) > 0) {
            $row = mysqli_fetch_assoc($result);
            if ($COD == $row['codadmin']) {
                // echo "<div id='chenar-informatii'>Cod incorect este corecta.</div>";
                // deschiderea in pagina de afisare a masinilor
                header('Location: administrator.php');
                exit();
            } 
            else if($COD != $row['codadmin']){
                echo ('Cod incorect');
            }
        } 
        
    }
?>

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