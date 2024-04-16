from django.shortcuts import render, redirect
from vegetable.models import Recipe
# Create your views here.


recipe_file = "recipe.html"
def recipes(request):
    if (request.method == "POST"):
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")   # for getting file this is needed
        Recipe.objects.create(name=recipe_name,description=recipe_description,image=recipe_image)
        print(f"name {recipe_name}, description: {recipe_description}, img: {recipe_image}")
        redirect("/recipes/")
    recipes = Recipe.objects.all()
    return render(request, recipe_file, context={"recipes":recipes})



def delete_recipe(request, id):
    # if(request.method == "DELETE"):
    query = Recipe.objects.get(id=id)
    query.delete()
    return redirect("/recipes/")
