from datetime import timedelta
from common import Recipe

recipe = Recipe(
    title="Classic Chili",
    subtitle="A simple, easy-to-make chili.",
    prep_time=timedelta(minutes=10),
    cook_time=timedelta(minutes=25),
    ingredients=[
        "1 pound ground beef",
        "1 (8 once) can tomato sauce",
        "1 (6 ounce) can tomato paste",
        "1 (14.5 ounce) can petite diced tomatoes (with their juice)",
        "2 (16 ounce) cans red kidney beans (drained and rinsed)",
        "1 1/2 cups beef broth (or substitute water)",
        "2 1/2 tablespoons chili powder",
        "2 tablespoons ground cumin",
        "1 tablespoon onion powder",
        "1 tablespoon garlic powder",
        "1 teaspoon salt",
        "1/2 teaspoon ground black pepper",
        "1/2 teaspoon ground cayenne pepper",
        "(on the side) El Yucateco XXXtra Hot Sauce Chile Habanero"
    ],
    instructions=[
        "Brown the ground beef in a skillet. Drain fat and return to skillet.",
        "Add all of the ingredients to the skillet. Stir until well combined.",
        "Bring to a low boil, reduce the heat, and simmer uncovered for 25 minutes, stirring occasionally.",
        "Remove from heat. Let rest for 10 minutes before serving.  Add El Yucateco as desired.",
    ]
)
