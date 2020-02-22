# flask-http webserver
Test webserver for opsschool jenkins/Monitoring class.  
With added Jenkinsfile, prometheus instrumentation and TLS reverse proxy.  
Thanks Tsahi!

Generating self-signed TLS certificates:  
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /data/certificates/server.key -out /data/certificates/server.crt
```
