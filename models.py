from sqlalchemy import Column, INT, VARCHAR, ForeignKey, DECIMAL, BOOLEAN, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

class BaseMixin():
    id = Column(INT, primary_key=True)
    engine = create_engine('postgresql://operator:operator@localhost:5432/test')
    Session = sessionmaker(bind=engine)

    @classmethod
    def save(self) -> None:
        with self.

