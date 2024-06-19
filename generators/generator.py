import random
import psycopg2
from psycopg2.extras import execute_batch
import os
import mimesis

def table_size(cursor, table_name: str):
    cursor.execute(f'SELECT COUNT(*) FROM "{table_name}"')
    tab_size = cursor.fetchone()
    if tab_size is None or tab_size == ():
        return 0
    return tab_size[0]


def get_id(cursor, table_name, column_name):
    cursor.execute(f'SELECT "{column_name}" FROM "{table_name}"')
    tmp = cursor.fetchall()
    return [int(i[0]) for i in tmp]


def generate_user(cursor, count: int):
    person = mimesis.Person()
    text = mimesis.Text()
    file = mimesis.File()
    execute_batch(cursor,
                  f'INSERT INTO "User" ("Username", "E_mail", "Password", "Status", "AvatarImage") '
                  f'VALUES (%s, %s, %s, %s, %s)',
                  [(person.name(),
                    person.email(),
                    person.password(),
                    text.sentence(),
                    file.file_name())
                   for i in range(count)])


def generate_theme_of_a_day(cursor, count: int):
    date = mimesis.Datetime()
    theme = mimesis.Text()
    execute_batch(cursor, f'INSERT INTO "ThemeOfADay" ("Date", "ThemeName") '
                          f'VALUES (%s, %s)',
                  [(date.date(), theme.words(2))
                   for i in range(count)])


def generate_group(cursor, count: int):
    name = mimesis.Text()
    logo = mimesis.File()
    execute_batch(cursor, f'INSERT INTO "Group" ("GroupName", "GroupLogo") '
                          f'VALUES (%s, %s)',
                  [(name.word(), logo.file_name())
                   for i in range(count)])


def generate_role(cursor):
    execute_batch(cursor, f'INSERT INTO "Role" ("RoleName") '
                          f'VALUES (%s);',
                  [["Owner",], ["Poster",], ["Subscriber",]])


def generate_subscribe(cursor, user_id: list[int], group_id: list[int], count: int):
    name = mimesis.Text()
    execute_batch(cursor, f'INSERT INTO "Subscribe" ("Price", "SubscribeName", "SubscribedUserID", "SubscribedGroupID")'
                          f'VALUES (%s, %s, %s, %s)',
                  [(round(random.uniform(7.00, 1000.00), 2),
                    name.word(),
                    random.choice(user_id),
                    None)
                   for i in range(int(count / 2))])
    execute_batch(cursor, f'INSERT INTO "Subscribe" ("Price", "SubscribeName", "SubscribedUserID", "SubscribedGroupID")'
                          f'VALUES (%s, %s, %s, %s)',
                  [(round(random.uniform(7.00, 1000.00), 2),
                    name.word(),
                    None,
                    random.choice(group_id))
                   for i in range(int(count / 2))])


def generate_subscriber(cursor, user_id: list[int], subscribe_id: list[int], count: int):
    time = mimesis.Datetime()
    execute_batch(cursor, f'INSERT INTO "Subscriber" ("SubscriberID", "SubscribeID", "EndOfSubscribe") '
                          f'VALUES (%s, %s, %s)',
                  [(random.choice(user_id), random.choice(subscribe_id), time.date())
                   for i in range(count)])


def generate_post(cursor, group_id: list[int], author_id: list[int], count: int):
    picture = mimesis.File()
    description = mimesis.Text()
    time = mimesis.Datetime()

    execute_batch(cursor, f'INSERT INTO "Post" ('
                          f'"GroupID", "AuthorID", "Picture", "Description", "TimePosted", "IsDeleted")'
                          f'VALUES (%s, %s, %s, %s, %s, %s)',
                  [(random.choice(group_id),
                    None,
                    picture.file_name(),
                    description.sentence(),
                    time.date(),
                    bool(random.getrandbits(1)))
                   for i in range(int(count / 2))])
    execute_batch(cursor, f'INSERT INTO "Post" ('
                          f'"GroupID", "AuthorID", "Picture", "Description", "TimePosted", "IsDeleted")'
                          f'VALUES (%s, %s, %s, %s, %s, %s)',
                  [(None,
                    random.choice(author_id),
                    picture.file_name(),
                    description.sentence(),
                    time.date(),
                    bool(random.getrandbits(1)))
                   for i in range(int(count / 2))])


def generate_message(cursor, user_id: list[int], count: int):
    text = mimesis.Text()
    time = mimesis.Datetime()

    execute_batch(cursor, f'INSERT INTO "Message" ("Text", "AuthorID", "TimeSent", "IsDeleted", "Read")'
                          f'VALUES (%s, %s, %s, %s, %s)',
                  [(text.sentence(),
                    random.choice(user_id),
                    time.date(),
                    bool(random.getrandbits(1)),
                    bool(random.getrandbits(1)))
                   for i in range(count)])


def generate_like(cursor, user_id: list[int], post_id: list[int], count: int):
    execute_batch(cursor, f'INSERT INTO "Like" ("PostID", "UserID")'
                          f'VALUES (%s, %s)',
                  [(random.choice(post_id), random.choice(user_id))
                   for i in range(count)])


def generate_group_user_role(cursor, user_id: list[int], group_id: list[int], role_id: list[int], count: int):
    execute_batch(cursor, f'INSERT INTO "GroupUserRole" ("GroupID", "UserID", "UserRoleID")'
                          f'VALUES (%s, %s, %s)',
                  [(random.choice(group_id), random.choice(user_id), random.choice(role_id))
                   for i in range(count)])


def generate_dialog(cursor, counter: int):
    file = mimesis.File()
    text = mimesis.Text()
    execute_batch(cursor, f'INSERT INTO "Dialog" ("DialogName", "Logo")'
                          f'VALUES (%s, %s)',
                  [(text.word(), file.file_name())
                   for i in range(counter)])


def generate_dialog_user(cursor, user_id: list[int], dialog_id: list[int], count: int):
    execute_batch(cursor, f'INSERT INTO "DialogUser" ("DialogID", "UserID")'
                          f'VALUES (%s, %s)',
                  [((random.choice(dialog_id)), (random.choice(user_id)))
                   for i in range(count)])


def generate_dialog_message(cursor, dialog_id: list[int], message_id: list[int], count: int):
    execute_batch(cursor, f'INSERT INTO "DialogMessage" ("DialogID", "MessageID")'
                          f'VALUES (%s, %s)',
                  [(random.choice(dialog_id), random.choice(message_id))
                   for i in range(count)])


def generate_comment(cursor, post_id: list[int], user_id: list[int], counter: int):
    comment_id = list(range(0, counter))
    comment_id.append(None)
    comment = mimesis.Text()
    time = mimesis.Datetime()

    execute_batch(cursor, f'INSERT INTO "Comment" ("PostID", "UserID", "Comment", "TimePosted")'
                          f'VALUES (%s, %s, %s, %s)',
                  [(random.choice(post_id),
                    random.choice(user_id),
                    comment.sentence(),
                    time.date()
                    )
                   for i in range(counter)])


size = int(os.getenv('SIZE', default=10**6))
dbname = os.getenv('PG_DBNAME', default="postgres")
user = os.getenv('PG_USER', default="CapTof")
password = os.getenv('PG_PASSWORD', default="CapTof")
host = os.getenv('PG_HOST', default="localhost")
port = os.getenv('PG_PORT', default="5432")


with psycopg2.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}") as conn:
    with conn.cursor() as cur:
        print("Generator connected")
        cur_size = table_size(cur, "User")
        print("User generate started ")
        if cur_size >= size - 10 ** 3:
            print("No user generate needed")
        else:
            add_size = size - cur_size
            generate_user(cur, add_size)
            print("User generate done")
            conn.commit()

        users_id = get_id(cur, "User", "UserID")

        cur_size = table_size(cur, "ThemeOfADay")
        print("Theme of a day generate started")
        if cur_size >= 100:
            print("No theme of a day generate needed")
        else:
            add_size = 100 - cur_size
            generate_theme_of_a_day(cur, add_size)
            print("Theme of a day generate done")
            conn.commit()

        cur_size = table_size(cur, "Group")
        print("Group generate started")
        if cur_size >= (size//10):
            print("No group generate needed")
        else:
            add_size = int(size//10 - cur_size)
            generate_group(cur, add_size)
            print("Group generate done")
            conn.commit()
        groups_id = get_id(cur, "Group", "GroupID")

        cur_size = table_size(cur, "Role")
        print("Role generate started")
        if cur_size > 0:
            print("No role generate needed")
        else:
            generate_role(cur)
            print("Role generate done")
            conn.commit()
        roles_id = get_id(cur, "Role", "RoleID")

        cur_size = table_size(cur, "Subscribe")
        print("Subscribe generate started")
        if cur_size >= (size//100):
            print("No subscribe generate needed")
        else:
            add_size = int(size//100) - cur_size
            generate_subscribe(cur, users_id, groups_id, add_size)
            print("Subscribe generate done")
            conn.commit()
        subscribes_id = get_id(cur, "Subscribe", "SubscribeID")

        cur_size = table_size(cur, "Subscriber")
        print("Subscriber generate started")
        if cur_size >= (size//10):
            print("No subscriber generate needed")
        else:
            add_size = size//10 - cur_size
            generate_subscriber(cur, users_id, subscribes_id, add_size)
            print("Subscriber generate done")
            conn.commit()

        cur_size = table_size(cur, "Post")
        print("Post generate started")
        if cur_size >= size:
            print("No post generate needed")
        else:
            add_size = size - cur_size
            generate_post(cur, groups_id, users_id, add_size)
            print("Post generate done")
            conn.commit()
        posts_id = get_id(cur, "Post", "PostID")

        cur_size = table_size(cur, "Message")
        print("Message generate started")
        if cur_size >= size:
            print("No message generate needed")
        else:
            add_size = size - cur_size
            generate_message(cur, users_id, add_size)
            print("Message generate done")
            conn.commit()
        messages_id = get_id(cur, "Message", "MessageID")

        cur_size = table_size(cur, "Like")
        print("Like generate started")
        if cur_size >= size//100:
            print("No like generate needed")
        else:
            add_size = size//100 - cur_size
            generate_like(cur, users_id, posts_id, add_size)
            print("Like generate done")
            conn.commit()

        cur_size = table_size(cur, "GroupUserRole")
        print("GroupUserRole generate started")
        if cur_size >= (size//100):
            print("No group-user-role generate needed")
        else:
            add_size = size//100 - cur_size
            generate_group_user_role(cur, users_id, groups_id, roles_id, add_size)
            print("GroupUserRole generate done")
            conn.commit()

        cur_size = table_size(cur, "Dialog")
        print("Dialog generate started")
        if cur_size >= size:
            print("No dialog generate needed")
        else:
            add_size = size - cur_size
            generate_dialog(cur, add_size)
            print("Dialog generate done")
            conn.commit()

        dialogs_id = get_id(cur, "Dialog", "DialogID")

        cur_size = table_size(cur, "DialogUser")
        print("DialogUser generate started")
        if cur_size >= (size//10):
            print("No dialog-user generate needed")
        else:
            add_size = size//10 - cur_size
            generate_dialog_user(cur, users_id, dialogs_id, add_size)
            print("Dialog-user generate done")
            conn.commit()

        cur_size = table_size(cur, "DialogMessage")
        print("DialogMessage generate started")
        if cur_size >= size//1000:
            print("No dialog-message generate needed")
        else:
            add_size = size//1000 - cur_size
            generate_dialog_message(cur, dialogs_id, messages_id, add_size)
            print("Dialog-message generate done")
            conn.commit()

        cur_size = table_size(cur, "Comment")
        print("Comment  generate started")
        if cur_size >= 100:
            print("No comment generate needed")
        else:
            add_size = 100 - cur_size
            generate_comment(cur, users_id, posts_id, add_size)
            print("Comment generate done")
            conn.commit()
        print("___All generations done___")
