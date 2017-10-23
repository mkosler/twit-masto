from server.models.repo import Repository


class TweetRepository(Repository):
    '''
    Tweet table repository
    '''

    def __init__(self, connection):
        super().__init__('tweet', connection)
