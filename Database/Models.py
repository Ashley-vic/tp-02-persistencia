from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime, date


class Evento(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nome: str = Field(..., max_length=150)
    data_inicio: date
    data_termino: date
    local: str = Field(..., max_length=200)
    descricao: str = Field(..., max_length=500)

    # Relacionamento com Sessão e Inscrição
    sessoes: List["Sessao"] = Relationship(back_populates="evento")
    inscricoes: List["Inscricao"] = Relationship(back_populates="evento")


class Participante(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nome: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100, unique=True)
    instituicao: str = Field(..., max_length=150)

    # Relacionamento com Inscrição
    inscricoes: List["Inscricao"] = Relationship(back_populates="participante")


class Palestrante(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nome: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100, unique=True)
    biografia: str = Field(..., max_length=500)

    # Relacionamento com Sessão
    sessoes: List["Sessao"] = Relationship(back_populates="palestrante")


class Sessao(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nome: str = Field(..., max_length=150)
    data_hora: datetime
    evento_id: UUID = Field(foreign_key="evento.id")
    palestrante_id: UUID = Field(foreign_key="palestrante.id")

    # Relacionamentos
    evento: Optional[Evento] = Relationship(back_populates="sessoes")
    palestrante: Optional[Palestrante] = Relationship(back_populates="sessoes")


class Inscricao(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    evento_id: UUID = Field(foreign_key="evento.id")
    participante_id: UUID = Field(foreign_key="participante.id")

    # Relacionamentos
    evento: Optional[Evento] = Relationship(back_populates="inscricoes")
    participante: Optional[Participante] = Relationship(back_populates="inscricoes")