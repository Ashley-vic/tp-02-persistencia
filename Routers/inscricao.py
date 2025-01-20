from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from Database.Database import get_session
from Database.Models import Inscricao

router = APIRouter()


@router.post("/", response_model=Inscricao)
def criar_inscricao(inscricao: Inscricao, session: Session = Depends(get_session)):
    session.add(inscricao)
    session.commit()
    session.refresh(inscricao)
    return inscricao


@router.get("/", response_model=list[Inscricao])
def listar_inscricoes(session: Session = Depends(get_session), limit: int = 10, offset: int = 0):
    query = select(Inscricao).offset(offset).limit(limit)
    inscricoes = session.exec(query).all()
    return inscricoes


@router.get("/{inscricao_id}", response_model=Inscricao)
def obter_inscricao(inscricao_id: int, session: Session = Depends(get_session)):
    inscricao = session.get(Inscricao, inscricao_id)
    if not inscricao:
        raise HTTPException(status_code=404, detail="Inscricao não encontrada")
    return inscricao


@router.put("/{inscricao_id}", response_model=Inscricao)
def atualizar_inscricao(inscricao_id: int, inscricao: Inscricao, session: Session = Depends(get_session)):
    db_inscricao = session.get(Inscricao, inscricao_id)
    if not db_inscricao:
        raise HTTPException(status_code=404, detail="Inscricao não encontrada")
    for key, value in inscricao.dict(exclude_unset=True).items():
        setattr(db_inscricao, key, value)
    session.add(db_inscricao)
    session.commit()
    session.refresh(db_inscricao)
    return db_inscricao


@router.delete("/{inscricao_id}")
def deletar_inscricao(inscricao_id: int, session: Session = Depends(get_session)):
    inscricao = session.get(Inscricao, inscricao_id)
    if not inscricao:
        raise HTTPException(status_code=404, detail="Inscricao não encontrada")
    session.delete(inscricao)
    session.commit()
    return {"message": "Inscricao deletada com sucesso"}