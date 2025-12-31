## step by step

#### create virtual environment and activate it

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

#### package installation

install fastApi and the web server runner `uvicorn`:

```bash
pip install fastapi uvicorn
```

install orm sqlAlchemy and postgres package. Remember NOT **psycopg2** but `psycopg`:

```bash
pip install sqlalchemy psycopg
```
