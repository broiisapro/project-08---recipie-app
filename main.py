import tkinter as tk
from tkinter import messagebox
import json

# Recipe data from the user (provided JSON data)
recipes_data = [
    {
        "name": "spaghetti bolognese",
        "image": "https://example.com/spaghetti.jpg",
        "ingredients": [
            "400g spaghetti",
            "2 tbsp olive oil",
            "1 onion, finely chopped",
            "2 garlic cloves, minced",
            "400g ground beef",
            "800g canned tomatoes",
            "2 tbsp tomato paste",
            "1 tsp sugar",
            "Salt and pepper to taste",
            "Grated Parmesan cheese"
        ],
        "procedure": [
            "Cook the spaghetti according to the package instructions.",
            "Heat olive oil in a pan and sauté onion and garlic until soft.",
            "Add ground beef and cook until browned.",
            "Stir in canned tomatoes, tomato paste, and sugar. Simmer for 15-20 minutes.",
            "Season with salt and pepper.",
            "Serve the sauce over the spaghetti and top with Parmesan cheese."
        ]
    },
    {
        "name": "chocolate cake",
        "image": "https://example.com/chocolate_cake.jpg",
        "ingredients": [
            "1 3/4 cups all-purpose flour",
            "3/4 cup cocoa powder",
            "2 cups sugar",
            "1 1/2 tsp baking soda",
            "1 1/2 tsp baking powder",
            "1 tsp salt",
            "2 large eggs",
            "1 cup whole milk",
            "1/2 cup vegetable oil",
            "2 tsp vanilla extract",
            "1 cup boiling water"
        ],
        "procedure": [
            "Preheat the oven to 350°F (175°C). Grease and flour two 9-inch round baking pans.",
            "Combine dry ingredients in a large bowl.",
            "Add eggs, milk, oil, and vanilla. Beat on medium speed for 2 minutes.",
            "Stir in boiling water (batter will be thin).",
            "Pour batter into prepared pans and bake for 30-35 minutes.",
            "Cool for 10 minutes before removing from pans. Frost as desired."
        ]
    },
    {
        "name": "vegetable stir-fry",
        "image": "https://example.com/vegetable_stir_fry.jpg",
        "ingredients": [
            "2 tbsp vegetable oil",
            "1 onion, sliced",
            "2 garlic cloves, minced",
            "1 cup broccoli florets",
            "1 cup bell peppers, sliced",
            "1 cup carrots, julienned",
            "1/4 cup soy sauce",
            "2 tbsp oyster sauce",
            "1 tsp cornstarch dissolved in 2 tbsp water",
            "Cooked rice or noodles (optional)"
        ],
        "procedure": [
            "Heat oil in a wok or large skillet over high heat.",
            "Add onion and garlic and stir-fry for 1 minute.",
            "Add broccoli, bell peppers, and carrots. Stir-fry for 3-5 minutes.",
            "Mix soy sauce, oyster sauce, and cornstarch mixture. Add to the pan.",
            "Cook until the sauce thickens and coats the vegetables.",
            "Serve over rice or noodles, if desired."
        ]
    },
    {
        "name": "banana bread",
        "image": "https://example.com/banana_bread.jpg",
        "ingredients": [
            "2-3 ripe bananas, mashed",
            "1/3 cup melted butter",
            "1 cup sugar",
            "1 egg, beaten",
            "1 tsp vanilla extract",
            "1 tsp baking soda",
            "Pinch of salt",
            "1 1/2 cups all-purpose flour"
        ],
        "procedure": [
            "Preheat oven to 350°F (175°C). Grease a 4x8-inch loaf pan.",
            "In a mixing bowl, combine mashed bananas and melted butter.",
            "Stir in sugar, egg, and vanilla.",
            "Sprinkle baking soda and salt over the mixture. Mix in.",
            "Add the flour and stir until just incorporated.",
            "Pour the batter into the prepared loaf pan.",
            "Bake for 60 minutes or until a tester comes out clean.",
            "Cool before slicing and serving."
        ]
    },
    {
        "name": "classic grilled cheese",
        "image": "https://example.com/grilled_cheese.jpg",
        "ingredients": [
            "2 slices of bread",
            "2 slices of cheese (cheddar, American, or Swiss)",
            "1-2 tbsp butter"
        ],
        "procedure": [
            "Butter one side of each slice of bread.",
            "Place one slice, buttered side down, in a skillet over medium heat.",
            "Top with cheese slices and the other bread slice, buttered side up.",
            "Cook until golden brown on one side, about 3-4 minutes.",
            "Flip and cook the other side until golden brown and cheese is melted.",
            "Serve hot."
        ]
    },
    {
        "name": "chicken curry",
        "image": "https://example.com/chicken_curry.jpg",
        "ingredients": [
            "2 tbsp vegetable oil",
            "1 onion, diced",
            "2 garlic cloves, minced",
            "1 tbsp ginger, minced",
            "2 tbsp curry powder",
            "1 lb chicken breast, cut into cubes",
            "1 can (14 oz) coconut milk",
            "1 cup chicken broth",
            "1 tsp salt",
            "1/2 tsp pepper",
            "Cilantro for garnish (optional)"
        ],
        "procedure": [
            "Heat oil in a pot over medium heat. Sauté onion, garlic, and ginger until fragrant.",
            "Add curry powder and stir for 1 minute.",
            "Add chicken and cook until lightly browned.",
            "Pour in coconut milk and chicken broth. Season with salt and pepper.",
            "Simmer for 20 minutes, stirring occasionally.",
            "Garnish with cilantro and serve with rice or naan."
        ]
    }
]

# Function to search for a recipe in the loaded data
def search_recipe():
    recipe_name = recipe_name_entry.get().strip().lower()
    if not recipe_name:
        messagebox.showerror("Input Error", "Please enter a recipe name.")
        return
    
    recipe_found = False
    for recipe in recipes_data:
        if recipe["name"].lower() == recipe_name:
            display_recipe(recipe)
            recipe_found = True
            break
    
    if not recipe_found:
        messagebox.showerror("Recipe Not Found", f"No recipe found for '{recipe_name}'.")

# Function to display the recipe in the result text box
def display_recipe(recipe):
    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, f"Recipe: {recipe['name']}\n\n")
    
    result_text.insert(tk.END, "Ingredients:\n")
    for ingredient in recipe["ingredients"]:
        result_text.insert(tk.END, f"- {ingredient}\n")
    
    result_text.insert(tk.END, "\nProcedure:\n")
    for step in recipe["procedure"]:
        result_text.insert(tk.END, f"{step}\n")

# Create the main window for the app
root = tk.Tk()
root.title("Recipe Finder")

# Create and pack the widgets for the GUI
title_label = tk.Label(root, text="Recipe Finder", font=("Arial", 20))
title_label.pack(pady=10)

search_label = tk.Label(root, text="Enter Recipe Name:", font=("Arial", 12))
search_label.pack(pady=5)

recipe_name_entry = tk.Entry(root, font=("Arial", 14), width=30)
recipe_name_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", font=("Arial", 14), command=search_recipe)
search_button.pack(pady=10)

result_text = tk.Text(root, width=50, height=15, font=("Arial", 12), wrap=tk.WORD)
result_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
