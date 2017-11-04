**twisted_and_threading**

__A test project integrating twisted with APIs using threading__

This will log to stdout showing no problem:
$ pyhton working_application.py


This will log to twistd.log showing only TCP server is running (use client.py to test)
Interestingly the 3rd party service start message is STILL printed to stdout:
$ twistd -y not_working.tac


This will log to twistd.log (3rd party start message AS WELL) and will work as expected:
$ twistd -y working.tac  #will work and log t