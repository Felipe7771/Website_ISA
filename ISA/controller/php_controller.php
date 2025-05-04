<?php

// aguarda o php receber o áudio vindo do esp32

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Salvar o áudio enviado
    $target_dir = "NIK/SongSaver/";
    if (!is_dir($target_dir)) {
        mkdir($target_dir, 0777, true);
    }

    $nomeArquivo = uniqid() . ".wav"; // Cria um nome único
    $caminhoCompleto = $target_dir . $nomeArquivo;

    // pega os dados vindo do POST
    $rawData = file_get_contents("php://input");

    // executa a criação do arquivo de áudio e checagem
    if (file_put_contents($caminhoCompleto, $rawData)) {
        
        // executar o script do python para que ele crie o audio resposta.wav

        // espaceshellcmd e escapeshellarg podem ser substituídos pelo shell_exec,
        // mas foram colocados por segurança de caracteres especiais
        $command = escapeshellcmd("python3 process_audio.py " . escapeshellarg($caminhoCompleto));
        $resultado = shell_exec($command);

        // procura o arquivo de resultado do python 
        // caso o php continue lendo o código sem o python ter encerrado
        $tentativas = 0;
        $result_file = "NIK/Esp32/result.txt";
        while (!file_exists($result_file)) {
            // manter na média 20 segundos
            if (++$tentativas > 200) {
                // Sai do loop mas continua o script
                break;
            }
            usleep(100000); // espera 100ms
        }

        // última checagem da existencia do arquivo de resposta
        if(!file_exists($result_file)){
            ErrorAudio();
            exit;
        }
        // como ele existe, o php pode apagá-lo e continuar a execução
        unlink($result_file);
        
         // Retornar resposta de áudio ao esp32
        $respostaAudio = "NIK/Esp32/response.wav"; // caminho do arquivo a ser devolvido

        // verifica se o arquivo existe
        if (file_exists($respostaAudio)) {

            // envio de audio
            header("Content-Type: audio/wav");      // ou outro tipo correto do arquivo
            header("Content-Length: " . filesize($respostaAudio));
            header("Content-Disposition: attachment; filename=response.wav");
            readfile($respostaAudio);

            //depois disso, o arquivo de áudio é excluido
            unlink($respostaAudio);

            // encerra o código
            exit;

        } else {

            ErrorAudio();
        }
    } else {
        ErrorAudio();
    }
} else {
    ErrorAudio();
}

function ErrorAudio(){

    // Caminho para o arquivo de áudio de erro
    $error_audio_path = "NIK/Error_case/response.wav";
    
    // Verificar se o arquivo de erro existe
    if (file_exists($error_audio_path)) {

        // Definir o tipo de conteúdo como áudio WAV
        header("Content-Type: audio/wav");     
        header("Content-Length: " . filesize($error_audio_path));
        header("Content-Disposition: attachment; filename=response.wav");

        // Ler e enviar o arquivo de áudio
        readfile($error_audio_path);

        exit;

    } else {
        // Caso o arquivo de erro não exista, enviar um código de erro HTTP 500
        http_response_code(500);
        echo "Erro interno do servidor: áudio de erro não encontrado.";
    }
}

