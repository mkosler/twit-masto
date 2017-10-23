from server.models.repo import Repository


class TwitterUserRepository(Repository):
    '''
    Twitter users table repository
    '''

    def __init__(self, connection):
        super().__init__('twitter_user', connection)
