# Endpoints para "Sessoes"
from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from sqlmodel import Session, select
from Database.Database import get_session
from Database.Models import Sessao
from uuid import UUID, uuid4


router = APIRouter()


@router.post("/", response_model=Sessao)
def criar_sessao(sessao: Sessao, session: Session = Depends(get_session)):
    try:
        sessao.data_hora = datetime.fromisoformat(sessao.data_hora.replace('Z', '+00:00'))
        sessao.evento_id = UUID(sessao.evento_id)
        sessao.palestrante_id = UUID(sessao.palestrante_id)
        session.add(sessao)
        session.commit()
        session.refresh(sessao)
        return sessao
    except Exception as e:
        print(f"Erro ao criar sessão: {e}")
        session.rollback()
        raise

@router.get("/", response_model=list[Sessao])
def listar_sessoes(session: Session = Depends(get_session), limit: int = 10, offset: int = 0):
    query = select(Sessao).offset(offset).limit(limit)
    sessoes = session.exec(query).all()
    return sessoes


@router.get("/{sessao_id}", response_model=Sessao)
def obter_sessao(sessao_id: UUID, session: Session = Depends(get_session)):
    sessao = session.get(Sessao, sessao_id)
    if not sessao:
        raise HTTPException(status_code=404, detail="Sessao não encontrada")
    return sessao


@router.put("/{sessao_id}", response_model=Sessao)
def atualizar_sessao(sessao_id: UUID, sessao: Sessao, session: Session = Depends(get_session)):
    db_sessao = session.get(Sessao, sessao_id)
    if not db_sessao:
        raise HTTPException(status_code=404, detail="Sessao não encontrada")
    for key, value in sessao.dict(exclude_unset=True).items():
        setattr(db_sessao, key, value)
    session.add(db_sessao)
    session.commit()
    session.refresh(db_sessao)
    return db_sessao


@router.delete("/{sessao_id}")
def deletar_sessao(sessao_id: UUID, session: Session = Depends(get_session)):
    sessao = session.get(Sessao, sessao_id)
    if not sessao:
        raise HTTPException(status_code=404, detail="Sessao não encontrada")
    session.delete(sessao)
    session.commit()
    return {"message": "Sessao deletada com sucesso"}