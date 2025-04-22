from fastapi import FastAPI

from app.api.categories import router as categories_router
from app.api.assets import router as assets_router
from app.api.department import router as departments_router
from app.db.database import Base, engine
from app.api.excel import router as excel_router

app = FastAPI(docs_url="/")

Base.metadata.create_all(bind=engine)

app.include_router(assets_router, prefix="/api/assets")
app.include_router(categories_router, prefix="/api/categories")
app.include_router(departments_router, prefix="/api/departments")
app.include_router(excel_router)


