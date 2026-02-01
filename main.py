from fastapi import FastAPI
from database import session

app = FastAPI()


# fetching all products
@app.get('/products')
def get_products():
    return 'hello world'
