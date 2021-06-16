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
4. `fb/member/login`
5. `fb/register`

## API Reference
### General
- Base URL: this app is hosted locally under the port 8000. The API base URL is `http://localhost:8000/fb`
- Authentication: this uses Basic authentication with username and password.
- You must set the header: `Content-Type: application/json` with every request a.
### Endpoints

#### 1. POST `/playgrounds`
to create a new user send a POST request with json body like:

example of request:
```bash 
curl -X POST https://fbrs.herokuapp.com/fb/playgrounds
	 -H "Content-Type: application/json" 
     -d 
    "{
        \"name\": \"CleverPG\", 
        \"price\":100, 
        \"description\":\"ooh yeah\", 
        \"address\": \"I am still just an idea in developers heads\"
    }"
	 --user "ahmed:password"
```
response:
```bash
{
    "id": 5,
    "name": "el-mesala",
    "photo": null,
    "price": 130,
    "description": "Wonderfull playground",
    "address": "Fayoum, el-mesala",
    "owner": 65
}
```

#### 2. GET `/playgrounds`
example of request: 
```bash
`curl https://fbrs.herokuapp.com/fb/playgrounds
	 -H "Content-Type: application/json"`
response:
```
```bash
[{
    "id": 1,
    "name": "CleverPG",
    "photo": null,
    "price": 100,
    "description": "ooh yeah",
    "address": "I am still just an idea in developers heads",
    "owner": 65
}, {
    "id": 2,
    "name": "alaamy",
    "photo": null,
    "price": 110,
    "description": "A  good Playground for you",
    "address": "Lower body, in your foot",
    "owner": 65
}]
```
#### 3. PUT `/playgrounds/<int:pk>`
example of request:
```bash 
`curl -X PUT https://fbrs.herokuapp.com/fb/playgrounds/1
	-H "Content-Type: application/json" 
    -d 
    "{
        \"name\": \"CleverPG\", 
        \"price\":100, 
        \"description\":\"ooh yeah\", 
        \"address\": \"I am still just an idea in developers heads\"
    }"
	--user "ahmed:password"`
```
#### 4. DELETE `/playgrounds/<int:pk>`
example of request:
```bash
curl -X DELETE https://fbrs.herokuapp.com/fb/playgrounds/7
	 -H "Content-Type: application/json"
     -u "ali:password"
```
response:
status = 204 no content


#### 5. POST `/reserve_an_h/<int:PG_pk>`
you send one value which is `reserved hour` as 
"3 2 2021 5" => "month day year hour"
example of request:

```bash 
`curl -X POST https://fbrs.herokuapp.com/fb/reserve_an_h/1
	-H "Content-Type: application/json" 
    -d 
    "{
        \"reserved_h\": \"3 2 2021 5"\"
    }"
	--user "ahmed:password"`
```
response:
```bash
{
    "id": 9,
    "reserved_hour": "2021-03-02T11:00:00Z",
    "playground_id": 1,
    "player": 73
}
```

#### 5. GET `/reserved_hs/<int:PG_pk>`

example of request:

```bash 
`curl https://fbrs.herokuapp.com/fb/reserved_hs/1
	-H "Content-Type: application/json" 
```
response:

```bash 
[
    {
        "id": 8,
        "reserved_hour": "2021-03-02T05:00:00Z",
        "playground_id": 1,
        "player": 73
    },
    {
        "id": 9,
        "reserved_hour": "2021-03-02T11:00:00Z",
        "playground_id": 1,
        "player": 73
    }
]
```


