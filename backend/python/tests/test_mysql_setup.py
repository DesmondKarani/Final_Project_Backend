# test_mysql_setup.py
import unittest
import mysql.connector
from mysql_setup import connect_to_mysql, setup_mysql

class TestMySQLSetup(unittest.TestCase):
    def setUp(self):
        self.db = connect_to_mysql()
        self.cursor = self.db.cursor()

    def test_connection(self):
        self.assertIsNotNone(self.db)

    def test_setup_mysql(self):
        db = setup_mysql('test_citation_system')
        self.assertIsNotNone(db)

        # Check if tables were created
        self.cursor.execute("SHOW TABLES")
        tables = [table[0] for table in self.cursor.fetchall()]
        self.assertIn('users', tables)
        self.assertIn('saved_citations', tables)

        # Check if sample data was inserted
        self.cursor.execute("SELECT * FROM users WHERE username = 'sample_user'")
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)

        self.cursor.execute("SELECT * FROM saved_citations WHERE style_name = 'APA7'")
        citation = self.cursor.fetchone()
        self.assertIsNotNone(citation)

    def tearDown(self):
        self.cursor.execute("DROP DATABASE IF EXISTS test_citation_system")
        self.db.close()

if __name__ == '__main__':
    unittest.main()
