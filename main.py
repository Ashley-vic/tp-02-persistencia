from fastapi import FastAPI
from Database.Database import create_db_and_tables  # Assuming this is a function to create tables
from Routers import eventos, participantes, palestrantes, sessoes  # Importing the routers

app = FastAPI()

app.include_router(eventos.router)
app.include_router(participantes.router)
app.include_router(palestrantes.router)
app.include_router(sessoes.router)

@app.on_event("startup")
async def startup():
    print("Starting the app...")
    create_db_and_tables()  
@app.get("/")
def read_root():
    return {"message": "Hello from tp-02-persistencia!"}
