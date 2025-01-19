from sqlmodel import SQLModel, Session, create_engine
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Configuração do engine
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

# Função para inicializar o banco de dados
def create_db_and_tables():
    """
    Cria as tabelas no banco de dados com base nos modelos definidos.
    """
    SQLModel.metadata.create_all(engine)

# Gerenciador de contexto para sessões
@contextmanager
def get_session():
    """
    Fornece uma sessão para interagir com o banco de dados.
    """
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()

