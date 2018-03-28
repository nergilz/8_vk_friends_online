import vk
import getpass
from vk.exceptions import VkException


APP_ID = 6421852


def get_user_login():
    user_login = input(' input user login: ')
    return user_login


def get_user_password():
    user_password = getpass.getpass(' input user password: ')
    return user_password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_online = api.users.get(
        user_ids=api.friends.getOnline(v=5.73),
        v=5.73
    )
    return friends_online


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        friends_online = get_online_friends(login, password)
        output_friends_to_console(friends_online)
    except VkException:
        print(' ERROR: incorrect password or login!')
