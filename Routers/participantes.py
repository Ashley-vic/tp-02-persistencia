from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from Database.Database import get_session
from Database.Models import Participante

router = APIRouter()


@router.post("/", response_model=Participante)
def criar_participante(participante: Participante, session: Session = Depends(get_session)):
    session.add(participante)
    session.commit()
    session.refresh(participante)
    return participante


@router.get("/", response_model=list[Participante])
def listar_participantes(session: Session = Depends(get_session), limit: int = 10, offset: int = 0):
    query = select(Participante).offset(offset).limit(limit)
    participantes = session.exec(query).all()
    return participantes


@router.get("/{participante_id}", response_model=Participante)
def obter_participante(participante_id: int, session: Session = Depends(get_session)):
    participante = session.get(Participante, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante não encontrado")
    return participante


@router.put("/{participante_id}", response_model=Participante)
def atualizar_participante(participante_id: int, participante: Participante, session: Session = Depends(get_session)):
    db_participante = session.get(Participante, participante_id)
    if not db_participante:
        raise HTTPException(status_code=404, detail="Participante não encontrado")
    for key, value in participante.dict(exclude_unset=True).items():
        setattr(db_participante, key, value)
    session.add(db_participante)
    session.commit()
    session.refresh(db_participante)
    return db_participante


@router.delete("/{participante_id}")
def deletar_participante(participante_id: int, session: Session = Depends(get_session)):
    participante = session.get(Participante, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante não encontrado")
    session.delete(participante)
    session.commit()
    return {"message": "Participante deletado com sucesso"}