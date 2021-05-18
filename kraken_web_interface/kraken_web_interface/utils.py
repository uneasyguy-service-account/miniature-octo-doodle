from aiomysql.cursors import DictCursor

from kraken_web_interface.kraken_web_interface.settings import db


class DBExecute(object):
    def __init__(self, sql: str, params=None, return_type='tuple'):
        """
                  Execute the sql of the study database
                  :param sql: sql statement
                  :param params: sql parameters
                  :param return_type: data type returned
        """
        self.sql = sql
        self.params = params
        self.return_type = return_type

    async def fetchone(self) -> (tuple, dict):
        async with await db.study_engine.acquire() as conn:  # type: aiomysql.connection.Connection
            if self.return_type == 'dict':
                async with conn.cursor(DictCursor) as cur:
                    if self.params is None:
                        await cur.execute(self.sql)
                    else:
                        await cur.execute(self.sql, self.params)
                    rel = await cur.fetchone()  # type: dict
            else:
                async with conn.cursor() as cur:  # type: aiomysql.cursors.Cursor
                    if self.params is None:
                        await cur.execute(self.sql)
                    else:
                        await cur.execute(self.sql, self.params)
                    rel = await cur.fetchone()  # type: tuple
        db.study_engine.release(conn)
        return rel

    async def fetchall(self) -> list:
        async with await db.study_engine.acquire() as conn:  # type: aiomysql.connection.Connection
            if self.return_type == 'dict':
                async with conn.cursor(DictCursor) as cur:  # type: aiomysql.cursors.Cursor
                    if self.params is None:
                        await cur.execute(self.sql)
                    else:
                        await cur.execute(self.sql, self.params)
                    rel = await cur.fetchall()
            else:
                async with conn.cursor() as cur:  # type: aiomysql.cursors.Cursor
                    if self.params is None:
                        await cur.execute(self.sql)
                    else:
                        await cur.execute(self.sql, self.params)
                    rel = await cur.fetchall()
        db.study_engine.release(conn)
        return rel