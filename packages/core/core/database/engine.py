from sqlalchemy import create_engine

connection_string = "sqlite:///db.sqlite3"

engine = create_engine(connection_string, echo=False)
