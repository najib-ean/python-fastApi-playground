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

### 3. generate and migrate

Using _alembic_ package to do migration table to database.</br>

- First need to generate / init

  ```bash
  alembic init alembic
  ```

- Create new migration file

  ```bash
  alembic revision --autogenerate -m "your message here"
  ```

- Do migration

  ```bash
  alembic upgrade head
  ```

### 4. run the application

let's say your `main.py` is on the root folder

```bash
uvicorn main:app --reload
```

if inside folder _app_ like `/app/main.py` then do this

```bash
uvicorn app.main:app --reload
```
