#### Readme by Jeffery Li

- Calorie Tracker is an application that tracks the foods you've eaten and their calories.

## User Stories

- Users will be able to;
- Add a date.
- Inside each date you can add food with a category, name, and calories.
- Edit a specific food.
- View food you've eaten from another day and add them to current day.
- Delete food.
- Delete date.
- View total calories for that particular day.


## Models

- Journal model
```class Journal:
    def __init__(self, data):
        self.id = data["id"]
        self.date = data["date"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
```

- Food model
```class Food:
    def __init__(self, data):
        self.id = data["id"]
        self.category = data["category"]
        self.name = data["name"]
        self.calories = data["calories"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
```


## Controllers

- Journal

| url | method | action |
|-----|--------|--------|
| / | get | display dates|
| /newentry | get | displays new entry form to add date|
| /addentry | post | posts new date |
| /dates/<int:id>| get | displays specific date |
| /delete_day/<int:id> | destroy | deletes a date |



- Food

| url | method | action |
|-----|--------|--------|
| /newfood/<int:journal_id> | post | post food to day|
| /foods/remove/<int:id>/<int:journal_id> | destroy | removes food from current day |
| /foods/delete/<int:id>/<int:journal_id> | destroy | removes food from history
| /foods/add_to_day/<int:food_id>/<int:journal_id>| post | post food to history |
| /foods/edit/<int:id>/<int:journal_id> | edit | displays food edit form |
| /foods/edit/<int:id>/<int:journal_id> | post | updates data entered in edit form|



## Technologies
- Python
- Flask
- MySQL(PyMySQL)
- HTML/CSS
- Bootstrap
