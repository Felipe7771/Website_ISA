<?php
function Check_login(){
    # checagem se a variável IsLogin existe e é verdadeira
    if( isset($_SESSION['IsLogin']) && $_SESSION['IsLogin'] ) {

        # significa que o usuário está logado
        # mudar botão para LOGOUT
        return true;
        
    } else {
        # significa que o usuário não está logado
        return false;
    }
}

function Define_button_log($is_login){
    # checagem se o usuário está logado
    if($is_login){
        # SIM, está logado
        # definir botão LOGOUT
        return '<a href="logout.php"><button class= "butlogout"><i class="bx bx-user icon-log"></i>Logout</button></a>';
    } else {

        # NÃO, está desconectado
        # definir botão LOGIN
        return '<a href="../login.php"><button class= "butlog"><i class="bx bx-user icon-log"></i>Login</button></a>';
    }
}
?>