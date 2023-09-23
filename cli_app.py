

# A Cli Interface to Communicate with Django APP, Start Django Server and then run this app 

from PyInquirer import prompt
from examples import custom_style_2
from prompt_toolkit.validation import Validator, ValidationError
import requests


questions = [
    {
        'type': 'list',
        'name': 'user_option',
        'message': 'Welcome to Inventory Manager',
        'choices': [ "Display inventory", "Display sales", "Remove Product", "Add Product", "Update Stock", "Record Sale"]
    }

]

def display_products():
    url = 'http://127.0.0.1:8000/products/'
    r = requests.get(url)
    if r.status_code == 200:
        print(r.json())

def display_sales():
    url = 'http://127.0.0.1:8000/sales/'
    r = requests.get(url)
    if r.status_code == 200:
        print(r.json())

def remove_product(id):
    url = 'http://127.0.0.1:8000/products/' + str(id)
    r = requests.delete(url)
    if r.status_code == 204:
        print("Product with id: {} Successfuly Deleted".format(id))

def add_product(product_id,name,price,stock):
    url = 'http://127.0.0.1:8000/products/'
    json_obj = {"product_id":product_id,"name":name, "price":price, "stock":stock}
    r = requests.post(url,json = json_obj)
    if r.status_code == 201:
        print("Product Added Successfully")

def update_stock(product_id,stock):
    url = 'http://127.0.0.1:8000/products/' + str(product_id)+ '/'
    r = requests.get(url)
    json_obj = r.json()
    json_obj["stock"] = stock
    print(json_obj)
    r = requests.put(url,json = json_obj)
    print(r.status_code)
    if r.status_code == 200:
        print("Stock Updated Successfully")

def record_sale(transaction_id,product_id,quantity,total_amount):
    url = 'http://127.0.0.1:8000/sales/'
    json_obj = {"transaction_id":transaction_id,"product_id":product_id, "quantity":quantity, "total_amount":total_amount}
    r = requests.post(url,json = json_obj)
    print(r.status_code)
    if r.status_code == 201:
        print("Transaction Added Successfully")


def main():
    answers = prompt(questions, style=custom_style_2)
    if answers.get("user_option") == "Display inventory":
        display_products()
    elif answers.get("user_option") == "Display sales":
        display_sales()
    elif answers.get("user_option") == "Remove Product":
        id = int(input("Enter Product ID: "))
        remove_product(id)
    elif answers.get("user_option") == "Add Product":
        id = int(input("Enter Product ID: "))
        name = input("Enter Product name: ")
        price = int(input("Enter Product price: "))
        stock = int(input("Enter Stock: "))
        add_product(id,name,price,stock)
    elif answers.get("user_option") == "Update Stock":
        id = int(input("Enter Product ID: "))
        stock = int(input("Enter Stock: "))
        update_stock(id,stock)
    elif answers.get("user_option") == "Record Sale":
        transaction_id = int(input("Enter Transaction ID: "))
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))
        total_amount = int(input("Enter total Amount: "))
        record_sale(transaction_id,product_id,quantity,total_amount)

if __name__ == "__main__":
    main()
