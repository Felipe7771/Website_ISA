
<?php

$host = '127.0.0.1';
$dbname = 'isa';
$user = 'root';
$password = '';

try{
    // ========================================
    // TESTE PARA XAMPP DA PORTA 3307
    $port = '3307';
    $conn = new PDO("mysql:host=$host;port=$port;dbname=$dbname",$user,$password);
    // ========================================
    // $conn = new PDO("mysql:host=$host;dbname=$dbname",$user,$password);
} catch (PDOException $e){
    echo "Erro : " . $e->getMessage();
}


?>
