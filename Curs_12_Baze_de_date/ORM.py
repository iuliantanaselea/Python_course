# ORM -> Object Relational Maping
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# conectare la db
engine = create_engine('sqlite:///users.db')

# creare tabele
Base.metadata.create_all(engine)

# pornire sesiune
Session = sessionmaker(bind=engine)
session = Session()

# adaugare
u = User(name='Andrei', age=29)
u2 = User(name='Andreea', age=30)

session.add(u)
session.add(u2)
session.commit()
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)

user = session.query(User).filter_by(name='Andrei').first()
session.delete(user)
session.commit()
