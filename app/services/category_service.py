from sqlalchemy.orm import Session

from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


class CategoryService:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category: CategoryCreate) -> Category:
        db_category = Category(**category.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get_category(self, category_id: int) -> Category | None:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_categories(self, skip: int = 0, limit: int = 100) -> list[Category]:
        return self.db.query(Category).offset(skip).limit(limit).all()

    def update_category(
        self, category_id: int, category: CategoryUpdate
    ) -> Category | None:
        db_category = self.get_category(category_id)
        if not db_category:
            return None

        update_data = category.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_category, key, value)

        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def delete_category(self, category_id: int) -> bool:
        db_category = self.get_category(category_id)
        if db_category:
            self.db.delete(db_category)
            self.db.commit()
            return True
        return False
