
# Setting Up Your Virtual Environment

1. **Create a Virtual Environment**: Start by creating a virtual environment tailored to your device with the following command:

   ```shell
   python -m venv env
   ```

2. **Activate Your Virtual Environment**: Activate the virtual environment using this command:

   ```shell
   env/Scripts/Activate
   ```

3. **Navigate to Your Project Directory**: Change your current directory to the location of your project.

4. **Install Dependencies**: Install the necessary dependencies from `requirements.txt` using pip:

   ```shell
   pip install -r requirements.txt
   ```

5. **Run Your Django Server**: Once all dependencies are installed successfully, start your Django server:

   ```shell
   python manage.py runserver
   ```

## Working with Endpoints

### List Products

To view a list of products, access the following URL:

[http://localhost:8000/api/products/](http://localhost:8000/api/products/)

### User Login

To log in as a user, use this URL:

[http://localhost:8000/auth/login/](http://localhost:8000/auth/login/)

Use the following credentials:

- **Username:** b
- **Password:** beno

### View a Single Product

To retrieve details about a single product, use the following URL:

[http://localhost:8000/api/products/1/](http://localhost:8000/api/products/1/)


### update A Product user PATCH Or PUT

To Update a single product, use the following URL With Patch OR Put Method:

[http://localhost:8000/api/products/1/](http://localhost:8000/api/products/1/)


### Delete  A Product use DELETE method

To Delete a single product, use the following URL with the DELETE Method:


[http://localhost:8000/api/products/1/](http://localhost:8000/api/products/1/)


###  I have added Filtering for the Products Based on name , price , and in stock_quantity

[http://localhost:8000/api/products/?price=100](http://localhost:8000/api/products/?price=100)


###  I have added Filtering for the Products Based on in stock_quantity
[http://localhost:8000/api/products/?stock_quantity=100](http://localhost:8000/api/products/?stock_quantity=100)


### I have added Filtering for the Products Based on name
[http://localhost:8000/api/products/?name=product%201](http://localhost:8000/api/products/?name=product%201)
