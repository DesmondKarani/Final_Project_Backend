# mongodb_setup.py
from pymongo import MongoClient

def connect_to_mongodb(uri='mongodb://localhost:27017/'):
    return MongoClient(uri)

def setup_mongodb(db_name='citation_database'):
    client = connect_to_mongodb()
    db = client[db_name]
    citation_styles = db['citation_styles']
    saved_citations = db['saved_citations']
    
    apa7_style = {
        "name": "APA7",
        "fields": [
            {"name": "author", "required": True},
            {"name": "year", "required": True},
            {"name": "title", "required": True},
            {"name": "source", "required": True},
            {"name": "doi", "required": False}
        ],
        "format": "{author}. ({year}). {title}. {source}. {doi}"
    }
    
    citation_styles.insert_one(apa7_style)
    return db

if __name__ == "__main__":
    setup_mongodb()
    print("MongoDB setup complete.")
