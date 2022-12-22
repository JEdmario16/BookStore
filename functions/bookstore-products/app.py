from chalice import Chalice

app = Chalice(app_name="bookstore-products")


@app.route("/")
def ping():
    return {"hll": "world"}
