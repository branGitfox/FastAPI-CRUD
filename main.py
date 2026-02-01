from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session
from database import session, engine
from database_models import Base
import database_models
from models import Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

# umm a mock data to push into the db cause don't want to create it manualy
products = [
    Product(id=1, name="Gun", description="M416 from pubg mobile", price=10.7),
    Product(id=2, name="Knife", description="Knife from pubg mobile", price=9.7)
]
def init_db():
    db = session()
    count = db.query(database_models.Product).count()
    if count == 0 :
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()

# a singleton db getter for dependecy injection
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

# fetching all products
@app.get('/products')
def get_products(db: Session = Depends(get_db)):
    if db.query(database_models.Product).count() == 0:
        return {'message': 'No product found'}
    else:
        datas = db.query(database_models.Product).all()
        return datas
