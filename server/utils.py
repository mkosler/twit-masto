from psycopg2 import sql


def get_all(curs, table_name, query=None):
    curs.execute(compose_query(table_name, query), list(query.values()))
    return curs.fetchall()


def compose_query(table_name, keys):
    base = sql.SQL('SELECT * FROM {}').format(sql.Identifier(table_name))
    if keys:
        base += sql.SQL(' WHERE ')
        base += sql.SQL(' AND ').join(
            [sql.SQL('{} = %s').format(sql.Identifier(k)) for k in keys]
        )
    return base + sql.SQL(';')
