from typing import Any, BinaryIO, Dict, List
import pandas as pd
from pydantic import FilePath
from sqlalchemy.orm import Session
from app.models.asset_movement import AssetMovement as Asset
from app.models.category import Category
from datetime import datetime
from io import BytesIO


class ExcelManager:
    @staticmethod
    def export_to_excel(db: Session):
        # Получаем данные из БД
        assets = db.query(Asset).all()
        categories = db.query(Category).all()

        # Преобразуем в DataFrame
        assets_data: List[Dict[str, Any]] = [
            {
                "ID": a.id,
                "Наименование": a.name,
                "Инвентарный номер": a.inventory_number,
                "Категория": a.category.name if a.category else None,
                "Стоимость": a.cost,
                "Дата приобретения": a.purchase_date,
                "Местоположение": a.location,
                "Статус": a.status,
            }
            for a in assets
        ]

        categories_data: List[Dict[str, Any]] = [
            {"ID": c.id, "Название": c.name, "Описание": c.description}
            for c in categories
        ]

        # Создаем Excel файл в памяти
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            pd.DataFrame(assets_data).to_excel(
                writer, sheet_name="Основные средства", index=False
            )
            pd.DataFrame(categories_data).to_excel(
                writer, sheet_name="Категории", index=False
            )

        output.seek(0)
        return output

    @staticmethod
    def import_from_excel(db: Session, file: str | FilePath | BinaryIO):
        # Читаем Excel файл
        xls = pd.ExcelFile(file)
        for element in xls.sheet_names:
            match element:
                case "Категории":
                    categories_df = pd.read_excel(xls, sheet_name="Категории")
                    for _, row in categories_df.iterrows():
                        if (
                            not db.query(Category)
                            .filter(Category.id == row["ID"])
                            .first()
                        ):
                            category = Category(
                                id=row["ID"],
                                name=row["Название"],
                                description=row.get("Описание"),
                            )
                            db.add(category)
                    db.commit()

                # Обрабатываем лист с активами
                case "Основные средства":
                    assets_df = pd.read_excel(xls, sheet_name="Основные средства")
                    for _, row in assets_df.iterrows():
                        if not db.query(Asset).filter(Asset.id == row["ID"]).first():
                            # Преобразуем дату из строки в объект datetime
                            purchase_date = row["Дата приобретения"]
                            if isinstance(purchase_date, str):
                                purchase_date = datetime.strptime(
                                    purchase_date, "%Y-%m-%d"
                                ).date()

                            asset = Asset(
                                id=row["ID"],
                                name=row["Наименование"],
                                inventory_number=row["Инвентарный номер"],
                                category_id=row["Категория"],
                                cost=row["Стоимость"],
                                purchase_date=purchase_date,
                                location=row.get("Местоположение"),
                                status=row.get("Статус", "active"),
                            )
                            db.add(asset)
                case _:
                    pass
        db.commit()
