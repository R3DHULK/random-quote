import random

quotes = [
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "If you want to live a happy life, tie it to a goal, not to people or things.",
    "The only way to do great work is to love what you do."
]

def get_random_quote():
    return random.choice(quotes)

print(get_random_quote())
