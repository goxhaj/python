#Create a MySQL Docker service 

## Pull MySQL image
`docker pull mysql:latest`

## Run docker MySQL image(save data in: $HOME/docker/volumes/mysql)
docker run --rm   --name mysql-docker -e MYSQL_ROOT_PASSWORD=docker -d -p 3306:3306 -v $HOME/docker/volumes/mysql:/var/lib/mysql mysql