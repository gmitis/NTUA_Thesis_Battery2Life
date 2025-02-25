-- disable write ahead logging and checkpoints for batch population of the database
ALTER SYSTEM SET synchronous_commit = 'off';
ALTER SYSTEM SET wal_level = 'minimal';
ALTER SYSTEM SET wal_keep_size = 0;
ALTER SYSTEM SET max_wal_senders = 0;
ALTER SYSTEM SET archive_mode = off;


CREATE DATABASE b2l;



DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'root') THEN
        CREATE ROLE root WITH LOGIN PASSWORD 'root';
        ALTER ROLE root WITH SUPERUSER LOGIN CREATEDB REPLICATION CREATEROLE;
    END IF;
END $$;
