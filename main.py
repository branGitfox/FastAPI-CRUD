from fastapi import FastAPI
from database import session, engine
from database_models import Base
app = FastAPI()

Base.metadata.create_all(bind=engine)
# fetching all products
@app.get('/products')
def get_products():
    return 'hello world'
