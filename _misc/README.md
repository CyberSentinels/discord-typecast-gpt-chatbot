1. Follow steps in the README.md in this repo's root directory

2. cd into this direcotry and then run the following:

```sh
vicorn app.main:app --reload
```

> Don't forget to activate the virtual environment each time you work on the project in a new terminal session by running the activate command again.

After these steps, you should be able to access the app by visiting http://localhost:8000 in your web browser.

## Testing
```sh
# run all tests in the tests/ folder
pytest --cov=app tests/
```