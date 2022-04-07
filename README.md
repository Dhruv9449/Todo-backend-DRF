# Todo Backend Django-rest-framework

Todo Backend project for learning Django-rest-framework using [Todo-Backend specs](https://todobackend.com/).


<br>


## Setup

### Virtual environment 

Setup and activate virtual environment-  

Linux
```sh
user@Host:/Projectpath$ virtualenv venv
user@Host:/Projectpath$ source venv/bin/activate
```  
Windows
```psh
C:\Users\user> virtualenv venv
C:\Users\user> source venv/Scripts/activate
```
Refer to the [official virtualenv documentation](https://virtualenv.pypa.io/en/latest/) for any further help
  
<br><br>

### Environment Variables 
You will need create a `.env` as shown in [`.env.example`](todo/todo/.env.example) inside the [`todo/todo/`](todo/todo/) folder with -  

`.env` format
```
SECRET_KEY=<Your Django key>
```

<br><br>

### Installing dependancies
To install all the dependancies for this project run the following command in your terminal - 
```sh
pip install -r requirements.txt
```

<br><br>

### Migrate Changes in database
Before you can get the server up and running you will have to migrate the changes made in the database. Run the following command -  

Windows
```psh
C:\Users\Username\dir> python manage.py migrate
```
Linux
```sh
user@hostname:~$ python3 manage.py migrate
```
> NOTE: Make sure you are in the `todo/` folder while running this command

<br><br>

### Run the server!
We're all set the run the server now! Type the following command in your terminal -  
```
./manage.py runserver
```
or  
Windows
```psh
C:\Users\Username\dir> python manage.py runserver
```
Linux  
```sh
user@hostname:~$ python3 manage.py runserver
```
And then type `localhost:8000` or `127.0.0.1:8000` in your browser's search bar and voila!

> NOTE: Make sure you are in the `todo/` folder while running this command

<br><br>

### Test the API

Head over to [Todo-backend's website](https://todobackend.com/specs/) and enter target root as `localhost:8000` or `127.0.0.1:8000`.

<br><br>

## License 
Copyright © 2022 Dhruv9449  
[MIT License](LICENSE)

<br>
<br>
<p align="center">
Developed by <a href="https://github.com/Dhruv9449" target=_blank>Dhruv Shah</a>
</p>
</p>