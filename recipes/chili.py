from datetime import timedelta
from generator import Recipe

recipe = Recipe(
    title="Family-Favorite Chili with Hidden Veggies",
    subtitle="A hearty and delicious chili the whole family will love!",
    prep_time=timedelta(minutes=20),
    cook_time=timedelta(hours=2, minutes=30),
    ingredients=[
        "1 large zucchini, chopped",
        "1 large red bell pepper, chopped",
        "2 tbsp paprika"
    ],
    instructions=[
        "In a large pot or enameled dutch oven, sauté onion..."
    ]
)
