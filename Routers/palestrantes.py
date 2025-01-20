from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from Database.Database import get_session
from Database.Models import Palestrante

router = APIRouter()


@router.post("/", response_model=Palestrante)
def criar_palestrante(palestrante: Palestrante, session: Session = Depends(get_session)):
    session.add(palestrante)
    session.commit()
    session.refresh(palestrante)
    return palestrante


@router.get("/", response_model=list[Palestrante])
def listar_palestrantes(session: Session = Depends(get_session), limit: int = 10, offset: int = 0):
    query = select(Palestrante).offset(offset).limit(limit)
    palestrantes = session.exec(query).all()
    return palestrantes


@router.get("/{palestrante_id}", response_model=Palestrante)
def obter_palestrante(palestrante_id: int, session: Session = Depends(get_session)):
    palestrante = session.get(Palestrante, palestrante_id)
    if not palestrante:
        raise HTTPException(status_code=404, detail="Palestrante não encontrado")
    return palestrante


@router.put("/{palestrante_id}", response_model=Palestrante)
def atualizar_palestrante(palestrante_id: int, palestrante: Palestrante, session: Session = Depends(get_session)):
    db_palestrante = session.get(Palestrante, palestrante_id)
    if not db_palestrante:
        raise HTTPException(status_code=404, detail="Palestrante não encontrado")
    for key, value in palestrante.dict(exclude_unset=True).items():
        setattr(db_palestrante, key, value)
    session.add(db_palestrante)
    session.commit()
    session.refresh(db_palestrante)
    return db_palestrante


@router.delete("/{palestrante_id}")
def deletar_palestrante(palestrante_id: int, session: Session = Depends(get_session)):
    palestrante = session.get(Palestrante, palestrante_id)
    if not palestrante:
        raise HTTPException(status_code=404, detail="Palestrante não encontrado")
    session.delete(palestrante)
    session.commit()
    return {"message": "Palestrante deletado com sucesso"}
