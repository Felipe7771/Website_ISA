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
    <img src='https://assets.onecompiler.app/43h62qpv7/43h62r9b5/logo_bar.png'> <!-- aqui é onde fica a logo -->
    <div>
      <a class='icon-style' href="index.php"><i class='bx bx-home-alt'></i></a> <!-- Ir para o Home -->
      <a class='icon-style' href="about.php"><i class='bx bxs-group'></i></a> <!-- Ir para o Sobre -->
     
    <?php echo $buttom; ?> <!-- Botão apartir do login do usuário -->
    <a href=""><button class= "butlog"><i class='bx bx-user icon-log'></i>Login</button></a>
         
    </div>
  </header>

  <main id="mainContainerforInf">
    <section class="inf-panel">

        <h1 class= "h1inf">SOBRE NÓS</h1>
        <form onsubmit="return validarLogin()">
            <p class='pinf'>O projeto ISA nasceu como parte do nosso Trabalho de Conclusão de Curso. A proposta surgiu da vontade de explorar o potencial da inteligência artificial no dia a dia das pessoas.</p>
            <p class='pinf'>A ISA é uma assistente virtual capaz de compreender perguntas feitas por voz e responder de forma clara e natural, utilizando recursos de inteligência artificial. Além de desenvolver a tecnologia, também também nos dedicamos à criação  de uma interface acessível e moderna, com foco na experiência do usuário.</p>
            <p class='pinf'>Nosso Grupo é formado por: Felipe, Miguel, Guilherme, Manuela e Bruno. Acreditamos que Tecnologias como a ISA podem tornar a tecnologia mais humana, acessivel e presente na vida das pessoas</p>
        </form>

    </section>
    
    
       <div class="contact-group">
         <div class="contato-coluna">
            <div class="contato-item">
             <div class="icon">
               <i class='bx bxl-instagram'></i>
             </div>
             <div class="textos">
               <span>@guilhermeluizsimon</span>
               <span>@manusobralpaz</span>
               <span>@felipecapelleti</span>
               <span>@miguelgmstella</span>
               <span>@brunoGay</span>
             </div>
           </div>
         </div>
       
         <div class="contato-coluna">
           <div class="contato-item">
             <div class="icon">
                <i class='bx bxs-envelope'></i>
             </div>
              <div class="textos">
               <a>guilhermeluizsimonprofissional@gmail.com</a>
               <a>manusobralpaz@gmail.com</a>
               <a>f.4355st@gmail.com</a>
               <a>@guilhermeluizsimon</a>
               <a>emaildobrunooovasiadogay@gmail.com</a>
              </div>
           </div>
        </div>
       </div>
  </main>
  
  

</body>
</html>
