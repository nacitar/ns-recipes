from datetime import timedelta
from common import Recipe

recipe = Recipe(
    title="Pizza Sauce",
    subtitle="A delicious honey-sweetened pizza sauce.",
    prep_time=timedelta(minutes=10),
    cook_time=timedelta(minutes=30),
    ingredients=[
        "1 (15 once) can tomato sauce",
        "1 (6 ounce) can tomato paste",
        "4 tablespoons honey",
        "4 tablespoons parmesan cheese",
        "2 tablespoons water",
        "1/2 tablespoon oregano flakes",
        "1/2 teaspoon garlic powder",
        "1/2 teaspoon onion powder",
        "1/2 teaspoon ground paprika",
        "1/4 teaspoon red pepper flakes",
        "1/4 teaspoon black pepper",
        "1/4 teaspoon white pepper",
    ],
    instructions=[
        "Bring to a low boil, reduce to medium heat, and simmer covered for 15 minutes, stirring occasionally.",
        "Remove from heat. Let rest for 10 minutes before serving.",
    ]
)
