<?php
// Inclui a conexão
include("conexao.php");

// Recebe os dados do formulário
$usuario = $_POST["n_usuario"] ?? '';
$email = $_POST["n_e-mail"] ?? '';
$senha = $_POST["n_senha"] ?? '';

// Verifica se o campo usuário está vazio
if (empty($usuario)) {
    echo "<script>alert('O campo usuário deve ser preenchido'); window.location.href='cadastro.html';</script>";
    exit;
}

// Verifica se o usuário já existe
$stmt = $conn->prepare("SELECT nome FROM cliente WHERE nome = :usuario");
$stmt->bindParam(':usuario', $usuario);
$stmt->execute();

if ($stmt->rowCount() > 0) {
    echo "<script>alert('Esse usuário já existe'); window.location.href='cadastro.html';</script>";
    exit;
}

// Insere o novo usuário
$stmt = $conn->prepare("INSERT INTO cliente (nome, email, senha) VALUES (:nome, :email, :senha)");
$stmt->bindParam(':nome', $usuario);
$stmt->bindParam(':email', $email);
$stmt->bindParam(':senha', $senha);

if ($stmt->execute()) {
    echo "<script>alert('Usuário cadastrado com sucesso!'); window.location.href='chat.php';</script>";
} else {
    echo "<script>alert('Não foi possível cadastrar esse usuário'); window.location.href='create_account.php';</script>";
}
?>
