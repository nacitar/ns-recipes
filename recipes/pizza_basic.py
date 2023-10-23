from datetime import timedelta
from common import Recipe

recipe = Recipe(
    title="Basic Pizza",
    subtitle="A classic staple.",
    prep_time=timedelta(minutes=10),
    cook_time=timedelta(minutes=25),
    ingredients=[
        "1 ball of pizza dough",
        "1 cup yellow cornmeal",
        "1/2 cup flour",
        "1/2 tablespoon olive oil (if dough is sticky)",
        "* your choice of cheeses and toppings",
        "* your choice of pizza sauce",
    ],
    instructions = [
        "Clean a large, flat surface for rolling the dough, such as a smooth countertop.",
        "On this surface, mix yellow cornmeal and flour thoroughly, piling it up in the center of the surface.",
        "If the dough isn't slightly oily from its preparation, lightly coat it with olive oil using your hands. This helps prevent sticking.",
        "Place the dough ball in the center of the cornmeal and flour mixture. Turn it over to ensure both sides are coated.",
        "Roll the dough out thin with a rolling pin. Apply gentle pressure, avoiding too much force. Fix any breaks with your hands.",
        "Gently trace and cut your desired pan shape from the dough using the serrated edge of a butter knife.",
        "Spray a pan with non-stick cooking spray and transfer the dough onto it.",
        "Spread your chosen pizza sauce evenly over the dough, followed by your desired toppings.",
        "Bake in a preheated oven at 400°F for 25 minutes.",
        "Remove from oven, cut into slices, and serve.",
        "* Any leftover dough can be repurposed for additional pizzas or calzones."
    ]
)
