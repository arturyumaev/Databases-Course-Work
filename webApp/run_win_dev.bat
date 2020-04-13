del config.ini
echo DATABASE=sqlite3> config.ini
echo PATH=./database/catalog.db>> config.ini

set FLASK_ENV=development
set FLASK_APP=app.py
set FLASK_DEBUG=1

flask run