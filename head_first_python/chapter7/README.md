# Create a MySQL Docker service 

## Pull MySQL image
`docker pull mysql:latest`

## Run docker MySQL image(save data in: $HOME/docker/volumes/mysql)
`docker run --rm   --name mysql-docker -e MYSQL_ROOT_PASSWORD=docker -d -p 3306:3306 -v $HOME/docker/volumes/mysql:/var/lib/mysql mysql`

## Create vvsearchlog database 
- `mysql -p`
- `>enter password`
- `create database vvsearchlog`
- `CREATE USER 'vvsearchuser'@'%' IDENTIFIED BY 'vvsearchpass';`
- `GRANT ALL PRIVILEGES ON vvsearchlog.* to 'vvsearchuser'@'%';`
- `mysql -u vvsearchuser -p`

## Create a log table
CREATE TABLE log (
    id int auto_increment primary key,
    ts timestamp default current_timestamp,
    phrase varchar(128) not null,
    letters varchar(32) not null,
    ip varchar(16) not null,
    browser_string varchar(256) not null,
    results varchar(64) not null
);