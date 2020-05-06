# $1 - deploy mode

rm config.ini
./redisTools.sh start # Start redis server

if [ "$1" = "prod" ]
then
  # Create database configuration file
  echo DATABASE=sqlite3> config.ini
  echo PATH=/var/www/webApp/webApp/database/catalog.db>> config.ini
        
  # Apache needs full rights on reading and writing
  sudo chmod -R 777 /var/www/webApp/

  # Disable site if already started
  sudo a2dissite webApp
  sudo systemctl reload apache2

  # Enable site
  sudo a2ensite webApp
  sudo systemctl reload apache2

  # Restart Apache
  sudo service apache2 restart
elif [ "$1" = "dev" ]
then
  echo DATABASE=sqlite3> config.ini
  echo PATH=./database/catalog.db>> config.ini

  python3 app.py
else
  echo "No keywords found!"
  echo "Use ./start [prod|dev]"      
fi

./redisTools.sh stop
