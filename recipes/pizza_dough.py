from datetime import timedelta
from common import Recipe

recipe = Recipe(
    title="Pizza Dough",
    subtitle="A simple honey-sweetened pizza dough. Cook time refers to waiting while rising/waking the yeast.",
    prep_time=timedelta(minutes=15),
    cook_time=timedelta(hours=2, minutes=10),
    ingredients=[
        "1 packet active dry yeast (2 1/4 teaspoons)",
        "3/4 cup warm water (100°F to 110°F)",
        "2 1/2 tablespoons honey",
        "2 cups flour",
        "~3 tablespoons olive oil",
    ],
    instructions=[
        "Using a meat thermometer, verify that the water is between 100°F and 110°F.",
        "In a medium mixing bowl, add active dry yeast, water, and honey. Mix well with a fork.",
        "Wait for 10 minutes. The mixture should now be frothy/bubbly if the yeast is working.",
        "Add flour and mix well, using your fork to press/pat the clumps together into a ball.",
        "Add a small amount of olive oil and use your fork to continue pressing the dough into a ball while spreading the olive oil around.",
        "Flip the dough ball as best as you can; it may be a bit loose. Add some olive oil and repeat the previous step on this side.",
        "Cover the mixing bowl with plastic wrap, a bag, or a lid to prevent the dough from drying out while rising.",
        "Wait 1 hour while the dough rises.",
        "Uncover the bowl and add a small amount of olive oil to coat the dough and prevent your hands from sticking.",
        "Knead the dough, and work it more into a ball shape. Return the dough to the mixing bowl and cover again.",
        "Wait 1 hour while the dough rises.",
        "The dough is now ready for use, but if preferred, you can extend or add additional rising and kneading cycles.",
        "* While the recipe suggests 1-hour waits, these can be lengthened to 2 hours if you have the time. The provided times are minimums for good results."
    ]
)
