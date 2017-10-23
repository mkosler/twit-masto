from psycopg2 import sql


class Repository:
    '''
    Base repository
    '''

    def __init__(self, table_name, connection):
        self.table_name = table_name
        self.connection = connection

    def get_all(self, queries=None):
        with self.connection.cursor() as curs:
            curs.execute(self._compose_query(queries), list(queries.values()))
            self.connection.commit()
            return curs.fetchall()

    def get_by_id(self, id):
        with self.connection.cursor() as curs:
            curs.execute(self._compose_query({'id': id}), (id,))
            self.connection.commit()
            return curs.fetchone()

    def insert(self, data):
        with self.connection.cursor() as curs:
            curs.execute(self._compose_insert_query(data), data)
            self.connection.commit()
            return curs.fetchone()

    def update(self, data):
        with self.connection.cursor() as curs:
            curs.execute(self._compose_update_query(data), data)
            self.connection.commit()

    def _compose_query(self, query):
        base = sql.SQL('SELECT * FROM {}').format(
            sql.Identifier(self.table_name)
        )
        if query:
            base += sql.SQL(' WHERE {}').format(sql.SQL(' AND ').join([
                sql.SQL('{} = %s').format(sql.Identifier(k)) for k in query
            ]))
        return base + sql.SQL(';')

    def _compose_insert_query(self, data):
        return sql.SQL(
            'INSERT INTO {} ({}) VALUES ({}) RETURNING *;'
        ).format(
            sql.Identifier(self.table_name),
            sql.SQL(', ').join([sql.Identifier(k) for k in data]),
            sql.SQL(', ').join([sql.SQL(f'%({k})s') for k in data])
        )

    def _compose_update_query(self, data):
        return sql.SQL(
            'UPDATE {} SET {} WHERE "id" = %(id)s;'
        ).format(
            sql.Identifier(self.table_name),
            sql.SQL(', ').join([
                sql.SQL('{} = {}').format(
                    sql.Identifier(k),
                    sql.SQL(f'%({k})s')
                ) for k in data
            ])
        )
