from sqlalchemy import Column, INT, VARCHAR, ForeignKey, \
    DECIMAL, BOOLEAN, select, BIGINT
from sqlalchemy.orm import declarative_base, sessionmaker, declarative_mixin
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

Base = declarative_base()


@declarative_mixin
class BaseMixin(object):
    id = Column(INT, primary_key=True)

    engine = create_async_engine('postgresql+asyncpg://belhard:belhard@0.0.0.0:5432/bh35d')
    _Session = sessionmaker(bind=engine, class_=AsyncSession)

    @staticmethod
    def create_session(func):
        async def wrapper(*args, **kwargs):
            async with BaseMixin._Session() as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    async def save(self, session: AsyncSession = None) -> None:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_session
    async def get(cls, pk, session: AsyncSession = None) -> Base | None:
        return await session.get(cls, pk)

    @classmethod
    @create_session
    async def all(cls, order_by: str = 'id', session: AsyncSession = None, **kwargs) -> list[Base]:
        query = await session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .order_by(order_by)
        )
        return query.all()

    @create_session
    async def delete(self, session: AsyncSession = None):
        await session.delete(self)
        await session.commit()


class Category(BaseMixin, Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(64), nullable=False, unique=True)

    def __str__(self):
        return self.name


class Product(BaseMixin, Base):
    __tablename__ = 'products'

    name = Column(VARCHAR(64), nullable=False)
    price = Column(DECIMAL(8, 2), default=1)
    is_published = Column(BOOLEAN, default=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

    def __str__(self):
        return self.name


class User(BaseMixin, Base):
    __tablename__ = 'users'

    id = Column(BIGINT, primary_key=True)
    email = Column(VARCHAR(32), nullable=False, unique=True)
    name = Column(VARCHAR(32), nullable=False)

    def __str__(self):
        return self.email
