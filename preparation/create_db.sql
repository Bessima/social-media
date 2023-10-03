CREATE USER social_user WITH ENCRYPTED PASSWORD 'password';

CREATE DATABASE social_media;
-- \c social_media;
-- CREATE EXTENSION citus;

GRANT ALL PRIVILEGES ON DATABASE social_media TO social_user;

GRANT ALL ON DATABASE social_media TO social_user;
ALTER DATABASE social_media OWNER TO social_user;
-- ALTER ROLE social_user SUPERUSER;