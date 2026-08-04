import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader, CSVLoader, Docx2txtLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
try:
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
except ModuleNotFoundError:
    from langchain_classic.chains import create_retrieval_chain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Carregar variáveis de ambiente (API Key)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

# 2. Configurar a página do Streamlit
st.set_page_config(page_title="Galley-La Co. | Den Den Mushi", page_icon="🐌", layout="centered")
st.title("🐌 Den Den Mushi AI")
st.subheader("Galley-La Company - Water 7")
st.markdown("Assistente Inteligente Corporativo dos Carpinteiros.")

# 3. Função para carregar e processar os documentos
@st.cache_resource(show_spinner="Lendo manuais da Galley-La...")
def inicializar_base_de_conhecimento(key):
    pasta_documentos = "documentos"
    documentos = []
    
    if not os.path.exists(pasta_documentos):
        return None
        
    for arquivo in os.listdir(pasta_documentos):
        caminho_completo = os.path.join(pasta_documentos, arquivo)
        if arquivo.endswith(".pdf"):
            loader = PyPDFLoader(caminho_completo)
            documentos.extend(loader.load())
        elif arquivo.endswith(".docx"):
            loader = Docx2txtLoader(caminho_completo)
            documentos.extend(loader.load())
        elif arquivo.endswith(".csv"):
            try:
                loader = CSVLoader(caminho_completo, encoding="utf-8")
                documentos.extend(loader.load())
            except Exception:
                loader = CSVLoader(caminho_completo, encoding="latin-1")
                documentos.extend(loader.load())
            
    if not documentos:
        return None
        
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    textos_fatiados = text_splitter.split_documents(documentos)
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=key
    )
    
    vectorstore = Chroma.from_documents(textos_fatiados, embeddings)
    return vectorstore.as_retriever()

# 4. Inicializa o retriever e o Chat
if api_key:
    retriever = inicializar_base_de_conhecimento(api_key)
    
    if retriever:
        llm = ChatGoogleGenerativeAI(model="models/gemini-3.6-flash", google_api_key=api_key)
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Você é o Den Den Mushi AI, assistente da Galley-La Company em Water 7. Responda de forma amigável com base nos manuais: {context}"),
            ("human", "{input}")
        ])
        
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        
        st.divider()
        pergunta = st.chat_input("O que você deseja saber, carpinteiro?")
        
        if pergunta:
            with st.chat_message("user"):
                st.write(pergunta)
            with st.chat_message("assistant", avatar="🐌"):
                with st.spinner("Consultando os arquivos..."):
                    resposta = rag_chain.invoke({"input": pergunta})
                    texto_resposta = resposta.get("answer", "")
                    if isinstance(texto_resposta, list):
                        # Extrai o texto limpo caso venha em formato estruturado de blocos
                        partes = [item.get("text", "") for item in texto_resposta if isinstance(item, dict) and "text" in item]
                        texto_resposta = "".join(partes) if partes else str(texto_resposta)
                    st.write(texto_resposta)
    else:
        st.info("📂 Coloque seus PDFs/DOCXs na pasta 'documentos'.")
else:
    st.error("❌ Chave API não encontrada no arquivo .env!")