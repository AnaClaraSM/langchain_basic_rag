# 🕳️ RAG com LangChain: Explorando Buracos Negros

Este é o meu primeiro sistema RAG (Retrieval-Augmented Generation), construído com **Python** e **LangChain**. O projeto utiliza uma página da Wikipédia sobre **buracos negros** como base de conhecimento, permitindo que você faça perguntas e receba respostas geradas por IA com base em conteúdos reais extraídos da web.

---

## 🔍 O que este projeto faz?

* Carrega o conteúdo da página da Wikipédia sobre buracos negros
* Divide o texto em *chunks* para facilitar a indexação
* Gera embeddings com o modelo `text-embedding-3-small` da OpenAI
* Armazena os vetores com a biblioteca **ChromaDB**
* Cria uma cadeia `RetrievalQA` com LangChain para responder perguntas
* Exibe a resposta e as fontes utilizadas

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

### 2. Instale as dependências

Crie um ambiente virtual e instale os pacotes:

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
```

Exemplo de `requirements.txt`:

```
langchain
langchain-community
openai
chromadb
beautifulsoup4
python-dotenv
```

### 3. Configure sua chave da OpenAI

Crie um arquivo `.env` na raiz do projeto:

```
OPENAI_API_KEY=sk-...
```

### 4. Execute o script

```bash
python main.py
```

---

## 💬 Exemplo de uso

```text
Pergunte alguma coisa: O que é um buraco negro?
Resposta: Um buraco negro é um objeto astronômico denso e massivo cujo intenso campo gravitacional impede qualquer coisa de escapar, nem mesmo a luz. Ele é formado pela deformação do espaço-tempo causada por uma massa suficientemente compacta, e possui um horizonte de eventos, que é o limite a partir do qual nada pode escapar. O buraco negro é caracterizado por sua capacidade de absorver tudo o que está ao seu redor, incluindo luz, e é classificado de acordo com sua massa e tamanho.

        Fontes:
        - https://pt.wikipedia.org/wiki/Buraco_negro
```

---

## 🛠️ Tecnologias utilizadas

* [Python](https://www.python.org/)
* [LangChain](https://www.langchain.com/)
* [OpenAI API](https://platform.openai.com/)
* [ChromaDB](https://www.trychroma.com/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Wikipedia](https://pt.wikipedia.org/wiki/Buraco_negro)

---

## 📌 Observações

* O sistema usa uma página fixa da Wikipédia, mas você pode adaptá-lo para qualquer outra página alterando a URL.
* Ideal para aprender os fundamentos de RAG com um caso real e acessível.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
