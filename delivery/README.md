# Delivery app

## First steps to start developing

1. Create a virtual env (venv)
```
python -m venv .venv
```
2. Activate venv
```
.\.venv\Scripts\activate
```
3. Install package
    - Development
    ```
    pip install -e . ['dev']
    ```
    - Prod
    ```
    pip install delivery
    ```
    
4. Setting environment variables
    - Linux
    ```
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```
    - Windows
    ```
    $env:FLASK_APP = "app.py"
    $env:FLASK_ENV = "development"
    ```
5. Running server
```
flask run
```

<br>
---

## Back-end (Flask)
|Endpoint|Method|
|---|---|
|/home|GET|
|/register|POST|
|/login|GET|
|/api/user/{id}|GET|
|/api/user/{id}|POST|
|/api/user/{id}|PUT|
|/api/product/{id}|GET|
|/api/product/{id}|POST|
|/api/product/{id}|PUT|
|/api/product/{id}|DELETE|
|/api/category/{id}|GET|
|/api/category/{id}|POST|
|/api/category/{id}|PUT|
|/api/restaurant/{id}|GET|
|/api/restaurant/{id}|POST|
|/api/restaurant/{id}|PUT|
|/api/restaurant/{id}|DELETE|
|/api/order/{id}|GET|
|/api/order/{id}|POST|

---

## Front-end (Vuejs)
