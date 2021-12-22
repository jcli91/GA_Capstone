from flask_app.config.mysqlconnection import query_db
from flask import Flask
# from flask_app.models import journal

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
    
    @classmethod
    def add_food_to_day(cls,data):
        query = "INSERT INTO food_by_date (journal_id, food_id) VALUES (%(journal_id)s, %(food_id)s)"
        results = query_db(query, data)
        return results
    
    @classmethod
    def deletefoodfromday(cls, data):
        query1 = "DELETE FROM food_by_date WHERE food_id = %(id)s LIMIT 1"
        return query_db(query1,data)
        
    @classmethod
    def deletefood(cls, data):
        query = "DELETE FROM food WHERE id = %(id)s"
        return query_db(query, data)
    
    @classmethod
    def foodlist(cls):
        query = "SELECT * FROM food"
        results = query_db(query)
        foodlist = []
        for food1 in results:
            foodlist.append(cls(food1))
        return foodlist
    
    @classmethod
    def onefood(cls, data):
        query = "SELECT * FROM food WHERE id = %(id)s"
        results = query_db(query, data)
        food = cls(results[0])
        return food
    
    @classmethod
    def updatefood(cls, data):
        query = "UPDATE food SET category = %(category)s, name = %(name)s, calories = %(calories)s WHERE id = %(id)s"
        results = query_db(query, data)
        print(results)
        # food = cls(results)
        
        
        
        
        
        
    
        
    
        
        
    
    