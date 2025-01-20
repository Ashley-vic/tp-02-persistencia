from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from Database.Database import get_session
from Database.Models import Evento
from uuid import UUID, uuid4


router = APIRouter()


@router.post("/", response_model=Evento)
def criar_evento(evento: Evento, session: Session = Depends(get_session)):
    print(evento)
    try:
        evento.data_inicio = datetime.strptime(evento.data_inicio, '%Y-%m-%d').date()
        evento.data_termino = datetime.strptime(evento.data_termino, '%Y-%m-%d').date()
        session.add(evento)
        session.commit()
        session.refresh(evento)
        return evento
    except Exception as e:
        print(f"Erro ao criar evento: {e}")
        session.rollback()
        raise

@router.get("/", response_model=list[Evento])
def listar_eventos(session: Session = Depends(get_session), limit: int = 10, offset: int = 0):
    query = select(Evento).offset(offset).limit(limit)
    eventos = session.exec(query).all()
    return eventos


@router.get("/{evento_id}", response_model=Evento)
def obter_evento(evento_id: UUID, session: Session = Depends(get_session)):
    evento = session.get(Evento, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    return evento


@router.put("/{evento_id}", response_model=Evento)
def atualizar_evento(evento_id: UUID, evento: Evento, session: Session = Depends(get_session)):
    db_evento = session.get(Evento, evento_id)
    if not db_evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    for key, value in evento.dict(exclude_unset=True).items():
        setattr(db_evento, key, value)
    session.add(db_evento)
    session.commit()
    session.refresh(db_evento)
    return db_evento


@router.delete("/{evento_id}")
def deletar_evento(evento_id: UUID, session: Session = Depends(get_session)):
    evento = session.get(Evento, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")
    session.delete(evento)
    session.commit()
    return {"message": "Evento deletado com sucesso"}
