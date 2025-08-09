from fastapi import FastAPI
from src.backend.app.api.pci import router as pci_router

app = FastAPI()
app.include_router(pci_router)
