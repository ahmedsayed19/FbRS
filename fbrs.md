# Football Playground Reservation Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Django]

- [Django-Rest-Framework]

## Running the server

Ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
source env/bin/activate
```

To run the server, execute:

```bash
python manage.py runserver
```

### End points


1. `fb/playgrounds`
2. `fb/playgrounds/<int:pk>`
3. `fb/reverse_h/<int:pk>`
4. `fb/member`
5. `fb/member/<int:pk>`
6. `fb/member/login`