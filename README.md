django-regex-redirects
======================

Django redirects, with regular expressions. It is a modified version of django.contrib.redirects.

Features
========

 * Redirect your visitors using regular expressions
 * Configurable via the admin
 * Counts the number of visitors
 * Redirects are exportable as .csv


Install
=======

```python setup.py install```

Add regex_redirects to your INSTALLED_APPS:

```
INSTALLED_APPS = (
  ...
  'regex_redirects',
  ...
)
```

Add the middleware to your MIDDLEWARE_CLASSES:

```
MIDDLEWARE_CLASSES = [
  'regex_redirects.middleware.RedirectFallbackMiddleware'
  ...
]
```

Run manage.py syncdb and you're good to go!




