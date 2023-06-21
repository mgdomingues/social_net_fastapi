# social_net_fastapi
social network api backend exercise using python FastAPI

Follow [Python API Development - Comprehensive Course for Beginners](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=46973s)

## Getting started

Install python 3.*.* and VSCode
 
### Create a Virtual Enviroment

inside your project folder run ```python3 -m venv venv```

### Change VSCode Pythn interpreter to the one in the venv

In VSCode
view -> command palette -> (search) python select interpreter -> select enter path
Enter the path to your virtual enviroment interpreter /[path to project]/venv/bin/


## FastAPI

### Install
```pip install "fastapi[all]"```

### Running the code on a web server

run
```uvicorn main:app```

unicorn [main python file]:[name given to fastAPI instance]

To reload on save
```uvicorn main:app --reload```

Go to the browser and open the link http://127.0.0.1:8000 