# fastapi_authentication

### Project setup

1. Install `python3.9`
2. Create a top level directory `mkdir fastapi_workspace` and navigate to that directory `cd fastapi_workspace`
3. Make sure the current working directory is `fastapi_workspace`
4. Create a virtual environment. Run `python3.9 -m venv env`
5. Activate the virtual env. Run `source env/bin/activate`
6. Make sure you are in `fastapi_workspace` directory. Clone the project from github. Run `git clone https://github.com/RohitKKansal/fastapi_authentication.git`
7. Navigate to the project directory. Run `cd fastapi_authentication/`
8. Run `pip3 install --upgrade pip3 && pip3 install -r requirements.txt`
9. Run `python main.py`. You can see the project on your browser at `0.0.0.0:8000`

### FastAPI Setup From Scratch

1. Create a top lavel directory `mkdir fastapi_project` and navigate to that directory `cd fastapi_project`
2. Create a environment with Python latest version. Run `python3.10 -m venv env`
3. Activate the virtual env. Run `source env/bin/activate`
4. Make sure you are in `fastapi_workspace` directory. Create a new file. Run `touch main.py`
5. Open the directory `fastapi_workspace` in your favorite integrated development environment (IDE). If you open the directory in visual studio code then Run `code ./`
6. Open the `main.py` file in visual studio code then write the code:-
    1. Import the FastAPI in the `main.py` file
    2. ```from fastapi import FastAPI
        import uvicorn
        
        app = FastAPI()

        @app.get('/')
        def index_view():
            return "It's working!"
            
        if __name__ == "__main__":
            uvicorn.run(app, host="0.0.0.0", port=8000)```
    3. Run `python main.py`.
    4. You can see the project on your browser at `0.0.0.0:8000`

### Setup on ubuntu(Linux)
```
git clone git@github.com:RohitKKansal/fastapi_authentication.git
cd fastapi_authentication
python3.8 -m venv env
source env/bin/active
pip install --upgrade pip && pip install -r requirements.txt
uvicorn main:app --reload
```

### Create migrations
```
https://alembic.sqlalchemy.org/en/latest/tutorial.html#running-our-first-migration
```