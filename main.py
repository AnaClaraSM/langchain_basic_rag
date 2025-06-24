# Imports
import os # Interação com o s.o
from langchain_community.document_loaders import WebBaseLoader # Carregador de texto de páginas web
from langchain_text_splitters import RecursiveCharacterTextSplitter # Divisor de textos em chunks
from langchain_openai import OpenAI, OpenAIEmbeddings # LLM e Embeddings OpenAI
from langchain.chains import RetrievalQA #
from langchain_community.vectorstores import Chroma # Banco de dados vetorial
from bs4 import BeautifulSoup
from dotenv import load_dotenv # Variáveis de ambiente


# Carrega as variáveis de ambiente
load_dotenv()

# Configura a chave OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")

# Carrega o documento da Web
url = "https://pt.wikipedia.org/wiki/Buraco_negro"
loader = WebBaseLoader(url)
documents = loader.load()

# Divide o texto em chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# Configura os embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=openai_api_key)

# Vector Store
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma-db"
)

retriever = vectorstore.as_retriever()

# Pipeline (cadeia de ações) RAG
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0, api_key=openai_api_key),
    retriever = retriever,
    return_source_documents = True
)

# Chat Loop
while True:

    # Pergunta
    query = input("Pergunte alguma coisa: ")
    response = qa.invoke(query)

    # Resposta
    print("Resposta: ", response["result"])
    print("\tFontes: ")
    printed_sources = set()
    for doc in response["source_documents"]:
        source = doc.metadata.get("source")
        if source and source not in printed_sources:
            print("\t-", source)
            printed_sources.add(source)