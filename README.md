Pydir
=====

Pydir is mkdir for Python modules.

    $ pydir -v myproject/module/etc
    Created directory myproject/module/etc
    Created file myproject/__init__.py
    Created file myproject/module/__init__.py
    Created file myproject/module/etc/__init__.py
    
    $ pydir -v myproject/anothermodule
    Created directory myproject/anothermodule
    File already exists: myproject/__init__.py
    Created file myproject/anothermodule/__init__.py

