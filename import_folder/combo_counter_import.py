calories = {
   'Hamburger': 600,
   'Cheese Burger': 750,
   'Veggie Burger': 400,
   'Vegan Burger': 350,
   'Sweet Potatoes': 230,
   'Salad': 15,
   'Iced Tea': 70,
   'Lemonade': 90,
}



combos = {
    "Cheesy Combo" : ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo" : ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo" : ["Vegan Burger", "Salad", "Lemonade"],
}




def calorie_counter (items):

    #empty list of calories
    total_calories = 0

    for item in items:
        item = item.strip() #strips the item to match in dictionary
        try:
            if item in calories:
                #appends to total calories
                total_calories += calories[item]

            elif item in combos:
                #creates a list of items in combo
                combo_items = combos[item]
                for i in combo_items:
                    i = i.strip()
                    #adds the calorie value of the items in combo to the total calorie list
                    total_calories += calories[i]
        except:
            print("an error occured")

    print("your total calories are " + str(total_calories))