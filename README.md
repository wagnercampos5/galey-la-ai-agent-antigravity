🐌 Den Den Mushi AI | Galley-La Company

Este projeto é uma solução de Inteligência Artificial Generativa desenvolvida para o Challenge Oracle + Alura (ONE AI For Tech). O Den Den Mushi AI atua como um assistente corporativo inteligente, projetado para auxiliar os carpinteiros e engenheiros navais da Galley-La Company (Water 7) na consulta de manuais técnicos, políticas de RH e tabelas de preços.

🌐 Aplicação Online (Deploy)

Acesse a aplicação em tempo real:
👉 Den Den Mushi AI — Streamlit Community Cloud

📝 Descrição do Projeto

O Den Den Mushi AI é um sistema de RAG (Retrieval-Augmented Generation). Diferente de um chatbot comum que tenta adivinhar respostas, este assistente recupera informações precisas de documentos internos da empresa antes de gerar uma resposta. O objetivo é reduzir o tempo gasto na busca por manuais impressos, otimizando a operação logística e de segurança nas Docas de Water 7.

🏛️ Arquitetura da Solução

O sistema segue um pipeline de dados estruturado para garantir respostas contextuais e seguras:

[Documentos: PDF/DOCX/CSV] ──> [LangChain Text Splitter] ──> [Google Gemini Embeddings]
                                                                      │
                                                                      ▼
[Interface Streamlit] <── [LLM Gemini 1.5 Flash] <── [Contexto] <── [ChromaDB VectorStore]


Ingestão: Carregamento de documentos em variados formatos (PDF, DOCX, CSV) localizados na pasta documentos utilizando loaders do LangChain.

Processamento (Chunking): Os textos são fragmentados em pedaços menores (chunks) de 1000 caracteres com sobreposição de 200 caracteres para preservar o contexto.

Embeddings: Conversão dos fragmentos de texto em vetores numéricos semânticos utilizando o modelo models/gemini-embedding-001 do Google.

Vector Store (ChromaDB): Armazenamento e indexação local desses vetores para permitir buscas rápidas baseadas em similaridade vetorial.

Geração (LLM): O modelo gemini-1.5-flash consome o prompt estruturado juntamente com os trechos recuperados para formular uma resposta precisa em linguagem natural.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.10+

Framework de IA: LangChain

LLM & Embeddings: Google Gemini (gemini-1.5-flash & gemini-embedding-001)

Banco Vetorial: ChromaDB

Interface Gráfica: Streamlit

Hospedagem / Cloud: Streamlit Community Cloud

📸 Demonstração da Aplicação

Interface do Assistente

Exemplo de Resposta do Agente

💬 Exemplos de Perguntas e Respostas

📋 Exemplo 1: Recursos Humanos e Segurança

Pergunta: "O que devemos fazer se a Aqua Laguna nível 3 for anunciada?"

Resposta do Agente: "Quando o alarme de nível 3 soar, todos os carpinteiros devem evacuar a Doca 1 imediatamente. Ferramentas pesadas devem ser presas ao solo ou levadas para o andar superior. Os dias de chuva da Aqua Laguna são considerados Folga Remunerada para todos os funcionários."

🪵 Exemplo 2: Engenharia Naval

Pergunta: "Como devo proceder para cortar a Madeira Adam?"

Resposta do Agente: "O corte da Madeira Adam deve ser feito utilizando serras de liga de aço temperado resfriadas a água, pois serras comuns quebram imediatamente devido à densidade extrema da madeira. Acesso restrito aos principais contramestres."

💰 Exemplo 3: Tabela de Preços (Financeiro)

Pergunta: "Qual é a embarcação mais barata e qual seu prazo de entrega?"

Resposta do Agente: "A embarcação mais barata na nossa tabela de preços é o Bote Salva-vidas, custando 500.000 Beries, com prazo de entrega de 1 semana."

🚀 Instruções de Execução Local

Pré-requisitos

Python 3.10 ou superior instalado.

Uma API Key válida gerada no Google AI Studio.

Passo a Passo

Clone o repositório:

git clone https://github.com/wagnercampos5/galey-la-ai-agent-antigravity.git
cd galey-la-ai-agent-antigravity


Crie e ative um ambiente virtual:

python -m venv venv
# No Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# No Linux/Mac:
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Configure o arquivo de ambiente:
Crie um arquivo .env na raiz do projeto e insira sua chave:

GEMINI_API_KEY=sua_chave_aqui


Execute a aplicação:

streamlit run app.py


Desenvolvido por Wagner Campos — Challenge Oracle + Alura (ONE AI For Tech).