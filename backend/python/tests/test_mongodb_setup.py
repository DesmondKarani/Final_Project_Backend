# test_mongodb_setup.py
import unittest
from mongodb_setup import connect_to_mongodb, setup_mongodb

class TestMongoDBSetup(unittest.TestCase):
    def setUp(self):
        self.client = connect_to_mongodb()
        self.db = self.client['test_citation_database']

    def test_connection(self):
        self.assertIsNotNone(self.client)

    def test_setup_mongodb(self):
        db = setup_mongodb('test_citation_database')
        self.assertIsNotNone(db)
        self.assertTrue('citation_styles' in db.list_collection_names())
        self.assertTrue('saved_citations' in db.list_collection_names())

        # Check if APA7 style was inserted
        apa7_style = db.citation_styles.find_one({"name": "APA7"})
        self.assertIsNotNone(apa7_style)

    def tearDown(self):
        self.client.drop_database('test_citation_database')
        self.client.close()

if __name__ == '__main__':
    unittest.main()
