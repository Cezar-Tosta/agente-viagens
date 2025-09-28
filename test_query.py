from sqlalchemy import create_engine, text

# Conectar ao banco
DATABASE_URL = "sqlite:///banco.db"
engine = create_engine(DATABASE_URL)

# Consulta desejada
query = """
SELECT * FROM hotels 
WHERE rating > 4.5 
ORDER BY price_per_night 
ASC;
"""

with engine.connect() as connection:
    result = connection.execute(text(query))
    rows = result.fetchall()
    columns = list(result.keys())

    print("Resultado da consulta:")
    print(", ".join(columns))
    for row in rows:
        print(", ".join(str(cell) for cell in row))