# flask-http webserver
added Jenkinsfile, prometheus instrumentation and TLS reverse proxy.  

Generating self-signed TLS certificates:  
```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 -keyout /data/certificates/server.key -out /data/certificates/server.crt
```
