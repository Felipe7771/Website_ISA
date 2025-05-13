
<?php

$host = '127.0.0.1';
$dbname = 'isa';
$user = 'root';
$password = '';

try{
    $conn = new PDO("mysql:host=$host;dbname=$dbname",$user,$password);
} catch (PDOException $e){
    echo "Erro : " . $e->getMessage();
}


?>
