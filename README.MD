This is the inventory management system having functionalities lie customer add customer details fetch and adding products or fecthing products 

## the superuser id and password are vaibhav 

the url patter requested to be use to send any request or check an api 
is 
http://127.0.0.1:8000/inventory/{desired url fron inventory.url}


please ensure that you check url from inventory.urls.py before using

## for any query : reach out at 

vishuchauhan461@gmail.com


## Here is the document which can help you to test these api on swagger. remember always follow the url pattern correctly and all the example of data provide are raw json .

1.Getting Started:<br>
Make sure your Inventory Management System is running on your local machine at http://127.0.0.1:8000/.


2.Checking Endpoints:<br>
Go to the API page at http://127.0.0.1:8000/inventory/ to see what you can do.


3.Trying out Products:<br>
Want to see what products are available? Hit http://127.0.0.1:8000/inventory/products/ to see the list.<br>
Want to add a new product? Send a POST request to the same URL with details like name, price, etc.
example : {
    "name": "wheat",
    "price": 29.99,
    "quantity": 100,
    "description": "A grain used as food "
}


4.Exploring Product Details:<br>
To see details of a specific product, go to http://127.0.0.1:8000/inventory/products/{product_id}/.<br>
Want to update the details? Send a PUT request with new details.<br>
Want to get rid of a product? Send a DELETE request.<br>

5.Checking Customers:<br>
Curious about your customers? Visit http://127.0.0.1:8000/inventory/customers/ to see them.<br>
If you want to add a new customer, send a POST request here.<br>

6.Customer Details:<br>
To see details of a particular customer, go to http://127.0.0.1:8000/inventory/customers/{customer_id}/.<br>
Need to update customer details? Send a PUT request.<br>
example: {
    "name": "John",
    "email": "john@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, GZB, India"
}
Want to remove a customer? Send a DELETE request.

7.Creating Bills:<br>
Ready to create a bill? Send a POST request to http://127.0.0.1:8000/inventory/bill/ with bill details.<br>
examnple : {
    "customer_id": 1,
    "products": [
        {
            "product_id": 2,
            "quantity": 3
        },
        {
            "product_id": 5,
            "quantity": 1
        }
    ],
    "total_amount": 129.95
}


8.Checking Responses:<br>
After each action, take a look at the responses you get back.<br>
Make sure they contain what you expected and have the right status codes (like 200 for success or 404 for not found).<br>