from flask_app.config.mysqlconnection import query_db
from flask import Flask

app = Flask(__name__)

class Food:
    def __init__(self, data):
        self.id = data["id"]
        self.category = data["category"]
        self.name = data["name"]
        self.calories = data["calories"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
    
    @classmethod
    def insert(cls, data):
        query = "INSERT INTO food (category, name, calories) VALUES (%(category)s, %(name)s, %(calories)s)"
        results = query_db(query, data)
        return results
    
        
    
        
        
    
    