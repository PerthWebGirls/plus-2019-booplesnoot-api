from django.contrib import admin

from .models import Profile, Preferences, Diet, DietRequirement, Recipe, Ingredient, Cuisine, Comments

admin.site.register(Profile)
admin.site.register(Preferences)
admin.site.register(Diet)
admin.site.register(DietRequirement)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Cuisine)
admin.site.register(Comments)
