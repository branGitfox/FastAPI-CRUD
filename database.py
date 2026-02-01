from sqlalchemy import create_engine
from sqlalchemy.orm import create_session, sessionmaker

db_url = 'mysql+pymysql://root@localhost:3306/shop_api'
engine = create_engine(db_url)
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
