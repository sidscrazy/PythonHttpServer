# PythonHttpServer
This repository contains two Python servers - one for HTTP server and one for HTTPS server. Both of them are configured to listen to port 8585
Once port forwrding is set on the router for port 8585, firewall exclusion added for port 8585 and server started on home machine, the server will be available across the internet for anyone. For safety, it is better to only run HTTPS server on the home machine after configuring locally generated certificates using openssl
