### 1. Setup dev environment

First of all, you must have the virtual env intalled in your machine.
[Installing virtualenv](https://virtualenv.pypa.io/en/stable/installation/ "Installing virtualenv")  

Run the steps bellow:
```bash
virtualenv -p $(which python3.6) venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

------------


### 2. Initial project setup
**Attention:** This section is dedicated to create the project from default boilerplate.

1. Change in all project the variable ***TEMPLATE-CHANGE*** for the ***project name***;
2. Change the URL from the origin remote to the new repository created by cloudformation
```bash
git remote set-url origin ssh://[SA-EAST-1-ALIAS]/v1/repos/[TEMPLATE-CHANGE]
```
3. Create the cloudformation infraestructure executing the script below:
```bash
./setup-cloudformation.sh
```

------------

### Running locally
````
$ chalice local --port=8084 --stage dev
````
**Having problem to run?**
Try:
````
$ pip2 uninstall chalice
````

------------
