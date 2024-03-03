hw_inventory={
    "Potato":{"price":10,"qty":2,"unit":'kg'},
    "Onion":{"price":20,"qty":3000,"unit":'g'},
    "Tomato":{"price":30,"qty":2000,"unit":'g'}
}
hw_menu={
    "Pizza":{
        "ingredients": ("Tomato","Onion"),
        "quantities": (300, 2),
        "units": ("g", "kg")
    },
    "Burger": {
        "ingredients": ("Potato","Onion"),
        "quantities": (300, 2),
        "units": ("g", "kg")
    },
    "Pani puri":{
        "ingredients": ("Potato","Rawa"),
        "quantities": (300, 2),
        "units": ("g", "kg")
    }
}
for item, details in hw_menu.items():
    ingredients = details["ingredients"]
    quantities = details["quantities"]
    units = details["units"]
    doable = True
    for i in range(len(ingredients)):
        ingredient = ingredients[i]
        required_quantity = quantities[i]
        required_unit = units[i]
        if ingredient in hw_inventory:
            available_quantity = hw_inventory[ingredient]["qty"]
            available_unit = hw_inventory[ingredient]["unit"]
            # Convert all quantities to the same unit for comparison
            if required_unit == "kg" and available_unit == "g":
                available_quantity /= 1000
            if available_quantity < required_quantity:
                doable = False
                print(f"Not enough {ingredient} for {item}")
        else:
            doable = False
            print(f"Ingredient {ingredient} not available for {item}")
    if doable:
        print(f"{item} is doable")
    else:
        print(f"{item} is not doable")