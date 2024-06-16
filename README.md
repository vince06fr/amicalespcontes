# Amicalespcontes

Amicalespcontes is a fork of [pinax-calendars](https://github.com/pinax/pinax-calendars)  modified to serve as a reservation site for the association of Contes firefighters.  
`pinax-calendars-demo` is a demo project to show how the [pinax-calendars](https://github.com/pinax/pinax-calendars) app works.



[Join pinaxproject on Slack](http://slack.pinaxproject.com/)

Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates. 
This collection can be found at http://pinaxproject.com.

This app was developed as part of the Pinax ecosystem but is just a Django app and can be used independently of other Pinax apps.


Getting Started
---------------

```
# first clone the project and cd into project directory
# Then, create a virtual environment and activate it
python3.7 -m venv
source venv/bin/activate
# update virtualenv
pip install - U pip setuptools
# optionally, you can install wheel(https://pythonwheels.com/) 
pip install wheel
# install the development requirments
pip install - r requirements/development.txt
# export the environment variables for testing
unset DJANGO_SETTINGS_MODULE
unset SECRET_KEY
export DJANGO_SETTINGS_MODULE="events.settings.development"
export SECRET_KEY="secret"
# migrate & run
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

Deployment in production is out of scope, please refer to the [official django documentation](https://docs.djangoproject.com/en/dev/howto/deployment/)


Pinax Documentation
----------------

The Pinax documentation is available at http://pinaxproject.com/pinax/. The `pinax-calendars-demo` documentation is currently under construction. If you would like to help us improve our documentation or write more documentation, please join our Pinax Project Slack team and let us know!


Contribute to Pinax
----------------

See [this blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/) including a video, or our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our [Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions, we would recommend for you to join our [Pinax Slack team](http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We would also highly recommend for your to read our [Open Source and Self-Care blog post](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).  


Pinax Code of Conduct
-----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found [here](http://pinaxproject.com/pinax/code_of_conduct/). 
We'd like to ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.



Pinax Project Blog and Twitter
-------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.


