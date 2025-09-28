# init_db.py

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from setup_database import Hotel, hotels_data

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///banco.db")
engine = create_engine(DATABASE_URL)

# Importar modelos e criar tabelas
from setup_database import Base
Base.metadata.create_all(engine)

# Inserir dados
Session = sessionmaker(bind=engine)
session = Session()

# Limpar dados antigos
session.execute(Hotel.__table__.delete())
session.commit()

# Inserir novos dados
for hotel_data in hotels_data:
    hotel = Hotel(**hotel_data)
    session.add(hotel)

session.commit()
session.close()

print("Banco inicializado com dados de exemplo.")