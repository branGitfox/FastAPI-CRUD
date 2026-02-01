from sqlalchemy import create_engine
from sqlalchemy.orm import create_session

db_url = 'mysql+pymysql://root@localhost:3306/shop_api'
engine = create_engine(db_url)
session = create_session(engine, autoflush=False, autocommit=False)
