
# include <WiFi.h>
# include <HTTPClient.h>
# include <WiFiClientSecure.h>
# include <SPIFFS.h>
# include <FS.h>
#include <driver/i2s.h>

// URL de aonde se localiza o servidor em que o php está
String URL = "C:/xampp/htdocs/diretorio_do_arq/arquivo.php";
// ou        "http://ip_do_computador/diretorio_do_arq/arquivo.php"

// para saber, apenas entre no cmd e coloque "ipconfig"


// Como vamos fazer com que o Esp32 conecte-se a internet desse jeito?
const char* ssid = "SSID"; //<-- Nome da internet
const char* password = "PASSWORD"; //<-- Senha

void saveResponseFile(HTTPClient& http, const char* caminho) {
  // transcreve a resposta do http á um arquivo de audio no caminho dado
  
  File f = SPIFFS.open(caminho, "w");
  // verifica se não ocorreu erro ao abrir novo arquivo para a escrita
  if (!f) return false;

  WiFiClient* stream = http.getStreamPtr();
  uint8_t buf[128];
  int len = http.getSize();

  while (http.connected() && (len > 0 || len == -1)) {
    size_t size = stream->available();
    if (size) {
      int c = stream->readBytes(buf, min(size, sizeof(buf)));
      f.write(buf, c);
      if (len > 0) len -= c;
    }
    delay(1);
  }

  f.close();
  return true;
}

void setup() {
  Serial.begin(4800);
  delay(3000);

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // iniciando conexão
  WiFi.begin(ssid, password);

  // aguardando a conexão ser feita
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
    /*
    ---------------------
    CÓDIGO DA GRAVAÇÃO DO ÁUDIO
    ---------------------
    */

  /*
  ------------------------
  CÓDIGO DA COMUNICAÇÃO DE RESPOSTA COM O PHP
  */

  // checagem se a conexão está ainda ativa
  if(WiFi.status() == WL_CONNECTED) {

    // pega o arquivo de audio salvo pelo microfone
    File command = SPIFFS.open("/wavFile.wav","r");

    // verifica se o arquivo EXISTE
    if(!command){
      Serial.println("Arquivo não encontrado");
    } else {

      HTTPClient http;
      // determina um tempo limite para que o 
      // usuário não fique esperando
      http.setTimeout(10000);

      // determina aonde o esp32 vai enviar e pegar audio devolta
      http.begin(URL);

      // determina o tipo de informação que vai ser enviado
      //nesse caso, o arquivo de áudio
      http.addHeader("Content-Type", "application/octet-stream");

      // envio e espera pela resposta
      // esse código envia ao PHP o arquivo de audio e aguarde desse PHP um arquivo de áudio resposta

      // code armazena a resposta do resultado da conexão, o arquivo de audio devolutivo é armazenado dentro do esp32
      int code = http.sendRequest("POST", &command, command.size());
      /* Definir ao PHP no retorno de resposta como:
      header("Content-Type: audio/wav");
      header("Content-Disposition: attachment; filename=saida.wav");
      readfile("uploads/saida.wav");
      */
      
      command.close();

      // sucesso ou não o retorno, o audio do usuário será apagado

      if(SPIFFS.remove(command)){
        Serial.println("Comando do usuário deletado")
      } else {
        Serial.println("Erro ao deletar o comando do usuário")
        
      }

      // checagem do retorno
      if (code == 200){
        // envio feito com sucesso
        // será transcrevido a resposta do http a um arquivo de audio
        if (saveResponseFile(http, "/response.wav")){
          Serial.println("Áudio salvo com sucesso!");

          /* ----------------------------------------------
          CÓDIGO PARA TRANSMITIR O ÁUDIO PARA O AUTO FALANTE
          -------------------------------------------------
          
          1º Obs: parece que o I2S também consegue
          2º Obs: fazer isso em uma função separada porque isso será utilizado em outras partes do programa
          */
        } else {
         Serial.println("Falha ao salvar áudio.");
        }
      } else if (code < 0){
        // o envio foi encerrado pelo timeout
        // uma dica seria deixar pronto um áudio para o usuário tenha uma resposta
         Serial.println("O tempo de resposta acabou");
      } else{
         Serial.println("Erro de conexão: %d\n", code);
        
      }

      http.end();

    }
  }
}
