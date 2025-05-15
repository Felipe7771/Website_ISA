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
        echo "<script>alert('Usuário ou senha incorreta'); window.location.href='../login.html';</script>";
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
             echo "<script>alert('Usuário ou senha incorreta'); window.location.href='../login.html';</script>";
        }
    }

    } catch(PDOException $e){
         echo "<script>alert('Erro ao consultar o servidor. Tente mais tarde'); window.location.href='../login.html';</script>";
    }

}

?>