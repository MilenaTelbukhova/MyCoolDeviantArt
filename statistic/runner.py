import psycopg2
from datetime import datetime
import os

def long_path(short_path: str) -> str:
    current_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_path, short_path)


dbname = os.getenv('PG_DBNAME', default="postgres")
user = os.getenv('PG_USER', default="CapTof")
password = os.getenv('PG_PASSWORD', default="CapTof")
host = os.getenv('PG_HOST', default="localhost")
port = os.getenv('PG_PORT', default="5432")
number_of_experiment = os.getenv('NUMBER_OF_EXPERIMENT', default=5)

queries = {
'''
SELECT P."Description"
FROM public."User" as U JOIN public."Post" as P on U."UserID" = P."AuthorID"
WHERE U."Username" = 'Rusty';''',
'''
SELECT *
FROM "User" AS U JOIN "Message" AS M on U."UserID" = M."AuthorID"
WHERE M."IsDeleted" = true and U."Username" = 'Rusty';
''',
'''
SELECT P."Description"
FROM "Group" AS G INNER JOIN "Post" AS P ON G."GroupID" = P."GroupID"
WHERE "GroupName" = 'pdf';''',
'''
SELECT SB."SubscribeName"
FROM "Subscribe" AS SB JOIN "Subscriber" AS SBR ON SB."SubscribeID" = SBR."SubscribeID"
WHERE SBR."EndOfSubscribe" = '2024-06-17' AND SB."Price" > '100.00';'''}


results_path = long_path(f'results/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}')
file = open(f'{results_path}.csv', 'a')
file.write("min,main,max\n")

with psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}") as conn:
    with conn.cursor() as cur:
        for query in queries:
            data = []
            for j in range(number_of_experiment):
                cur.execute(f'EXPLAIN ANALYSE {query}')
                tmp = cur.fetchall()
                result = tmp[-1][0].replace("Execution Time: ", "").replace(" ms", "")
                data.append(float(result))
            min_data = round(min(data), 3)
            max_data = round(max(data), 3)
            main_data = round(sum(data)/number_of_experiment, 3)
            file.write(f"{min_data},{main_data},{max_data}\n")
