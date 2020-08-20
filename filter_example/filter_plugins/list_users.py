def list_users(users_list, key, value=True):
    ''' List the users that meet some criteria

    Args:
        user_list: dictionary of users.
        key: the key to be filter by.
        value: the expected value for that key.
    Returns:
        The list of names for all the users that met
        that criteria.
    '''

    usernames_list = []
    for user in users_list:
        if key in user and user[key] == value:
            usernames_list.append(user['name'])

    return usernames_list


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        ''' Add the filter to the list of filters '''
        
        return {
            # Name of the filter : Name of the function to be called
            'list_users': list_users
        }
