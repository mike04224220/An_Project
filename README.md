E-commerce
===========

Welcome to the my world, Neexxus Project! This Django application is designed to manage different kinds of products, orders, and users efficiently.

Requirements
------------

*   **PostgreSQL** (Make sure it's installed and running)
*   **Python 3.12.4**

Installation Guide
------------------

Follow these steps to get the project up and running on your local machine.

### 1\. Clone the Repository

Clone the project repository from GitHub to your local machine.

```bash
git clone https://github.com/mike04224220/E-commerce.git nexxus
cd nexxus
```

### 2\. Set Up Virtual Environment

Create and activate a virtual environment.


```bash
Option 1:
    pip install virtualenv
    virtualenv my_virtual_env
Option 2:
    python3.12.4 -m venv my_virtual_env

Activate:
    CDM: source venv/bin/activate 
    PowerShell: .\my_virtaul_env\Scripts\Activate
    Bash: source .my_virtaul_env/Scripts/activate
    Linux: source bin/activate
```

### 3\. Install Dependencies

Install the required Python packages using `pip`.

`pip install -r requirements.txt`

### 4\. Configure Environment Variables

Create a `.env` file in the root of the project. You can use `.env.example` as a template.


`cp .env.example .env`

Update the `.env` file with your database credentials and other necessary configurations.

### 5\. Set Up the Database

Create the PostgreSQL database and apply migrations.

```bash
psql -U postgres CREATE DATABASE DBnexxus;
```
Apply migrations 

```bash
python manage.py migrate
```

### 6\. Create a Superuser

Create a superuser to access the Django admin interface.


```
python manage.py createsuperuser
```

### 7\. Run the Development Server

Start the Django development server.

```
./manage.py runserver
```

Access the project by navigating to `http://127.0.0.1:8000` in your web browser.

Project Structure
-----------------

*   **index**: Show each data about us, Nexxus.
*   **products**: Handles everything related to coffee products.
*   **users**: Manages user authentication and profiles.
*   **orders**: Manages customer orders.

Contributing
------------

We welcome contributions! Please fork the repository and submit pull requests for any features, improvements, or bug fixes.