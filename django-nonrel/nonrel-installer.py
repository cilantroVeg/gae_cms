#!/usr/bin/env python
import subprocess

def get_urls_master():
    urls_master = [
        "git clone https://github.com/django-nonrel/django.git",
        "git clone https://github.com/django-nonrel/djangoappengine.git",
        "git clone https://github.com/django-nonrel/djangotoolbox.git",
        "hg clone https://bitbucket.org/twanschik/django-autoload",
        "git clone https://github.com/django-nonrel/django-dbindexer.git",
        "git clone https://github.com/django-nonrel/django-testapp.git"
    ]
    return urls_master


def get_project_list():
    project_list = [
        'cms',
        #'arturo',
        #'interpegasus',
        #'magicangel',
        #'music',
        #'nrwl',
        #'recipes',
        #'yiyask',
        'django-testapp'
    ]
    return project_list


def main():
    url_array = get_urls_master()
    for url in url_array:
        subprocess.call(url, shell=True)

# Installs the base system for django-nonrel
main()