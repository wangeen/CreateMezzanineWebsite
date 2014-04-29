CreateMezzanineWebsite
======================

The script for build a website with Mezzanine on a total new machine.


http://www.rosslaird.com/blog/customizing-mezzanine/  
http://getbootstrap.com/getting-started/#customizing  
http://mezzanine.jupo.org/docs/content-architecture.html#overriding-vs-extending-templates  
https://github.com/twbs/bootstrap  

Possible Issues while install.

- **no such table: pages_page?**  
    ./manage.py syncdb  
    ./manage.py migrate

- **sharing host commit**  
      #!/usr/bin/env python  
      import subprocess  
      subprocess.call("git push", shell=True)  
      subprocess.call('''ssh name@name.com "cd name.com; pwd; git checkout HEAD .; pkill python"''', shell=True)  
