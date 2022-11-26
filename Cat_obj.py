from Cat import Cat

cats = [
    {
     "name": "Васька",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Мурка",
     "gender": "девочка",
     "age": 1,
    },
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)