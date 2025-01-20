from fastapi import FastAPI
from Database.Database import create_db_and_tables
from Routers import eventos, participantes, palestrantes, sessoes, inscricao

app = FastAPI()

app.include_router(eventos.router, prefix="/eventos", tags=["eventos"])
app.include_router(participantes.router, prefix="/participantes", tags=["participantes"])
app.include_router(palestrantes.router, prefix="/palestrantes", tags=["palestrantes"])
app.include_router(sessoes.router, prefix="/sessoes", tags=["sessoes"])
app.include_router(inscricao.router, prefix="/inscricoes", tags=["inscricoes"])
@app.on_event("startup")
async def startup():
    print("Starting the app...")
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Hello from tp-02-persistencia!"}