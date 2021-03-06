# App dirs structure

When apps start to grow its good practice to modularize and break it down into several files and subdirectories to make maintenance and refactoring easier. In this lecture will do just that for the puppies app. This is the structure that we'll use:

``` txt
<root>
  |__ app.py
  |__ <migrations>
  |     |__ ...
  |
  |__ <myproject>
  |     │__ __init__.py
  |     │__ models.py
  │     │__ data.sqlite
  │     |__ <owners>
  │     │     │__ forms.py
  │     │     │__ views.py
  │     │     |__ <templates>
  │     │           |__ <owners>
  │     │                 |__ add_owner.html
  │     │
  │     |__ <puppies>
  │     │     │__ forms.py
  │     │     │__ views.py
  │     │     |__ <templates>
  │     │           |__ <puppies>
  │     │                 │__ add.html
  │     │                 │__ delete.html
  │     │                 │__ list.html
  |     |
  │     |__ <static>
  |     |     |__ <css>
  |     |     |     |__ ...
  |     |     |
  |     |     |__ <js>
  |     |     |     |__ ...
  |     |     |
  |     |     |__ <img>
  |     |           |__ ...
  |     |     
  │     |__ <templates>
  │           |__ base.html
  │           |__ home.html
  |
  |__ Pipfile
  |__ Pipfile.lock
  |__ README.md
  |__ .gitignore
  |__ .gitattributes
```

To achive this we are going to use **blueprints**. These blueprints will allow us to register a `url_prefix` for each `views.py` file. So we can have a `/owners/add` endpoint and a `/puppies/add` endpoint without Flask getting confused when using two add views.

The blueprints will be created in the `views.py` files for each model, and then registered in the `__init__.py` script. In that file, the blueprints need to be definied after setting up the DB.

``` python
from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint, url_prefix = "/owners")
app.register_blueprint(puppies_blueprint, url_prefix = "/puppies")
```
