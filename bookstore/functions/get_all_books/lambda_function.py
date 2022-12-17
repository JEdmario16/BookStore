from libs.common import get_books_collection

def lambda_handler(event, context):

    # Get the books collection
    books_collection = get_books_collection()

    # Get all the books
    books = books_collection.find()
    
    # Convert the books to a list
