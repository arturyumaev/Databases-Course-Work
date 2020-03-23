# disable site
sudo a2dissite webApp
sudo systemctl reload apache2

# enable site
sudo a2ensite webApp
sudo systemctl reload apache2

# restart apache
sudo service apache2 restart