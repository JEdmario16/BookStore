from chalice import Chalice

app = Chalice(app_name='bookstore-products')


@app.route("/get_products")
def get_products():
    """
    Collect all products from mongo database and return them as a json object.
    """