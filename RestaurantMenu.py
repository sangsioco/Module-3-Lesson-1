restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverage"] = {"Coke": 2.99, "Rootbeer": 2.99}
restaurant_menu["Main Course"]["Steak"] = "17.99"
remove_item = restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)