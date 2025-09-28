# setup_database.py

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco
DATABASE_URL = "sqlite:///banco.db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definir a tabela de hotéis
class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    price_per_night = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)  # de 1 a 5
    availability = Column(Integer, nullable=False)  # número de quartos disponíveis

# Criar tabelas
Base.metadata.create_all(engine)

# Dados de exemplo
hotels_data = [
    {"name": "Hotel Plaza", "city": "Paris", "price_per_night": 95.0, "rating": 4.5, "availability": 12},
    {"name": "Le Petit Paris", "city": "Paris", "price_per_night": 78.0, "rating": 4.2, "availability": 8},
    {"name": "Grand Palace", "city": "Paris", "price_per_night": 120.0, "rating": 4.8, "availability": 5},
    {"name": "Chic Boutique", "city": "Paris", "price_per_night": 85.0, "rating": 4.3, "availability": 15},
    {"name": "Riviera Resort", "city": "Nice", "price_per_night": 110.0, "rating": 4.6, "availability": 7},
    {"name": "Sunset Beach", "city": "Nice", "price_per_night": 90.0, "rating": 4.1, "availability": 10},
    {"name": "Mountain Lodge", "city": "Lyon", "price_per_night": 80.0, "rating": 4.0, "availability": 6},
    {"name": "City Center Inn", "city": "Lyon", "price_per_night": 65.0, "rating": 3.9, "availability": 20},
]

# Inserir dados
Session = sessionmaker(bind=engine)
session = Session()

for hotel_data in hotels_data:
    hotel = Hotel(**hotel_data)
    session.add(hotel)

session.commit()
session.close()

print("Banco de dados criado com sucesso!")
print("Arquivo: banco.db")