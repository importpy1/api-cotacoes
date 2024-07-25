### Api de cotações de moedas

<div style="display: inline_block">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter" /> 

</div>

##

### 📜 Descrição 

Este projeto envolve o desenvolvimento de um script que faz uma requisição a uma API e retorna as cotações das principais moedas do mercado.

##

### 📚 Ferramentas e tecnologias tratadas nesse projeto

- Python
- Lib Requests
- Pandas e análise de dados
- JSON

##

### ⚙ Requisitos

Antes de iniciar, verifique se você tem o Python e uma IDE instalados em seu computador. Além disso, o script requer a instalação de bibliotecas como pandas, requests e json. Para instalá-las, execute o seguinte comando:

```
pip install pandas
pip install requests
pip install json
```

##

### ⚒️ Como rodar?

1. Clone o repositório:
   
```
git clone https://github.com/importpy1/api-cotacoes.git
```

2. Navegue até o diretório do projeto:

```
cd api-cotacoes
```

3. Execute o script Python:

```
python cotacoes.py
```

##

### ✏️ Licença

Proibida a utilização dos arquivos e códigos em questão para fins diferentes de aprendizado e estudo.

Claro! Aqui está um README completo para o seu projeto de API simples usando Flask:

```markdown
# API Simples em Python com Flask

Este repositório contém um exemplo simples de como criar uma API usando Flask. A API possui um único endpoint que retorna uma mensagem "Olá, Mundo!".

## Requisitos

- Python 3.x
- pip (Python package installer)

## Como Executar

Siga os passos abaixo para configurar e executar a aplicação:

### 1. Clone o Repositório

Clone este repositório para a sua máquina local:

```bash
git clone https://github.com/seu-usuario/minha_api_simples.git
cd minha_api_simples
```

### 2. Crie um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
source venv/bin/activate   # No Windows, use venv\Scripts\activate
```

### 3. Instale as Dependências

Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install flask
```

### 4. Execute a Aplicação

Inicie a aplicação executando o arquivo `app.py`:

```bash
python app.py
```

### 5. Acesse a API

Abra o seu navegador ou uma ferramenta como Postman e faça uma requisição GET para o seguinte endereço:

```
http://127.0.0.1:5000/api
```

Você deverá ver uma resposta JSON como esta:

```json
{
    "message": "Olá, Mundo!"
}
```

## Estrutura do Projeto

O projeto possui a seguinte estrutura de diretórios e arquivos:

```
minha_api_simples/
├── venv/
├── app.py
├── requirements.txt
└── README.md
```

- `app.py`: Contém o código da aplicação Flask.
- `requirements.txt`: Lista as dependências do projeto.
- `README.md`: Este arquivo, com informações sobre o projeto.

## Código da Aplicação

Aqui está o código completo do arquivo `app.py`:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify({'message': 'Olá, Mundo!'})

if __name__ == '__main__':
    app.run(debug=True)
```

## Como Contribuir

Se você quiser contribuir com este projeto, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature ou correção (`git checkout -b feature/nova-feature`).
3. Faça o commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o repositório remoto (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
```

Este README inclui todos os detalhes necessários para configurar, executar e entender a API simples criada com Flask. Adapte o link do repositório GitHub para o seu próprio repositório.
