# fastapi_authentication

### Project setup

1. Install `python3.9`
2. Create a top level directory `mkdir fastapi_workspace` and navigate to that directory `mkdir fastapi_workspace`
3. Make sure the current working directory is `fastapi_workspace`
4. Create a virtual environment. Run `python3.9 -m venv env`
5. Activate the virtual env. Run `source env/bin/activate`
6. Make sure you are in `fastapi_workspace` directory. Clone the project from github. Run `git clone https://github.com/RohitKKansal/fastapi_authentication.git`
7. Navigate to the project directory. Run `cd fastapi_authentication/`
8. Run `pip3 install --upgrade pip3 && pip3 install -r requirements.txt`
9. Run `python main.py`. You can see the project on your browser at `0.0.0.0:8000`

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