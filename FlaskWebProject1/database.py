from flask_mysqldb import MySQL

class MYSQLinstance:
    _instance = None

    @staticmethod
    def get_instance(app=None):
        if MYSQLinstance._instance is None:
            MYSQLinstance._instance = MySQL(app)
        return MYSQLinstance._instance
