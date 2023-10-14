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




def food_list (food):
    #an empty list of food calories
    cal_list = []
    #for each food item listed by the user
    for item in food:
        #.strip() deletes spaces, to match the key in calories dic
        if item.strip() in calories:
            #pulls the value of the key using .get
            cal_list.append(calories.get(item.strip()))

    tot_cals = sum(cal_list)
    print ("total calories is " + str(tot_cals))