MakeMIT Website
=======

Local Dev
-----
1. Set up python virtual env
2. `pip install -r requirements.txt`
3. Edit `STATIC_ROOT` in settings.py for local dev 
4. `python manage.py compile` to compile `.styl` sheets
5. `python manage.py runserver`

Production
-----
1. `ssh athena.dialup.mit.edu`, then `ssh techfair@scripts.mit.edu` to get into the scripts console
2. Need to be in the scripts console to run `compile`
3. Edit `STATIC_ROOT` in settings.py for production
