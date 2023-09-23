# django-rest-api
A REST api written in Django 

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. 
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone git@github.com:icurious/Inventory_Management.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd Inventory_Management
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```


    After the Django server is successfully up.
    Start the cli_app.py file to access REST API from CLI

    python cli_app.py

    (Choose the operation with Arrow and give necessary inputs)


    *** If Faced with Import Error for this File, related to collections module
    Change in this file - \[my_env]\lib\site-packages\prompt_toolkit\styles\from_dict.py
    from collections.abc import Mapping instead of from collections import Mapping

    This issue is seen in python 3.10