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

→ Link para o site oficial: [Raspberry Pi](https://www.raspberrypi.com/)

### O que é a Raspberry?

![Raspberry](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/b9b85bec-d499-4b02-9375-d6b8365db440)

O Raspberry Pi (RPi) é um microcomputador de placa única projetado pela Raspberry Pi Foundation, lançado inicialmente em 2012 com o modelo Raspberry Pi 1 Model B. Ele é uma alternativa acessível e compacta aos computadores tradicionais, contendo todos os componentes essenciais em uma única placa.

Equipado com processador, memória RAM, placa de vídeo integrada e diversos conectores (como USB, HDMI, áudio e GPIO), o Raspberry Pi suporta sistemas operacionais baseados em Linux e pode ser utilizado para uma variedade de finalidades. Desde atividades educacionais em programação e eletrônica até projetos de automação residencial, servidores de mídia, IoT e prototipagem.

### Procedimento para utilização da Raspberry

**→ Download da imagem da Raspberry no cartão SD**

![Download Rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/43c0610e-1f53-4f49-a8e4-995e1e0473f7)

**→ Configurar Raspberry Pi Imager**

![Config rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/29791fca-ad97-4d61-bffe-ee43250a3af7)

- **Raspberry Pi Device:** Raspberry Pi 4;
- **Operating System:** Raspberry Pi OS (64-bit);
- **Storage:** Generic- SD/MMC/MS PRO USB Device-31.9GB.

**→ NEXT**

![Customisation Rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/8344d348-7e68-4a7c-832f-895cf0a83e82)

**→ EDIT SETTINGS**

→ GENERAL:

![Settings rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/a07bbbdd-b534-4ff2-beec-7f1f6c07fe0d)

Configurações:

- **Set hostname:** projetoIA;
- **Username:** instrutor;
- **Set locale settings**
- **Time zone:** America/Sao_Paulo;
- **Keyboard layout:** pt.

→ SAVE

→ SERVICES:

![Services rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/2c7861d8-8ddd-413a-b28b-e59ce0b62115)

Enable SSH ✅

SSH - É um protocolo de comunicação remoto via terminal, pelo terminal conseguimos acessar a RASP e realizar configurações.

→ SAVE

![SAVE RASP](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/8e28c164-d4c5-4573-8ebd-8418f36f6557)

→ Clicar no botão “YES” para a criação da imagem no cartão SD.

## Python

→ Link para o site oficial: [Python](https://www.python.org/)

### Preparação do ambiente - Python:

→ Instalação e Configuração do VScode

Obs: A instalação do VScode foi realizada somente para o desenvolvimento do projeto. Após a aprovação da interface, a utilização do python passou a ser utilizada pelo terminal, para melhorar a otimização.

*Antes da instalação do VScode, a própria Rasp dá uma opção para a atualização dos sistema operacional.

→ No terminal:

```python
pip install code
```

```python
code
```

→ No VScode, realizar a instalação e ativação do python (extensões): 

![Extensoes Py](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/6926ddcb-4f7e-4faf-9f1c-7b189e5482e0)

---

### `Configuração do ambiente sem o VScode`

→ Preparação do ambiente pelo terminal:

- Atualização dos pacotes da RASP

```jsx
sudo apt-get update
sudo apt-get upgrade
```

- Criação de pasta para o projeto

```jsx
MKDIR ProjetoIA
```

- Clonar o repositório do git

```jsx
git clone https://github.com/ccadu86/IA-EMO-ES.git
```

- Criação de ambiente virtual

```jsx
python -m venv venv
```

- Ativar ambiente virtual

```jsx
source venv/bin/activate
```

- Instalações das bibliotecas

```jsx
pip install opencv-python
pip install --upgrade google-cloud-vision
pip install RPi-GPIO
```

- Start aplicação

```jsx
python main.py
```

## Cloud Vision API

**Documentação do Cloud Vision**

[Documentação do Cloud Vision  |  Cloud Vision API  |  Google Cloud](https://cloud.google.com/vision/docs?hl=pt-br)

- ACESSAR GOOGLE CLOUD PLATFORM (GCP):

[Cloud Computing Services | Google Cloud](https://cloud.google.com/)

1. Resgate dos créditos (US$300) para o projeto
2. Acesso ao produto: **Cloud Vision API**

---

- Ao realizar o acesso à plataforma, há um projeto pré-criado pela plataforma. Porém, foi optado a criação de um novo projeto.

**Nome do Projeto**: IA - EMOCOES

- Utilização do **Face Detection**, funcionalidade disponível na IA do Cloud Vision.
- Ativação da API do Cloud Vision pela plataforma.

---

Detalhes do Produto - Cloud Vision API

**Valor para utilização da API - FACE DETECTIONS OPERATIONS:**

| REQUISIÇÕES | 0 até < 1000/mês | > 1000/mês |
| --- | --- | --- |
| BRL | 0,00 | 8,870629612 |
- Reconhece a emoção a partir da captura de imagem.
- Ao realizar a habilitação da API é necessário uma credencial de API para realizar acessos.
- Criação de uma **Conta de Serviço: IA_EMOCOES**. Ao criar uma ****conta de serviço é possível utilizar qualquer serviço do Google Cloud Platform.
- Done
- Acesso à conta
- Acesso às Chaves e gerar arquivo JSON (***credentials.json***)

## Integração com a Webcam

→ Realização dos primeiros testes da integração da WebCam.

**Ideia Principal**

Na Raspberry é feito um Request na API do Cloud Vision, que nos disponibilizará um JSON com as informações geradas a partir da requisição.

Dentro do JSON deve ser procurado a chave onde é informada as emoções que foram encontradas.

*Tarefa realizada após a configuração da API.

- No terminal, instalar a biblioteca do Google com o seguinte comando:

```html
pip install --upgrade google-cloud-vision
```

### `Teste 1:`

- Criação do arquivo def_imports.py

```python
from google.cloud import vision

def detect_faces(path):
    """Detecta rostos em uma imagem."""

    # Cria um cliente para o serviço de anotação de imagens do Google Cloud Vision
    client = vision.ImageAnnotatorClient()

    # Abre o arquivo de imagem no caminho especificado e lê seu conteúdo
    with open(path, "rb") as image_file:
        content = image_file.read()

    # Cria um objeto de imagem a partir do conteúdo lido
    image = vision.Image(content=content)

    # Solicita a detecção de rostos na imagem
    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Nomes das probabilidades de emoções, conforme definido no google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",         # Desconhecido
        "VERY_UNLIKELY",   # Muito Improvável
        "UNLIKELY",        # Improvável
        "POSSIBLE",        # Possível
        "LIKELY",          # Provável
        "VERY_LIKELY",     # Muito Provável
    )
    print("Faces:")

    # Itera sobre cada rosto detectado na imagem
    for face in faces:
        # Imprime a probabilidade de cada emoção para o rosto detectado
        print(f"anger: {likelihood_name[face.anger_likelihood]}")      # Raiva
        print(f"joy: {likelihood_name[face.joy_likelihood]}")          # Alegria
        print(f"surprise: {likelihood_name[face.surprise_likelihood]}") # Surpresa

        # Obtém as coordenadas dos vértices do polígono delimitador do rosto
        vertices = [
            f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
        ]

        # Imprime as coordenadas dos vértices do rosto
        print("face bounds: {}".format(",".join(vertices)))

    # Verifica se houve algum erro na resposta
    if response.error.message:
        # Levanta uma exceção com a mensagem de erro e um link para mais informações
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
```

- Criação do arquivo main.py

```python
from def_imports import *
import os

os.environ ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

print(detect_faces('foto.jpeg'))
```

- Resultado no terminal após o teste:

```python
(.venv) instrutor@proetoIA:~/Documents/IA-EMO-ES $ python main.py
Faces:
anger: VERY_UNLINKELY
joy: VERY_LIKELY
surprise: VERY_UNLIKELY
face nounds: (246,67), (775,67), (775,683), (246,683)
None
```

### `Teste 2:`

- Arquivo def_imports.py

```python
from google.cloud import vision

def detect_faces(path):
    """Detecta rostos em uma imagem."""

    # Cria um cliente para o serviço de anotação de imagens do Google Cloud Vision
    client = vision.ImageAnnotatorClient()

    # Abre o arquivo de imagem no caminho especificado e lê seu conteúdo
    with open(path, "rb") as image_file:
        content = image_file.read()

    # Cria um objeto de imagem a partir do conteúdo lido
    image = vision.Image(content=content)

    # Solicita a detecção de rostos na imagem
    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Nomes das probabilidades de emoções, conforme definido no google.cloud.vision.enums
    likelihood_name = (
        "UNKNOWN",         # Desconhecido
        "VERY_UNLIKELY",   # Muito Improvável
        "UNLIKELY",        # Improvável
        "POSSIBLE",        # Possível
        "LIKELY",          # Provável
        "VERY_LIKELY",     # Muito Provável
    )
    print("Faces:")

#Comentar essa parte
    # Itera sobre cada rosto detectado na imagem
    #for face in faces:
        # Imprime a probabilidade de cada emoção para o rosto detectado
        #print(f"anger: {likelihood_name[face.anger_likelihood]}")      # Raiva
        #print(f"joy: {likelihood_name[face.joy_likelihood]}")          # Alegria
        #print(f"surprise: {likelihood_name[face.surprise_likelihood]}") # Surpresa

        # Obtém as coordenadas dos vértices do polígono delimitador do rosto
        #vertices = [
            #f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
        #]

        # Imprime as coordenadas dos vértices do rosto
        #print("face bounds: {}".format(",".join(vertices)))

    # Verifica se houve algum erro na resposta
    if response.error.message:
        # Levanta uma exceção com a mensagem de erro e um link para mais informações
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
```

- Arquivo main.py

```python
from def_imports import *
import os

os.environ ["GOOGLE_APPLICATION_CREDENTIALS"] = 'credentials.json'

print(detect_faces('foto.jpeg'))
```

- Resultado no terminal após o teste:

```python
Faces: [bounding_poly {
	vertices {
		x: 246
		y: 67
	}
	vertices {
		x: 775
		y: 67
	}
	vertices {
		x: 775
		y: 683
	}
	vertices {
		x: 246
		y: 683 
	}
}
fd_bounding_poly {
	vertices {
		x: 301
		y: 220
	}
	vertices {
		x: 718
		y: 220
	}
	vertices {
		x: 718
		y: 637
	}
	vertices {
		x: 301
		y: 637 
	} 
} 
landmarks {
	type_:
		LEFT_EYE position {
			x: 434.759918
			y: 365.621918
			z: -0.00130653381
		}
	}
	landmarks {
		type_: RIGHT_EYE position {
			x: 594.609863
			y: 365.956329
			z: 3.84433651
		}
	}
	landmarks {
		type_: LEFT_OF_LEFT_EYEBROW position {
			x: 380.010223
			y: 323.234192
			z: 14.1111031
		}
	}
	landmarks {
		type_: RIGHT_OF_LEFT_EYEBROW position {
			x: 478.717926
			y: 319.387024
			z: -26.6964569
		}
	} 
	landmarks {
		type_: LEFT_OF_RIGHT_EYEBROW position {
			x: 550.675232
			y: 320.928833
			z: -25.0222549
		}
	}
	landmarks {
		type_: RIGHT_OF_RIGHT_EYEBROW position {
			x: 648.830078
			y: 323.236908
			z: 20.5603962
		}
	}
	landmarks {
		type_: MIDPOINT_BETWEEN_EYES position {
			x: 514.295654
			y: 359.641
			z: -29.4551201
		}
	}
	landmarks {
		type_: NOSE_TIP position {
			x: 515.89563
			y: 451.595
			z: -77.2197418
		}
	}
	landmarks {
		type_: UPPER_LIP position {
			x: 516.562256
			y: 504.816071
			z: -43.5845261
		}
	}
	landmarks {
		type_: LOWER_LIP position {
			x: 515.569275
			y: 563.684875
			z: -34.6525879
		}
	}
	landmarks {
		type_: MOUTH_LEFT position {
			x: 429.596313
			y: 518.402222
			z: -2.25559235
		}
	}
	landmarks {
		type_: MOUTH_RIGHT position {
			x: 595.857117
			y: 520.15271
			z: 0.89873457
		}
	}
	landmarks {
		type_: MOUTH_CENTER position {
			x: 515.725708
			y: 532.28772
			z: -33.1510773
		}
	}
	landmarks {
		type_: NOSE_BOTTOM_RIGHT position {
			x: 566.228821
			y: 465.132111
			z: -19.8852158
		}
	}
	landmarks {
		type_: NOSE_BOTTOM_LEFT position {
			x: 463.280396
			y: 463.98996
			z: -21.9731503
		}
	}
	landmarks {
		type_: NOSE_BOTTOM_CENTER position {
			x: 516.443359
			y: 479.795929
			z: -43.8077888
		}
	} landmarks {
		type_: LEFT_EYE_TOP_BOUNDARY position {
			x: 434.96814
			y: 350.403656 
			z: -8.28114414
		}
	}
	landmarks {
		type_: LEFT_EYE_RIGHT_CORNER position {
			x: 469.078186
			y: 367.866638
			z: 0.688108444
		}
	}
	landmarks {
		type_: LEFT_EYE_BOTTOM_BOUNDARY position {
			x: 434.007385 
			y: 377.524109 
			z: -1.99274445
		}
	}
	landmarks {
		type_: LEFT_EYE_LEFT_CORNER position {
			x: 400.206451 
			y: 366.176056 
			z: 13.1190462 
		}
	}
	landmarks {
		type_: RIGHT_EYE_TOP_BOUNDARY position {
			x: 595.895569 
			y: 352.349976 
			z: -4.51774073
		}
	}
	landmarks {
		type_: RIGHT_EYE_RIGHT_CORNER position { 
			x: 627.879883 
			y: 368.318695 
			z: 18.5005665
		}
	}
	landmarks {
		type_: RIGHT_EYE_BOTTOM_BOUNDARY position {
			x: 595.238098 
			y: 377.830048 
			z: 1.95094728
		}
	} 
	landmarks {
		type_: RIGHT_EYE_LEFT_CORNER position {
			x: 563.714844 
			y: 367.412201 
			z: 2.98846149
		}
	}
	landmarks { 
		type_: LEFT_EYEBROW_UPPER_MIDPOINT position {
			x: 428.018341 
			y: 306.688873 
			z: -15.4812593
		}
	} 
	landmarks { 
		type_: RIGHT_EYEBROW_UPPER_MIDPOINT position { 
			x: 600.341064 
			y: 307.378357 
			z: -11.4225082
		}
	} 
	landmarks { 
		type_: LEFT_EAR_TRAGION position { 
			x: 326.388641 
			y: 418.985199 
			z: 187.66629
		}
	}
	landmarks {
		type_: RIGHT_EAR_TRAGION position {
			x: 693.065 
			y: 419.866425 
			z: 196.387131
		}
	} 
	landmarks {
		type_: FOREHEAD_GLABELLA position { 
			x: 512.72876 
			y: 323.332184 
			z: -31.4045334
		}
	}
	landmarks {
		type_: CHIN_GNATHION position { 
			x: 517.847595 
			y: 640.319214 
			z: -15.0868464
		}
	} 
	landmarks { 
		type_: CHIN_LEFT_GONION position {
			x: 353.873596 
			y: 549.23877 
			z: 119.562744
		}
	}
	landmarks {
		type_: CHIN_RIGHT_GONION position {
			x: 660.976318 
			y: 554.016 
			z: 127.350922
		}
	}
	landmarks {
		type_: LEFT_CHEEK_CENTER position {
			x: 398.043488 
			y: 464.291412 
			z: 11.6552858 
		}
	}
	landmarks {
		type_: RIGHT_CHEEK_CENTER position {
			x: 630.060547 
			y: 466.530945 
			z: 16.9067898
		}
	}
	roll_angle: -0.0073674405
	pan_angle: 1.40242183 
	tilt_angle: 0.687861621 
	detection_confidence: 0.98046875 
	landmarking_confidence: 0.723549843 
	joy_likelihood: VERY_LIKELY 
	sorrow_likelihood: VERY_UNLIKELY 
	anger_likelihood: VERY_UNLIKELY 
	surprise_likelihood: VERY_UNLIKELY 
	under_exposed_likelihood: VERY_UNLIKELY 
	blurred_likelihood: VERY_UNLIKELY 
	headwear_likelihood: VERY_LIKELY 
]

## Configuração do Hardware

![a.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/df22d4e2-0408-43fc-b139-e6be3d34d022/e7520a8c-3d27-4aec-bcda-e08b6c7b8ad5/a.png)

### Sistema de Pull Down da Raspberry Pi 4

Utilizamos um circuito com resistores de pull-down integrados ao pino GPIO17 (General Purpose Input/Output). Esse resistor é utilizado para garantir que os pinos GPIO tenham um estado definido (alto ou baixo) quando não está sendo ativamente acionado por um dispositivo externo, no caso o botão presente no nosso projeto.

**Resistores de Pull Down**

- **Pull Down**: Um resistor de pull-down é conectado entre o pino GPIO e o terra (GND). Assegurando que o pino esteja em um estado de baixo (0V) quando nenhum sinal é aplicado. Sem o resistor de pull-down, o pino ficaria flutuante e poderia ler valores imprevisíveis devido a interferências elétricas.

**Configuração**

Na Raspberry Pi, os resistores de pull-down podem ser configurados programaticamente usando a biblioteca GPIO (por exemplo, RPi.GPIO no Python).

```jsx
import RPi.GPIO as GPIO

# Configura o modo da pinagem
GPIO.setmode(GPIO.BCM)

# Define o pino 17 (GPIO 17) como entrada com pull-down
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
```

### Utilização de Portas e Fios no Pinout da Raspberry Pi 4

- **Porta GROUND** (9): FIO MARROM
    - **Função**: Conexão ao terra (GND) da Raspberry Pi. Isso fornece um referencial de 0V para os circuitos.
    
- **Porta GPIO 17** (11): FIO AMARELO
    - **Função:** Sensor que realiza o envio de sinal. Configurado como uma entrada com resistor de pull-down.
    
- **Porta GPIO 27** (13): FIO LARANJA (reserva)
    - **Função**: Outro pino GPIO configurável. Reservado para futuras conexões ou utilizações.

- **Porta 3V3 power** (17): FIO VERMELHO
    - **Função**: Fornece uma saída de 3.3V da Raspberry Pi. É utilizado como alimentação de sensores ou outros componentes eletrônicos que operam com 3.3V.

Diagrama de pinagem da Raspberry Pi 4:
![diagrama](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/955c4a51-f12b-48f7-84f9-a323395c176a)

![rasp](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/8a6688f0-d393-4010-b7e9-74b30a5f2755)

**Componente botão**

- Realiza o pull-down na operação.

![Botão](https://github.com/ccadu86/IA-EMO-ES/assets/134337212/a34fc537-d9c5-4bbb-a711-4d461bc52393)

```

