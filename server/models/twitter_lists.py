from server.models.repo import Repository


class TwitterListRepository(Repository):
    '''
    Twitter list table repository
    '''

    def __init__(self, connection):
        super().__init__('twitter_list', connection)
