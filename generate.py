#!/usr/bin/env python3
import os
import importlib.util
from typing import Dict
from pathlib import Path
from dataclasses import dataclass
from datetime import timedelta
from string import Template
from common import Recipe

from datetime import timedelta

def timedelta_to_str(td: timedelta) -> str:
    days, remainder = divmod(td.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    result = []
    if days:
        result.append(f"{int(days)} day{'s' if days != 1 else ''}")
    if hours:
        result.append(f"{int(hours)} hour{'s' if hours != 1 else ''}")
    if minutes:
        result.append(f"{int(minutes)} min{'s' if minutes != 1 else ''}")
    if not days and not hours and not minutes:
        result.append(f"{int(seconds)} sec{'s' if seconds != 1 else ''}")
    return " ".join(result)

def render_to_html(recipe: Recipe) -> str:
    with open("template.html", "r") as f:
        template = Template(f.read())
    return template.substitute(
        title=recipe.title,
        subtitle=recipe.subtitle,
        prep_time=timedelta_to_str(recipe.prep_time),
        cook_time=timedelta_to_str(recipe.cook_time),
        total_time=timedelta_to_str(recipe.prep_time + recipe.cook_time),
        ingredients='\n'.join([f"<li>{item}</li>" for item in recipe.ingredients]),
        instructions='\n'.join([f"<li>{item}</li>" for item in recipe.instructions])
    )

def load_recipes_from_folder(folder: str) -> Dict[str, Recipe]:
    recipes = {}

    # Ensure all .py files are sorted alphabetically by filename
    files = sorted([f for f in Path(folder).glob("*.py")])

    for file in files:
        module_name = os.path.splitext(os.path.basename(file))[0]

        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Assuming the recipe is stored in a variable named "recipe" in each .py file
        recipes[module_name] = module.recipe

    return recipes

def main():
    recipes = load_recipes_from_folder("recipes")
    output_dir = "docs"
    with open(f"{output_dir}/index.html", "w") as index:
        index.write("<h1>Recipes Index</h1>\n<ul>\n")
        for module_name, recipe in recipes.items():
            filename = f"{module_name}.html"
            with open(f"{output_dir}/{filename}", "w") as f:
                f.write(render_to_html(recipe))
            index.write(f'<li><a href="{filename}">{recipe.title}</a></li>\n')
        index.write("</ul>")

if __name__ == "__main__":
    main()
