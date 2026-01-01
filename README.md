# step by step

### 1. create virtual environment and activate it

create virtual environment:

```bash
python -m venv <env_name>
```

activate the environment:

```bash
source myenv/bin/activate
```

If you want to `deactivate`:

```bash
deactivate
```

### 2. package installation

You can do put all the packages required to one file requirements.txt, and then do installation command

```bash
pip install -r requirements.txt
```

### 3. after do some codes then run the application

let's say your `main.py` is on the root folder

```bash
uvicorn main:app --reload
```

if inside folder _app_ like `/app/main.py` then do this

```bash
uvicorn app.main:app --reload
```
