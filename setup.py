from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Dependências principais
install_requires = [
    # Dependências principais
    "streamlit==1.31.0",
    "python-dotenv==1.0.0",
    
    # CrewAI e dependências
    "crewai==0.11.1",
    "langchain-community==0.0.14",
    "langchain-openai==0.0.5",
    
    # Processamento de texto
    "markdown==3.4.3",
    "markdown-it-py==2.2.0",
    "mdurl==0.1.2",
    
    # OpenAI
    # tiktoken removido pois requer compilação
    "openai>=1.7.1,<2.0.0",  # Atualizado para atender ao requisito do crewai
    
    # Processamento de dados
    "numpy>=1.22.0,<1.25.0",  # Versão pré-compilada para evitar problemas
    "pydantic>=2.4.2,<3.0.0",  # Compatível com crewai
    
    # PDF e formatação - simplificado para evitar problemas de compilação
    "reportlab==3.6.13",
    
    # Outras dependências
    "requests==2.31.0",
    "duckduckgo-search==3.9.6",
    
    # Dependências com versões fixas para evitar conflitos
    "rich==13.7.0",
    "instructor>=0.5.2,<0.6.0",  # Versão compatível com crewai
    
    # Adicionando setuptools para resolver problema com distutils
    "setuptools>=65.5.0"
]

# Configuração para evitar instalação de dependências opcionais
def exclude_deps():
    import os
    import sys
    
    # Evitar instalação de dependências opcionais problemáticas
    os.environ["SKIP_CHROMADB_INSTALL"] = "1"
    os.environ["SKIP_SENTENCE_TRANSFORMERS"] = "1"
    os.environ["SKIP_FAISS"] = "1"
    
    # Se estiver no Streamlit Cloud, evite dependências pesadas
    if os.environ.get("STREAMLIT_SERVER_RUNNING") == "true":
        return ["chromadb", "faiss-cpu", "sentence-transformers"]
    return []

setup(
    name="healph_articles",
    version="0.1.0",
    author="Rafael Araújo",
    author_email="seu.email@exemplo.com",
    description="Gerador de Artigos de Saúde com IA usando CrewAI e Streamlit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/araujobazilio/healph_articles",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires=">=3.10",
    exclude_deps=exclude_deps(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    keywords="ai health medical article generation crewai streamlit",
    project_urls={
        "Bug Reports": "https://github.com/araujobazilio/healph_articles/issues",
        "Source": "https://github.com/araujobazilio/healph_articles",
    },
    include_package_data=True
)
