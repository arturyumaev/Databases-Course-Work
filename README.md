# Databases-Course-Work

#### Подключение к удаленной VM:

```
$ ssh arturyumaev@52.170.255.31
```

#### Разработка велась на windows, поэтому для запуска нужно установить переменные окружения

```
>set FLASK_APP=app.py
>set FLASK_ENV=development
```

Для запуска на продакшне, установить окружение обратно

```
>set FLASK_ENV=production
```

#### Работа на удаленном сервере и деплой сервиса

Step 1: Я использовал Microsort Azure сервер (беспланую пробную версию)

Step 2: Скачать PuTTY и войти по SSH на 52.170.255.31

Step 3: Скачать и установить Apache
- sudo apt update
- sudo apt install apache2
- apache2 -version

Step 4: Установить конфигурацию Firewall
- sudo ufw app list
- sudo ufw allow ‘Apache’

Step 5: Установить конфигурацию Apache
- sudo systemctl status apache2  

Step 6: Скачать и включить mod_wsgi
-       sudo apt-get install libapache2-mod-wsgi python-dev

Step 7: Создать приложение Flask (уже было создано). Желательно по тому же пути, потому что дальнейшая конфигурация напрямую от этого зависит
-       cd /var/www 
-       sudo mkdir webApp
-       cd webApp

Step 8: Install flask
-        sudo apt-get install python-pip
- 	 sudo apt-get install python3-pip 
-        sudo pip install Flask 
- 	 sudo pip3 install Flask
-        sudo pip install flask_sqlalchemy
- 	 sudo pip3 install flask_sqlalchemy
- 	 sudo apt install python3-flask
-	 sudo apt install python-flask

Step 9: Использовать WinSCP для трансфера файлов по SSH на сервер или через гит

Step 10: Прописать конфигурацию и активировать виртуальный хост
- 	cd /etc/apache2/sites-available
- 	sudo touch webApp.conf
или
-       sudo vim /etc/apache2/sites-available/webApp.conf

```
<VirtualHost *:80>
		ServerName 52.170.255.31
		ServerAdmin email@mywebsite.com
		WSGIScriptAlias / /var/www/webApp/webapp.wsgi
		<Directory /var/www/webApp/webApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/webApp/webApp/static
		<Directory /var/www/webApp/webApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```


-      sudo a2ensite webApp 
-      systemctl reload apache2

Step 11: Создаем  .wsgi файл (уже создан в директории)
-      sudo nano webapp.wsgi 

```python
#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/webApp/")

from webApp.app import app as application
application.secret_key = 'Add your secret key'
```


Step 12: Перезапускаем apache
-      sudo service apache2 restart 

Step 13: Visit the ip address of your server in the browser to  access your website!

Полное видео с туториалом тут:https://www.youtube.com/watch?v=YFBRVJPhDGY

