djproject-12factor
==============================

Skeleton django project, following the principles of the twelve factors app or at least part of it :)


Installation
-------------------------------

1. Checkout the project:

.. code-block:: bash

  $ git clone git@github.com:{{ github_username }}/{{ project_name }}.git

2. Create the virtual environment:

.. code-block:: bash

  $ cd {{ project_name }}
  $ python bootstrap

3. Create the environment variables needed for the project (see in env.template with example):

.. code-block:: bash

  $ cat << EOF > .env
  > DEBUG=True
  > PORT=8000
  > SEND_MAIL=False
  > # Others variables
  EOF

4. Create the database::

.. code-block:: bash

  $ python manage.py syncdb --migrate

5. Start the server::

.. code-block:: bash

  $ python manage.py runserver


Observations
----------------------------
Recommend using autoenv for development:  https://github.com/kennethreitz/autoenv

And honcho for production: https://github.com/nickstenning/honcho
