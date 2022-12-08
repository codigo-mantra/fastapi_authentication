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
4. Make sure you are in `fastapi_project` directory. Create a new file. Run `touch main.py`
5. Open the directory `fastapi_project` in your favorite integrated development environment (IDE). If you open the directory in visual studio code then Run `code ./`
6. Open the `main.py` file in visual studio code then write the code:-
    1. Import the FastAPI in the `main.py` file
    2. ```
        from fastapi import FastAPI
        import uvicorn
        
        app = FastAPI()

        @app.get('/')
        def index_view():
            return "It's working!"
            
        if __name__ == "__main__":
            uvicorn.run(app, host="0.0.0.0", port=8000)
        ```
    3. Run `python main.py`.
    4. You can see the project on your browser at `0.0.0.0:8000`

7. Create a file for database connection :-
    1. Install package. Run `pip3 install sqlalchemy`
    2. Create a folder for connect database `mkdir settings` in this folder create a file `touch database.py`
    3. ```
        from sqlalchemy import create_engine
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy.orm import sessionmaker
        SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        ALGORITHM = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES = 30
        SQLALCHEMY_DATABASE_URL = "sqlite:///./twofactor_app.db"
        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
    ```

8. How to create models :-
    1. Create a model file `models.py` in current directory `fastapi_project`
    2. There are a few parts to make this work. The first part is to connect to the database:
    ```
        engine = create_engine(my_database_connection)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
    ```
    3. Then create models class For Example:
    ```
    from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
    from settings.database import Base

    class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True, index=True)
        email = Column(String, unique=True, index=True)
        first_name = Column(String)
        last_name = Column(String)
        hashed_password = Column(String)
        otp_secret = Column(String)
        disabled = Column(Boolean, default=False)
    ```
    4. `SQLAlchemy` is a Python SQL toolkit and ORM supporting database manipulation and management. `SQLAlchemy` provides users with an ORM using Data Mapper design pattern.

    5. `sqlalchemy` All atributes import from `sqlalchemy` for example Model Data types:- `Boolean, Column, Integer, String, Enum, ForeignKey` etc. We can import any data type from `sqlalchemy` It is provide lots of data types.

    6. The `__tablename__` attribute tells SQLAlchemy the name of the table to use in the database for each of these models.

    7. `Base`:- `declarative_base` is a factory function, that returns a base class (actually a metaclass), and the entities are going to inherit from it. Once the definition of the class is done, the Table and mapper will be generated automatically.


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