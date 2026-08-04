🐌 Den Den Mushi AI | Galley-La Company

Este projeto é uma solução de Inteligência Artificial Generativa desenvolvida para o Challenge Oracle + Alura (ONE AI For Tech). O Den Den Mushi AI atua como um assistente corporativo inteligente, projetado para auxiliar os carpinteiros e engenheiros navais da Galley-La Company (Water 7) na consulta de manuais técnicos, políticas de RH e tabelas de preços.

📝 Descrição do Projeto

O Den Den Mushi AI é um sistema de RAG (Retrieval-Augmented Generation). Diferente de um chatbot comum que tenta adivinhar respostas, este assistente recupera informações precisas de documentos internos da empresa antes de gerar uma resposta. O objetivo é reduzir o tempo gasto na busca por manuais impressos, otimizando a operação logística e de segurança nas Docas.

🏗️ Arquitetura

O sistema segue um pipeline de dados estruturado para garantir respostas contextuais:

Ingestão: Carregamento de documentos em variados formatos (PDF, DOCX, CSV) usando LangChain.

Processamento (Chunking): Os textos são fragmentados em pedaços menores (chunks) de 1000 caracteres para melhor processamento.

Embeddings: Conversão dos textos em vetores numéricos semânticos utilizando o modelo gemini-embedding-001.

Vector Store (ChromaDB): Armazenamento local desses vetores para permitir buscas rápidas baseadas em similaridade.

Geração (LLM): O modelo gemini-1.5-flash consome os dados recuperados e formula uma resposta em linguagem natural, mantendo o contexto corporativo.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.10+

Framework de IA: LangChain

LLM: Google Gemini 1.5 Flash

Banco Vetorial: ChromaDB

Interface: Streamlit

Ambiente de Execução: Local (com suporte a OCI - Oracle Cloud Infrastructure)

🚀 Instruções de Instalação

Pré-requisitos

Python 3.10 ou superior instalado.

Uma API Key do Google AI Studio.

Passo a Passo

Clone o repositório:

git clone https://github.com/seu-usuario/den-den-mushi-ai.git
cd den-den-mushi-ai


Crie um ambiente virtual:

python -m venv venv
# No Windows:
.\venv\Scripts\Activate.ps1
# No Linux/Mac:
source venv/bin/activate


Instale as dependências:

pip install -r requirements.txt


Configure o ambiente:
Crie um arquivo .env na raiz do projeto e adicione sua chave:

GEMINI_API_KEY=sua_chave_aqui


Execute a aplicação:

streamlit run app.py


💬 Exemplos de Perguntas e Respostas

Pergunta: "O que devemos fazer se a Aqua Laguna nível 3 for anunciada?"
Resposta: "Quando o alarme de nível 3 soar, todos os carpinteiros devem evacuar a Doca 1 imediatamente. Ferramentas pesadas devem ser presas ao solo ou levadas para o andar superior."

Pergunta: "Qual é o custo de um Galeão de Batalha da Marinha?"
Resposta: "Com base na nossa tabela de preços atualizada, o Galeão de Batalha (Marinha) tem um preço base de 300.000.000 Beries."

Desenvolvido por Wagner | Challenge Oracle + Alura