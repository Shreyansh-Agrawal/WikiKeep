from typing import Tuple

from database.connection import get_connection


class DatabaseHelper:

    async def read(self, query: str, params: Tuple = None, fetch_one: bool = False):
        connection = await get_connection()
        try:
            if fetch_one:
                row = (
                    await connection.fetchrow(query, *params)
                    if params
                    else await connection.fetchrow(query)
                )
                return dict(row) if row else None

            rows = (
                await connection.fetch(query, *params)
                if params
                else await connection.fetch(query)
            )
            return [dict(row) for row in rows]

        finally:
            await connection.close()

    async def write(self, query: str, params: Tuple = None):
        connection = await get_connection()
        try:
            if params:
                await connection.execute(query, *params)
            else:
                await connection.execute(query)

        finally:
            await connection.close()
