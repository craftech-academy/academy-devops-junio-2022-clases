Parte 2 - Dockerfile:

Nginx:

docker build -f Dockerfile-nginx . -t nginx-custom:0.0.1

docker run -d --name nginx-1 --network test nginx-custom:0.0.1

Alpine:

docker build -f Dockerfile-alpine . -t alpine-custom:0.0.1 

docker run -d --name alpine-1 --network test -e NGINX_IP='nginx-1' alpine-custom:0.0.1

MultiStage:

