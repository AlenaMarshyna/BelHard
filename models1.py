from sqlalchemy import Column, INT, VARCHAR, ForeignKey, DECIMAL, BOOLEAN, create_engine, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker



Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Base):
    __tablename__ = 'products'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(64), nullable=False)
    price = Column(DECIMAL(8, 2), default=0.0)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Status(Base):
    __tablename__ = 'statuses'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(10), nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(INT, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False)


class Oder(Base):
    __tablename__ = 'orders'

    id = Column(INT, primary_key=True)
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)


class Order_item(Base):
    __tablename__ = 'order_items'

    id = Column(INT, primary_key=True)
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)

engine = create_engine('postgresql://operator:operator@localhost:5432/test')
Session = sessionmaker(bind=engine)


# from csv import DictReader
#
# with open('category.csv', 'r', encoding='utf-8') as file:
#     reader = DictReader(file)
#
#     with Session() as session:
#         for category in reader:
#             cat = Category(**category)
#             session.add(cat)
#             try:
#                 session.commit()
#             except IntegrityError:
#                 session.rollback()
#
# with open('products.csv', 'r', encoding='utf-8') as file:
#     reader = DictReader(file)
#
#     with Session() as session:
#         for product in reader:
#             prod = Product(**product)
#             session.add(prod)
#             try:
#                 session.commit()
#             except IntegrityError:
#                 session.rollback()

with Session() as session:
    query = session.scalars(
        select(Category)
        .filter(Category.id > 1)
        .order_by('name')
    )
    query = query.all()

