from flask_app.config.mysqlconnection import query_db
from flask import Flask
from flask_app.models import food

app = Flask(__name__)

class Journal:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
    
    @property
    def foods(self):
        query = f"SELECT * FROM food JOIN food_by_date ON food.id = food_by_date.food_id JOIN journals ON food_by_date.journal_id = journals.id WHERE journals.id = {self.id}"
        results = query_db(query)
        print(results)
        foods = []
        for food1 in results:
            foods.append(food.Food(food1))
        return foods
    
    @property
    def total_calories(self):
        query = f"SELECT * FROM food JOIN food_by_date ON food.id = food_by_date.food_id JOIN journals ON food_by_date.journal_id = journals.id WHERE journals.id = {self.id}"
        results = query_db(query)
        total_calories = 0
        for food1 in results:
            total_calories += food1["calories"]
        return total_calories
        
    
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
    
    @classmethod
    def delete_by_id(cls, data):
        query1 = "DELETE FROM food_by_date WHERE journal_id = %(id)s"
        query_db(query1,data)
        query2 = "DELETE FROM journals WHERE id = %(id)s"
        return query_db(query2, data)

    
        
