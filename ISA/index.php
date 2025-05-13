<?php
session_start();
include 'php_functs/button_login.php';

# checagem se o usuário está logado
$response = Check_login();

# pegar formato do botão a partir da resposta do $response
$buttom = Define_button_log($response);
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ISA Menu</title>
  <link href='css/style_home.css' rel='stylesheet'>
  <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700&display=swap" rel="stylesheet">
  <link rel="icon" href="img/icon_nav.png">
</head>
<body>

<!-- HEADER padrão em todas as telas -->
  <header>
    <img src='img/logo_bar.png'> <!-- aqui é onde fica a logo -->
    <div>
      <a href="index.php"><i class='bx bx-home-alt icon-style'></i></a> <!-- Ir para o Home -->
      <a href="about.php"><i class='bx bxs-group icon-style'></i></a> <!-- Ir para o Sobre -->

      <?php echo $buttom; ?> <!-- Botão apartir do login do usuário -->
      <!-- <a href=""><button class= "butlog"><i class='bx bx-user icon-log'></i>Login</button></a> -->
      
    </div>
  </header>
<!-- fim o HEADER padrão -->

  <main id="mainContainer">
    <section class="black-panel">
      <div>
        <h1 class= "h1"><i>BEM VINDO</i></h1>
        <p class= "p">Tenha uma ótima experiência com nossa nova IA por interação de voz.</p>
        <!-- Ir para Chat ou Login -->
        <a href="php_functs/go_to_Chat_or_Login.php"><button class= "button">Converse com a ISA</button></a> 

      </div>
    </section>
    <aside class="right-panel"></aside>
  </main>

</body>
</html>