SELECT 'CREATE DATABASE pet_adoption_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'pet_adoption_db')\gexec