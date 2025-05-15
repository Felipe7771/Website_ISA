<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
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
  <title>Bem-Vindo</title>
  <link href='css/style.css' rel='stylesheet'>
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


  <main id="mainContainer">
    <section class="black-panel">

        <h1 class= "h1">CRIAR CONTA</h1>
        <!-- Como eu chamo o create_account? já que chamar diretamente ele vai trocar de tela... -->
        <form onsubmit="return validarLogin()"> 
          <div class='group'>
            <p class='pfor'>NOME</p>
            <input class='input' type="text" id="n_usuario" placeholder="Usuário" required>
            <p class='pfor'>E-MAIL</p>
            <input class='input' type="text" id="n_e-mail" placeholder="E-mail" required>
            <p class='pfor'>SENHA</p>
            <input class='input' type="password" id="n_senha" placeholder="Senha" required>
            <br>
            <!--  Aqui vai ficar a mensagem de erro  -->
            <br>
            <button class= "buttonform" type="submit">Entrar</button>
          </div>
        </form>

    </section>
  </main>

</body>
</html>
