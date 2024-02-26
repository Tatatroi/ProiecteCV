<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "utilizatori";

$conn = mysqli_connect($servername,$username,$password,$dbname);

//verificare conexiune
if (!$conn) {
    die("Conexiunea la baza de date a esuat: " . mysqli_connect_error());
  }

?>