#!/usr/bin/env python
import os.path
import inspect
import timeit
import subprocess

def script(cmd):
    print cmd
    subprocess.call(cmd,  shell=True)


def installPackage():
    print "Install Packages"
    script("sudo pip install south")
    script("sudo pip install django-compressor")
    print "The following step is a bit slow,  please pay attention."
    script("sudo pip install mezzanine")
    script("source ~/.bashrc")
    pass

def newMezzanineProject():
    script("mezzanine-project mysite")
    os.chdir("mysite")
    script("python manage.py createdb")
    # create your theme
    script("django-admin.py startapp myTheme")
    os.chdir("myTheme")
    script("mkdir static")
    os.chdir("static")
    script("mkdir css img js")
    os.chdir("..")
    script("mkdir templates")
    os.chdir("templates")
    script("mkdir includes")
    os.chdir("..")
    os.chdir("..")
    print "Hah, almost done, now please customize your UI."
    print '''
    From that point on,
    a theme in Mezzanine can be implemented entirely as a standard Django app.
    Simply create a Django app with templates and static directories,
    copy the relevant HTML,
    CSS and JavaScript files into it from Mezzanine that you wish to modify,
    '''
    print "Please refer to http://www.rosslaird.com/blog/customizing-mezzanine/ for detail"
    script("python manage.py runserver")
    pass

if __name__  ==  "__main__":
    print '''
        Script for build a website from Zero
    '''
    # uncomment following line to enable install package
    #installPackage()
    newMezzanineProject()

    pass


