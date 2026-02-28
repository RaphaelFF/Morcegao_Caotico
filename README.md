# Morcegao_Caotica

![capa provisoria](capa.png)
<h4 align="center"><a href="https://www.notion.so/G-D-D-Morceg-o-Caotica-2b5a1d75416980c49744ee21f420d816?source=copy_link">Clique para Acessar o Game Design Document (GDD) do projeto</a></h4>

---

## 📝 Sobre o Projeto

**Morcegão Caótico** é um jogo de arcade desenvolvido em **Python**, utilizando a biblioteca **Pygame**. Inspirado em jogos do estilo *endless runner*, o jogador controla um morcego que deve desviar de obstáculos (canos) enquanto os cenários e a dificuldade mudam dinamicamente conforme a pontuação aumenta.

---

## 🚀 Como Executar

### 📋 Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

* **Python 3.13 +**
* **Pygame 2.5.2 +**
* Sistema operacional: Windows, Linux ou macOS

---

### 📦 Instalação

1. Clone o repositório para sua máquina local:

```bash
https://github.com/RaphaelFF/Morcegao_Caotico.git
```

2. Acesse a pasta do projeto:

```bash
cd Morcegao_Caotico
```

3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

> Caso não possua o arquivo `requirements.txt`, instale manualmente:
>
> ```bash
> pip install pygame==2.5.2
> ```

---

### ▶️ Executando o jogo

Após instalar as dependências, execute o comando:

```bash
python app.py
```

O jogo será iniciado em uma nova janela.

---

## 🎮 Controles

* **Barra de Espaço** ou **Clique do mouse**: faz o morcego subir
* Sem interação: o morcego desce automaticamente

---

## 📁 Estrutura do Projeto

```text
Morcegao_Caotico/
│
├── app.py                # Arquivo principal do jogo
├── configuracoes.py      # Configurações gerais (tela, FPS, dificuldade)
├── README.md             # Documentação do projeto
│
├── assets/
│   ├── img/              # Imagens (cenários, jogador, obstáculos, UI)
│   └── audio/            # Sons e efeitos sonoros
│
├── modulos/
│   ├── inicio.py         # Tela inicial do jogo
│   ├── jogo.py           # Loop principal e mecânicas
│   ├── fim_de_jogo.py    # Tela de Game Over
│   └── utilitarios.py    # Funções auxiliares
│
└── capa.png              # Imagem de capa do projeto
```

---

## ℹ️ Observações

* Os cenários, canos e variações visuais são escolhidos de forma **aleatória** a cada partida.
* A dificuldade aumenta a cada 10  pontos.
* Os sons são carregados automaticamente em `.wav` ou `.ogg`.
