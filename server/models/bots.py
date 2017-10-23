from server.models.repo import Repository


class BotRepository(Repository):
    '''
    Bot table repository
    '''

    def __init__(self, connection):
        super().__init__('bot', connection)
