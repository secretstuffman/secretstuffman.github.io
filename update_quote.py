import random

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are."
]

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_html = html.replace("<!--QUOTE-->", random.choice(quotes))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)
