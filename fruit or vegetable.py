fruit_or_vegetable = str(input())

switcher = {
    "banana": "fruit",
    "apple": "fruit",
    "tomato": "vegetable",
    "cherry": "fruit",
    "kiwi": "fruit",
    "lemon": "fruit",
    "grapes": "fruit",
    "cucumber": "vegetable",
    "pepper": "vegetable",
    "carrot": "vegetable",
}

print(switcher.get(fruit_or_vegetable, "unknown"))
