<?php
session_start();

# iniciar conexão
include 'conexao.php';

# para evitar riscos, esse código é inicializado apenas quando é chamado via POST
if($_SERVER['REQUEST_METHOD'] == 'POST'){

    # coletar dados do arquivo login
    $usuario = $_POST['usuario'];
    $senha = $_POST['senha'];

    # por segurança, tente executar a consulta
    try{

    # checar se o dado informado ao usuário é um email ou nome
    if(filter_var($usuario,FILTER_VALIDATE_EMAIL)){
        $tabela = 'email';
    } else {
        $tabela = 'nome';
    }

    # inciar conexão
    $pdo = $conn->prepare('SELECT nome, email, nome FROM cliente WHERE :tabela = :usuario');
    $pdo->execute(array(
        ':tabela' => $tabela,
        ':usuario' => $usuario,
    ));

    # coleta de resultao
    $result = $pdo->fetchAll(PDO::FETCH_ASSOC);

    #verificar se ocorreu uma resposta
    if(!($result)){

        # USUÁRIO NÃO ENCONTRADO
        error_case("Usuário ou senha incorreta");
    }

    #como o resultado (principalmente email) possa ter vários resultados, temos que checá-los
    foreach($result as $user_result){

        if($usuario == $user_result[$tabela] && $senha == $user_result['senha']){

            # USUÁRIO ENCONTRADO
            $_SESSION['Name'] = $user_result['nome'];

            # desativa o valor de erro
            $_SESSION['Erro'] = False;
            # afirmação ao site que o usuário está logado
            $_SESSION['IsLogin'] = True;

            header('Location: ../chat.php');
            exit();

        } else{

            # SENHA INCORRETA
            error_case("Usuário ou senha incorreta");
        }
    }

    } catch(PDOException $e){
        error_case("Erro ao consultar o servidor. Tente mais tarde");
    }

}

# função de encerramento quando o código gera erro
function error_case($message_erro){
        # ESTRUTURA DE ERRO {
        $_SESSION['Erro'] = True; // estado de erro
        $_SESSION['Message_erro'] = $message_erro;
        # retornar texto escrito pelo usuário á tela
        $_SESSION['user'] = $GLOBALS['usuario'];
        $_SESSION['password'] = $GLOBALS['senha'];
        # }

        header('Location: ../login.php');
        exit();
}

?>