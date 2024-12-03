from src.database.sql_alchamy import db


class ItemModel:
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
