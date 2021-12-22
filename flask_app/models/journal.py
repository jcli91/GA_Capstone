from flask_app.config.mysqlconnection import query_db
from flask import Flask

app = Flask(__name__)

class Journal:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
    
    @property
    def foods(self):
        query = f"SELECT * FROM food JOIN food_by_date ON food.id = food_by_date.food_id JOIN journals ON food_by_date.journal_id = journals.id WHERE date = {self.date}"
    
    @classmethod
    def add_day(cls, data):
        query = "INSERT INTO journals (date) VALUES (%(date)s)"
        results = query_db(query, data)
        return results
    
    @classmethod
    def show_days(cls):
        query = "SELECT * FROM journals"
        results = query_db(query)
        days = []
        for day in results:
            days.append(cls(day))
        return days
    
    @classmethod
    def show_day(cls, data):
        print(data)
        query = "SELECT * FROM journals WHERE id = %(id)s"
        results = query_db(query, data)
        day = cls(results[0])
        return day
    
        
