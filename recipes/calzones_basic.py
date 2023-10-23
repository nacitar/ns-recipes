from datetime import timedelta
from common import Recipe

recipe = Recipe(
    title="Basic Calzones",
    subtitle="A great meal your family can customize to each person's preferences.",
    prep_time=timedelta(minutes=20),
    cook_time=timedelta(minutes=25),
    ingredients=[
        "1 ball of pizza dough",
        "1 cup yellow cornmeal",
        "1/2 cup flour",
        "1/2 tablespoon olive oil (if dough is sticky)",
        "* your choice of cheeses and toppings",
        "* your choice of pizza sauce for dipping",
    ],
    instructions = [
        "Clean a large, flat surface for rolling the dough, such as a smooth countertop.",
        "On this surface, mix yellow cornmeal and flour thoroughly, piling it up in the center of the surface.",
        "If the dough isn't slightly oily from its preparation, lightly coat it with olive oil using your hands. This helps prevent sticking.",
        "Place the dough ball in the center of the cornmeal and flour mixture. Turn it over to ensure both sides are coated.",
        "Roll the dough into a thin, rectangular shape using a rolling pin. Apply gentle pressure, avoiding too much force. Fix any breaks with your hands.",
        "With the serrated edge of a butter knife, gently cut out rectangular pieces from the dough. These will be used for the calzones.",
        "Spray a pan with non-stick cooking spray and transfer the dough rectangles onto it.",
        "On <b><u>just under half</u></b> of each rectangle, layer your ingredients. Start with cheese, add your toppings, and finish with another layer of cheese to bind everything.",
        "Fold the dough over to encase the toppings. Press the edged together, trimming any excess dough. Use these scraps to patch any thin spots or holes.",
        "Bake in a preheated oven at 400°F for 25 minutes.",
        "Remove from oven, slice into preferred portions, and serve with pizza sauce.",
    ]
)
