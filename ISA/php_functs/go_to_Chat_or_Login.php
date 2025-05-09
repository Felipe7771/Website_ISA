<?php
include 'button_login.php';

# verifique se o usuário está logado
if(Check_login()){
    # se está logado, vá para o chat.php
    header('Location: ../chat.php');
    exit();
} else {
    # se não está logado, vá para o login.php
    header('Location: ../login.php');
    exit();
}
?>