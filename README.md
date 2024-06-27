# Projeto IA - Reconhecimento de emoções

<aside>
💡 A ideia principal do projeto é utilizar uma API da Google (Cloud Vision), para extrair emoções do usuário, pela webcam.

</aside>

Na configuração proposta, os equipamentos principais são: um botão, um monitor, uma Raspberry Pi e uma webcam. O procedimento se inicia com o usuário posicionando seu rosto diante da webcam para que seja exibido na tela do monitor. Em seguida, o botão é pressionado para acionar o processo de captura de imagem. Automaticamente, a foto é tirada e os dados faciais são enviados para uma API por meio de uma requisição. Após um curto período, a foto capturada é apresentada na tela juntamente com um retângulo que delimita o rosto do usuário, acompanhado de uma legenda que descreve a emoção identificada.


## `Esquema visual - Brainstorming:`

![Brainstorming](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/65148cd1-6bc1-43fa-b73c-59895b9457a3)

## `GCP:`

- Cloud Vision;
- Credenciais.

## `RASP:`

- Request → API GCP;
- JSON → Chaves.

## `Estética visual:`

Planejamento de uma estética visual visando o relacionamento entre o usuário, o monitor, e o botão que será usado para iniciar o processo de captura.

## **`Equipamentos:`**

- Raspberrry Pi 4;
- Monitor;
- Webcam.

## `Software:`

- Instalação do VSCODE;
- Instalação da Rasp OS Debian;
- Instalação do GIT.

## `Hardware:`

- Botão → Resistor → Pull-Down.

## Raspberry

→ Link para o site oficial:

[Raspberry Pi](https://www.raspberrypi.com/)

### O que é a Raspberry?

![Raspberry](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/b9b85bec-d499-4b02-9375-d6b8365db440)

O Raspberry Pi (RPi) é um microcomputador de placa única projetado pela Raspberry Pi Foundation, lançado inicialmente em 2012 com o modelo Raspberry Pi 1 Model B. Ele é uma alternativa acessível e compacta aos computadores tradicionais, contendo todos os componentes essenciais em uma única placa.

Equipado com processador, memória RAM, placa de vídeo integrada e diversos conectores (como USB, HDMI, áudio e GPIO), o Raspberry Pi suporta sistemas operacionais baseados em Linux e pode ser utilizado para uma variedade de finalidades. Desde atividades educacionais em programação e eletrônica até projetos de automação residencial, servidores de mídia, IoT e prototipagem.

### Procedimento para utilização da Raspberry

**→ Download da imagem da Raspberry no cartão SD**

![Download Rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/43c0610e-1f53-4f49-a8e4-995e1e0473f7)

**→ Configurar Raspberry Pi Imager**

![Customisation Rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/8344d348-7e68-4a7c-832f-895cf0a83e82)

- **Raspberry Pi Device:** Raspberry Pi 4;
- **Operating System:** Raspberry Pi OS (64-bit);
- **Storage:** Generic- SD/MMC/MS PRO USB Device-31.9GB.

**→ NEXT**

![Settings rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/a07bbbdd-b534-4ff2-beec-7f1f6c07fe0d)

**→ EDIT SETTINGS**

→ GENERAL:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/df22d4e2-0408-43fc-b139-e6be3d34d022/ba3cc7bc-355c-42f0-87ed-925e1dd1ddac/Untitled.png)

Configurações:

- **Set hostname:** projetoIA;
- **Username:** instrutor;
- **Set locale settings**
- **Time zone:** America/Sao_Paulo;
- **Keyboard layout:** pt.

→ SAVE

→ SERVICES:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/df22d4e2-0408-43fc-b139-e6be3d34d022/01e46258-896b-4ef1-8a69-002b9e08b236/Untitled.png)

Enable SSH ✅

SSH - É um protocolo de comunicação remoto via terminal, pelo terminal conseguimos acessar a RASP e realizar configurações.

→ SAVE

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/df22d4e2-0408-43fc-b139-e6be3d34d022/1440e6e4-9524-4853-ad29-22c2314a496e/Untitled.png)

→ Clicar no botão “YES” para a criação da imagem no cartão SD.

