CREATE USER social_user WITH ENCRYPTED PASSWORD 'password';

CREATE DATABASE social_media;

GRANT ALL PRIVILEGES ON DATABASE social_media TO social_user;

GRANT ALL ON DATABASE social_media TO social_user;
ALTER DATABASE social_media OWNER TO social_user;