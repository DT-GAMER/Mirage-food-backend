# MIRAGE FOOD 

# Setup, Installation and Contribution Instructions

## Prerequisites
1. Ensure you have `python3` version >=3.8 installed. To find out about this, Open a command prompt or terminal and type `python3 -v`.
2. You have a text editor (preferably VScode) installed on your computer
3. You have mysql set up as it is what we will be using

## Contributing Rules
1. Clone repository
 ```bash
git clone git@github.com:mwiks-dev/AskGiver.git 
```
or
 ```bash
git clone https://github.com/mwiks-dev/AskGiver.git 
```

2. Checkout to a branch using the following format ft-<feature-being-developed>(e.g git checkout -b ft-getallusers)

NOTE: All Pull requests should be made toward the development branch.

## Create and Activate Virtual Environment
  Navigate into the folder you cloned the project
 ```bash
 python3 -m venv virtual
 source virtual/bin/activate
```
 Ensure that this file is hidden inside the gitignore
## Create dotenv file for storing secrets and credentials
 ```bash
 touch .env
```

## Setting Up Cloudinary Credentials

- Sign Up for Cloudinary, If you haven't already

- After logging in, you'll be redirected to your Cloudinary dashboard.
Retrieve Your API Credentials for Python:

## Configure your project secrets and credentials in this file

### Sample dotenv file will have the following structure:

 ```bash
 SECRET_KEY='REPLACE_ANY_SECRET_kEY'
 DB_NAME='REPLACE_DATABASE_NAME'
 DB_USER='REPLACE_DATABASE_USERNAME'
 DB_PASSWORD='REPLACE DATABASE_PASSWORD'
 CLOUDINARY_CLOUD_NAME='REPLACE_ME'
 CLOUDINARY_API_KEY='REPLACE_ME'
 CLOUDINARY_API_SECRET='REPLACE_ME'
 ```
**Ensure that this file is hidden inside the gitignore**


## Install Dependencies 
 ```bash
 pip3 install -r requirements.txt
```
or
 ```bash
 python3 -m pip install -r requirements.txt
```

## Configuring your database, apply the database migrations using the following command:

 ```bash
 python3 manage.py migrate
```
## Run the application 
 ```bash
 python3 manage.py runserver
```
Open the application on your browser `127.0.0.1:8000`.

## Making a Commit
Ensure to follow these steps when committing:

1. git add .
2. git commit -m <_message here_>
3. git pull origin development
4. git push origin <name-of-your-branch>

## Opening a Pull request

1. Go to github
2. Open a new Pull Request to the Development Branch and not the Main Branch.

## Technology used 
- [Python 3.10.12](https://www.python.org/)
- [Django == 4.2.4](https://docs.djangoproject.com/en/4.2/)
- [Cloudinary](https://cloudinary.com/)
- [MySQL](https://www.mysql.com/)
