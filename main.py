from fastapi import FastAPI
from database import session, engine
from database_models import Base
import database_models
from models import Product

app = FastAPI()

Base.metadata.create_all(bind=engine)

# umm a mock data to push into the db cause don't want to create it manualy
products = [
    Product(id=1, name="Gun", description="M416 from pubg mobile", price=10.7)
]
def init_db():
    db = session()
    for product in products:
        db.add(database_models.Product(**product.model_dump()))
    db.commit()


# fetching all products
@app.get('/products')
def get_products():
    return 'hello world'
