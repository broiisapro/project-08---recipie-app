// Fetch recipes and populate the dropdown menu
fetch('/get_recipes')
    .then(response => response.json())
    .then(data => {
        const select = document.getElementById('recipe-select');
        data.forEach(recipe => {
            const option = document.createElement('option');
            option.value = recipe.name;
            option.textContent = recipe.name;
            select.appendChild(option);
        });
    })
    .catch(error => console.error('Error fetching recipes:', error));

// Handle form submission
document.getElementById('recipe-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from reloading the page

    const selectedRecipe = document.getElementById('recipe-select').value;
    if (!selectedRecipe) {
        alert('Please select a recipe.');
        return;
    }

    // Fetch recipe details for the selected recipe
    fetch('/get_recipe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ 'dish': selectedRecipe })
    })
        .then(response => response.json())
        .then(data => {
            const results = document.getElementById('results');
            if (data.error) {
                results.innerHTML = `<p>${data.error}</p>`;
            } else {
                results.innerHTML = `
                    <div class="recipe-card">
                        <h2>${data.name}</h2>
                        <img src="${data.image}" alt="${data.name}" style="width: 300px; height: auto;">
                        <h3>Ingredients:</h3>
                        <ul>${data.ingredients.map(ing => `<li>${ing}</li>`).join('')}</ul>
                        <h3>Procedure:</h3>
                        <ol>${data.procedure.map(step => `<li>${step}</li>`).join('')}</ol>
                    </div>`;
            }
        })
        .catch(error => console.error('Error fetching recipe:', error));
});
