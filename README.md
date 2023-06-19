
<h2 align="center">PERSONAL</h2>

## :scroll: Description

This is a website where you can customize your website the way you want through Django Admin. The site was created with the aim of helping online course sellers, personal trainers, and other professionals promote their sales and redirect customers to direct contact with the service provider.

Here, you have the freedom to customize and adapt your website according to your needs and preferences. With the Django Admin platform, you can easily manage content, add new products or services, and even track sales performance.

Our proposition is to provide a practical and efficient solution for you to promote your business more effectively. Through our system, you will have an online showcase to display your products or services, as well as offer a direct communication channel for potential customers to get in touch with you.

## :rocket: Technologies

The technologies usage in this project is:
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [JavaScript](https://www.javascript.com/)
- [Bootstrap](https://getbootstrap.com/)
- [JQuery](https://www.sqlite.org/)


##  :wrench: Setup
Clone this repository in your computer.
```
$ git clone https://github.com/JuanPabloDS/SMRings.git
```
After, install python development package:

Ubuntu.
```shell
$ sudo apt-get install python-dev
```

Fedora.
```shell
$ sudo dnf install python3-devel
```

Inside the project directory, you need to create your virtual enviroment and active it:
```shell
$ python -m venv pyenv
$ source pyenv/bin/activate
```

Upgrade pip:
```shell
$ pip install -U pip
```

Run the command to install the env requirements:
```shell
$ pip install -r requirements.txt
```

Run the migrations:
```shell
$ python manage.py migrate
```

Create your Django User:
```shell
$ python manage.py createsuperuser
```

Start the application:
```shell
$ python manage.py runserver
```

Look the swagger accessing *http://localhost:8000*
Look the django-admin accessing *http://localhost:8000/admin* and use your superuser email and password.
