# Endpoints para "Sessoes"
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from Database.Database import get_session
from Database.Models import Sessao

router = APIRouter()


@router.post("/", response_model=Sessao)
def criar_sessao(sessao: Sessao, session: Session = Depends(get_session)):
    session.add(sessao)
    session.commit()
    session.refresh(sessao)
    return sessao


@router.get("/", response_model=list[Sessao])
def listar_sessoes(session: Session = Depends(get_session), limit: int = 10, offset: int = 0):
    query = select(Sessao).offset(offset).limit(limit)
    sessoes = session.exec(query).all()
    return sessoes


@router.get("/{sessao_id}", response_model=Sessao)
def obter_sessao(sessao_id: int, session: Session = Depends(get_session)):
    sessao = session.get(Sessao, sessao_id)
    if not sessao:
        raise HTTPException(status_code=404, detail="Sessao não encontrada")
    return sessao


@router.put("/{sessao_id}", response_model=Sessao)
def atualizar_sessao(sessao_id: int, sessao: Sessao, session: Session = Depends(get_session)):
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
def deletar_sessao(sessao_id: int, session: Session = Depends(get_session)):
    sessao = session.get(Sessao, sessao_id)
    if not sessao:
        raise HTTPException(status_code=404, detail="Sessao não encontrada")
    session.delete(sessao)
    session.commit()
    return {"message": "Sessao deletada com sucesso"}