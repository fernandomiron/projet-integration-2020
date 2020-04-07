# Institut des Carrières Commerciales 2019-2020: Projet d'intégration de développement

*Author: Bryan M. Ramsamy - March 2020*

This documentaion is based on a linux (Ubuntu 18.04.4 LTS) version.

For Windows or Mac, please refere to the matching documentation.

Creating and developping on a virtual Ubuntu 18.04.4 machine is higly recommanded in order to keep the development environment as simimilar as possibl between the different developpers.

## IMPORTANT NOTES

- **NEVER PUSH DIRECTLY ON MASTER**
- **ALWAYS UPDATE YOUR BRANCH FROM MASTER**
- **DO NOT FORGET TO MAKE MIGRATIONS AND MIGRATE AFTER EACH FETCH/PULL FROM GITHUB**
- **ENGLISH CODE ONLY**
- **ALWAYS ADD EXPLICIT MESSAGES TO YOUR COMMITS**
- **ALWAYS DOCUMENT YOUR CODE**

## Prerequisites

This documentation has been provided by DigitalOcean before being readapted: <https://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04>

Our first step will be install all of the pieces that we need from the repositories. We will install `pip3`, the Python package manager, in order to install and manage our Python components. We will also install the database software and the associated libraries required to interact with them.


### Install MySQL

**Important note: For this project, python3 will be used. python2 has been deprecated since January 2020 and won't have further support !**

```bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev mysql-server libmysqlclient-dev
```

You will be asked to select and confirm a password for the administrative MySQL account.

After the installation, you can create the database directory structure by typing:

```bash
sudo mysql_install_db
```

You can then run through a simple security script by running:

```bash
sudo mysql_secure_installation
```

*Note: this installation method has been deprecated but stills works. It should be enough for this project.*

You’ll be asked for the administrative password you set for MySQL during installation. Afterwards, you’ll be asked a series of questions. Besides the first question which asks you to choose another administrative password, select yes for each question.

### Create the database and the database user

We can start by logging into an interactive session with our database software by typing the following (the command is the same regardless of which database software you are using):

```bash
mysql -u root -p
```

You will be prompted for the administrative password you selected during installation. Afterwards, you will be given a prompt.

First, we will create a database for our Django project. Each project should have its own isolated database for security reasons. We will call our database `reservations`. We’ll set the default type for the database to UTF-8, which is what Django expects:

```sql
CREATE DATABASE reservations CHARACTER SET UTF8;
```

Remember to end all commands at an SQL prompt with a semicolon.

Next, we will create a database user which we will use to connect to and interact with the database. Set the password to something strong and secure. For this project, we will use and communicate the same user and password.

*Note: Keep in mind, sharing credentials like this is highly prohibited and should be done in a real development project !*

```sql
CREATE USER pid_admin@localhost IDENTIFIED BY 'PID_2020pass';
```

**As you can see, the username used in this project would be `pid_admin`, while the password will be `PID_2020pass`. The settings.py file has already been configured with those credentials. You can use other credentials, but don't forget to change them in the settings.py file too.**

Now, all we need to do is give our database user access rights to the database we created:

```sql
GRANT ALL PRIVILEGES ON reservations.* TO pid_admin@localhost;
```

Flush the changes so that they will be available during the current session:

```sql
FLUSH PRIVILEGES;
```

Exit the SQL prompt to get back to your regular shell session:

```sql
exit
```

### Install Django with virtualenv

You can get the virtualenv package that allows you to create these environments by typing:

```bash
sudo pip3 install virtualenv
```

Make sure you are in the root directory of your Django project !

We can create a virtual environment to store our Django project’s Python requirements by typing:

```bash
virtualenv env
```

This will install a local copy of Python3 and pip3 into a directory called `env/` within your project directory.

*Note: The `env/` folder has already been added in the `.gitignore` file. If you chose another name for your virtualenv, don't forget to adjust in the `.gitignore`. But this is not recommanded. Working as a team, we should avoid using different .gitignore files.*

Before we install applications within the virtual environment, we need to activate it. You can do so by typing:

```bash
source env/bin/activate
```

Your prompt will change to indicate that you are now operating within the virtual environment. It will look something like this `(env)user@host:~/reservations$`.

*Note: You can deactivate the virtualenv by the following command:*

```bash
deactivate
```

**Important note: Keep in mind that all the requirements must be installed. If you don't run a virtualenv, every requirements will be installed directly on your global environment, which can lead to conflicts if you have other apps running !**

**Important note: You won't be able to run the Django dev-server correctly if you don't activate the virtualenv !**

Once your virtual environment is active, we can install the requirements with `pip3` in our virtual. `Django` and `mysqlclient` packages are the most required. `Django` will install the framework architecure while `mysqlclient` will allow us to use the database we configured.

All of them are available with the other required and optional packages in the `requirement.txt` file. `pip3` can read this file and install everything declared in it. If no version is sepcified, python3 will automatically try to get the latest version, which can cause conflicts in some cases:

```bash
pip3 install -r requirements.txt
```

### Import manually the environment file

The project-leader should provide you an `.env` file.
This file contains senssible credentials and MUST NOT be shared on the repository. The file was already added into the `.gitignore` file.

You must put the `.env` file in the `reservation/reservation` directory, alongside the `manage.py` file.

### Let Django prepare the MySQL database tables

Now that the Django settings are configured, we can migrate our data structures to our database and test out the server.

We can begin by creating and applying migrations to our database. Since we don’t have any actual data yet, this will simply set up the initial database structure:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Create a superuser

After creating the database structure, we can create an administrative account by typing:

```bash
python3 manage.py createsuperuser
```

You will be asked to select a username, provide an email address, and choose and confirm a password for the account.

*Note: This one can be unique for you. All the team members mustn't use the same superuser's credentials*

### Launch the Django runserver_plus

You can now run the runserver script with the follwing command:

```bash
./scripts/runserver.sh
```

If the server fails to start, it will be relaunched every 5 seconds by displaying an error message in the terminal. Keep the server's log attached to the terminal to get the error messages.

Press `Ctrl + C` to kill the server.

The Django dev-server is exposed on the port 8000.
You can access to it by typing the following address in your web browser: `localhost:8000`

By default, no home page has been created yet but you can access to the admin panel by entering the following url: `localhost:8000/admin/` and entering your superuser's credentials.

## Tools

### ipython

It's recommand to use the ipython shell_plus instead of the regular python3 shell. iPython provides a lot of usefull and convenient functions and make the use of the shell more easy.

```bash
python3 manage.py shell_plus
```

If you want to use the original python3 shell, you still can with this command:

```bash
python3 manage.py shell
```
