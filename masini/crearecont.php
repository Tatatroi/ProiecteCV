<?php
    require('conexiune.php');
    if (!empty($_POST['nume1']) && !empty($_POST['prenume']) && !empty($_POST['Email']) && !empty($_POST['telefon']) && !empty($_POST['parola']) && !empty($_POST['repeta-parola'])) {     
    // verificăm dacă s-a trimis formularul
        if (isset($_POST['submit'])) {
            $nume = $_POST['nume1'];
            $prenume = $_POST['prenume'];
            $telefon = $_POST['telefon'];
            $email = $_POST['Email'];
            $parola = $_POST['parola'];
            
            //Adaugare in baza de date
            $sql = "INSERT INTO utilizatori(Nume, Prenume,Telefon, email, parola) VALUES ('$nume', '$prenume', '$telefon','$email', '$parola')";
        }    
        if (mysqli_query($conn, $sql)) {
            // setăm variabila de sesiune pentru a nu se trimite in baza de date informatii dupa refresh
            $_SESSION['succes_creare_cont'] = "Contul a fost creat cu succes.";
        } else {
            echo "Eroare: " . $sql . "<br>" . mysqli_error($conn);
        }
        
        mysqli_close($conn);

        // redirecționăm utilizatorul către aceeași pagină
        header("Location: crearecont.php");
        exit;
    }
?>
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
        
        <?php if (isset($_SESSION['succes_creare_cont'])): ?>
            <img src="imagini/bifa.png" alt="Bifa">
            <p><?php echo $_SESSION['succes_creare_cont']; ?></p>
            <?php unset($_SESSION['succes_creare_cont']); ?>
        <?php else: ?>

    <form action="crearecont.php" method="post" id = "formsub">
        <h2>Nume Utilizator: </h2><input type="text" name="nume1"><br><br>
        <h2>Prenume: </h2><input type="text" name="prenume"><br><br>
        <h2>Email: </h2><input type="email" name="Email"><br><br>
        <h2>Telefon: </h2><input type="text" name="telefon"><br><br>
        <h2> Parola: </h2><input type="password" name="parola"><br><br>
        <h2>Repeta parola: </h2><input type="password" name="repeta-parola"><br><br>
        <input type="submit" name="submit" value="Trimite" id = "input">
    </form>
<?php endif; ?>
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