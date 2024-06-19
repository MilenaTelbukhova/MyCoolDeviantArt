echo "Creating roles"
psql postgresql://"${PG_USER}":"${PG_PASSWORD}"@"${PG_HOST}"/postgres << EOF
    CREATE ROLE reader;
    CREATE ROLE writer;
    CREATE ROLE group NOLOGIN;

    GRANT CONNECT ON DATABASE postgres TO reader;
    GRANT CONNECT ON DATABASE postgres TO writer;
    GRANT CONNECT ON DATABASE postgres TO group;

    GRANT USAGE ON SCHEMA public TO reader;
    GRANT USAGE ON SCHEMA public TO writer;
    GRANT USAGE ON SCHEMA public TO group;

    GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader;
    GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO writer;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO group;
EOF

echo "Roles created"
echo "Creating users"
users="${USERS:-user1:password1:reader,user2:password2:writer,user3:password3:group}"

for user in ${users//,/ }
do
    username=$(echo "$user" | cut -d ':' -f 1)
    password=$(echo "$user" | cut -d ':' -f 2)
    role=$(echo "$user" | cut -d ':' -f 3)

    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -p "$POSTGRES_PORT" <<-EOSQL
        CREATE USER $username WITH PASSWORD '$password';
        GRANT $role TO $username;
EOSQL
done && echo "Users created"