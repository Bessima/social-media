CREATE USER social_user WITH ENCRYPTED PASSWORD 'password';

CREATE DATABASE social_media;

GRANT ALL PRIVILEGES ON DATABASE social_media TO social_user;
