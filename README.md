# Twitch Clip Downloader

## Getting a local environment up

1. Populate your `conf/envvars.sh` file. Find someone who knows how to if you don't.
2. Start local MySQL if you're using a local DB (you should), otherwise point env vars to staging. You can do this with the [backend-deps](https://github.com/Glovo/glovo-backend-deps) repo for now.
4. Build [the avro schema registry docker image](https://github.com/Glovo/avro-schema-registry) with the `avro-schema-registry` tag by cloning the repo and running `docker build . -t avro-schema-registry` inside it.
5. Start docker compose with `docker-compose -f docker-compose-dev.yml --project-name=glovo-backend up`
7. Run `./scripts/localstack-setup-streams.sh`
8. Run `./scripts/localstack-setup-registry.sh`
6. Start the server in development mode with `./console run`
7. Happy coding!

## Dependencies on external services

- All things amazon: You should be running [localstack](https://github.com/localstack/localstack) through the provided docker compose file. Remember to:
  - Specify `KINESIS_USE_LOCALSTACK="true"` on your envvars.sh file
  - Run the `script/localstack-setup-xxxx.sh` scripts whenever you restart the docker compose containers.
  - Ensure you have dummy local environment variables on your envvars.sh file. Localstack doesn't authenticate them but the Amazon libraries require them to be present. Do this by adding `AWS_ACCESS_KEY_ID="dienamerequie"` and `AWS_SECRET_ACCESS_KEY="dienamerequie"` to your envvars.sh (the values are placeholders)
- MySQL: You should be running a local mysql docker image with a copy of staging data in order to test.
- Redis: You should be running a local redis docker image through the provided docker compose file.

## Applying migrations with pt-online-schema-change

Run this from Control server.

```bash
# Do it inside screen just in case you lose connection
screen -S schema_change

# Apply the migration (see how the table appears in the DSN and not in the alter)
pt-online-schema-change\
    --execute\
    --recursion-method='dsn=D=glovo_live,t=pt_dsn'\
    --max-lag 3\
    --alter-foreign-keys-method auto\
    --progress percentage,1\
    --alter "ADD COLUMN [column] INT DEFAULT NULL"\
    h=[db_host],D=[database],t=[table],u=[user],p=[password]

# detach from screen with CTRL + A + D (if you want)

# go back to session with
screen -r schema_change
```
