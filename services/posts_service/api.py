
posts = [
    {
        "id":1,
        "title": "Buy Grocergies",
        "description": "Milk, Eggs, Cheese",
        "done": False
    }
]

def get_posts():
    return posts

def add_post(new_post):
    posts.append(new_post)