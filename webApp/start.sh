#!/bin/bash

# $1 - deploy mode

if [ $1 = "production" ]; then
        # Create database configuration file
        echo "/var/www/webApp/webApp/database/catalog.db" > db.conf
        
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

elif [ $1 = "development" ]; then
        echo "./database/catalog.db" > db.conf
fi