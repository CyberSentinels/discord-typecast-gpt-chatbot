# compassionate conversationalist bot

## How to run this server locally
To get started with running this repository, you need to perform the following steps:

1. Clone the repository from GitHub using 

```sh
git clone REPO_GIT_URL
```

2. Create a new virtual environment using `venv`:
```sh
python3 -m venv venv
```

3. Activate the virtual environment:
```sh
source venv/bin/activate
```

4. Install the dependencies listed in `requirements.txt`:
```sh
pip install -r requirements.txt
```

5. Start the FastAPI app:
```sh
uvicorn app.main:app --reload
```

> Don't forget to activate the virtual environment each time you work on the project in a new terminal session by running the activate command again.

After these steps, you should be able to access the app by visiting http://localhost:8000 in your web browser.

## Testing
```sh
# run all tests in the tests/ folder
pytest --cov=app tests/
```
