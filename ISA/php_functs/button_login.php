<?php

function Check_login(){
    # checagem se a variável IsLogin existe e é verdadeira
    if( isset($IsLogin) && $IsLogin == true) {
        # significa que o usuário está logado
        # mudar botão para LOGOUT
        return true;
    } else {
        # significa que o usuário não está logado
        # mudar botão para LOGIN
        return false;
    }
}


?>