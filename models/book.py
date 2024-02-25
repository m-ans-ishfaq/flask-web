from sqlalchemy import Column, Integer, String
from models.base import Base
from jsonschema import validate, ValidationError

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
    @staticmethod
    def validate_book_data(data):
        book_schema = {
            "type": "object",
            "properties": {
                "title": {"type": "string", "minLength": 1},
                "author": {"type": "string", "minLength": 1}
            },
            "required": ["title", "author"],
            "additionalProperties": False
        }
        try:
            validate(instance=data, schema=book_schema)
            return True
        except ValidationError as e:
            print(f"Error: {e}")
            return False