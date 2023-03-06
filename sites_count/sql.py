"""Communicate with atoll via sql."""

import os

import cx_Oracle


class NetworkLive(object):
    """Object represintation of communicating with Network live db."""

    def __init__(self, sql_selects: dict):
        """
        Construct a new network live object.

        Args:
            sql_selects: sql commands to get data by technologies
        """
        for tech, sql_command in sql_selects.items():
            setattr(self, tech, sql_command)

    def execute_sql(self, sql_type: str, table: str):
        """
        Execute sql command in Network live db.

        Args:
            sql_type: type of sql command - select or insert
            table: table type by technology

        Returns:
            list
        """
        atoll_dsn = cx_Oracle.makedsn(
            os.getenv('ATOLL_HOST'),
            os.getenv('ATOLL_PORT'),
            service_name=os.getenv('SERVICE_NAME'),
        )
        with cx_Oracle.connect(
            user=os.getenv('ATOLL_LOGIN'),
            password=os.getenv('ATOLL_PASSWORD'),
            dsn=atoll_dsn,
        ) as connection:
            cursor = connection.cursor()
            if sql_type == 'select':
                select_commands = {
                    'gsm': self.gsm_select,
                    'wcdma': self.wcdma_select,
                }
                cursor.execute(select_commands[table])
                return cursor.fetchall()
            elif sql_type == 'insert':
                pass
