from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from app.utils.excel_manager import ExcelManager
from app.db.database import get_db

router = APIRouter(prefix="/excel", tags=["excel"])


@router.get("/export")
async def export_to_excel(db: Session = Depends(get_db)):
    excel_file = ExcelManager.export_to_excel(db)
    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=assets_export.xlsx"},
    )


@router.post("/import")
async def import_from_excel(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    ExcelManager.import_from_excel(db, file.file)
    return {"message": "Данные успешно импортированы"}
