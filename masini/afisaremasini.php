<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="stil.css">
    <style>
        .item {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        .item img {
            width: 150px;
            height: 150px;
            margin-right: 10px;
        }
        .item2 img {
            width: 150px;
            height: 150px;
            margin-right: 10px;
        }
        .item2 p{
            font-weight: bolder;
        }
        
        .item2 {
    display: grid;
    grid-template-columns: auto 1fr;
    align-items: center;
    margin-bottom: 10px;
}

.item2 img {
    width: 150px;
    height: 150px;
    margin-right: 10px;
}

.item2 p {
    margin: 0;
    font-weight: bolder;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.item2 p:nth-child(2),
.item2 p:nth-child(3),
.item2 p:nth-child(4) {
    margin-top: 5px;
}

    </style>
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

   
   
   <?php
            // Conectare la baza de date
            require_once('conexiune.php');

            // Selectare elemente din baza de date
            $sql = "SELECT * FROM staf";
            $result = mysqli_query($conn, $sql);

            // Verificare dacă există cel puțin un rând de extras în rezultat
            if (mysqli_num_rows($result) > 0) {

                // Parcurgere rezultate și creare divuri
                while ($row = mysqli_fetch_assoc($result)) {
                    echo '<div class="item">';
                    echo '<img src="' . $row["imagine"] . '">';
                    echo '<p>' . $row["nume"] . '</p>';
                    echo ':&nbsp;&nbsp;';
                    echo '<p>' . $row['scurt_text'] . '</p>';
                    echo '</div>';
                }
            } else {
                echo "Nu exista elemente in baza de date.";
            }

            // Inchidere conexiune
            

    ?>

            <div id = "titlu-anunt">
                <p>Oferte disponibile pe siteul nostru</p>
            </div>

            <div id = "anunt">
                <?php
                    require_once('conexiune.php');

                    $sql = "SELECT * FROM  masini";
                    $rez = mysqli_query($conn, $sql);
                    if (mysqli_num_rows($result) > 0) {

                        // Parcurgere rezultate și creare divuri
                        while ($row = mysqli_fetch_assoc($rez)) {
                            echo '<div class="item2">';
                            echo '<img src="imagini/pozemasini/' . $row["imagine"] . '">';
                            echo '<p>Marca:' . $row["marca"] . '</p>'; 
                            echo '<p>Pret' . $row["pret"] . '</p>'; 
                            echo '<p>Numar kilometri:' . $row["nrkm"] . '</p>'; 
                            echo '<p>Combustibil:' . $row["combustibil"] . '</p>'; 
                            echo '&nbsp;&nbsp;';
                            echo '</div>';
                        }
                    } else {
                        echo "Nu exista anunturi disponibile.";
                    }
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