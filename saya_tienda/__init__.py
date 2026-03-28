import pymysql

# Allow Django's MySQL backend to work without mysqlclient.
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb()
