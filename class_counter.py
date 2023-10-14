from datetime import datetime



import json
with open("data/meals.json") as file:
	meals = json.load(file)
     
with open ("data/combos.json") as file:
	combos = json.load(file)
      
with open ("data/calories_j.json") as file:
	calories = json.load(file)

meal_list = meals.get('meals')
combos_list = combos.get('combos')


meals2 = {x["name"]: x for x in meal_list}

meals3 = {x["id"]: x for x in meal_list}

combos2 = {x["name"]: x for x in combos_list}




#instead of creating a new property for too many calories and refusing the order,
#i will raise an error
class MealTooBigError (Exception):
     def __init__(self):
          self.message = "too many calories"


class Order:
    counter = 0  #to count multiple orders

    def __init__(self, items):
        #to display order number
        self.order_id = f"order number {Order.counter + 1}"
        #to display order time
        self.date = datetime.now()
        self.items = items
        #to increase the counter with each order
        Order.counter +=1

    @property
    def calories(self):
        tot_calories = 0
        for item in self.items:
            item = item.strip()
            if item in meals2:
                meal_name = meals2[item]
                tot_calories += meal_name['calories']
            elif item in combos2:
                combo_name = combos2 [item]
                combo_items = combo_name['meals']
                for i in combo_items:
                    i = i.strip()
                    if i in meals3:
                        combo_tot = meals3[i]
                        tot_calories += combo_tot['calories']
        if tot_calories >2000:
             raise MealTooBigError
        return tot_calories
    
    @property
    def price(self):
         tot_price = 0
         for item in self.items:
            item = item.strip()
            if item in meals2:
                meal_name = meals2[item]
                tot_price += meal_name['price']
            elif item in combos2:
                combo_name = combos2 [item]
                combo_items = combo_name['meals']
                for i in combo_items:
                    i = i.strip()
                    if i in meals3:
                        combo_tot = meals3[i]
                        tot_price += combo_tot['price']
         return tot_price

    def order_summary (self):
         print(f"Order ID: {self.order_id}")
         print(f"order time {self.date}")
         print(f"total calories: {self.calories}")
         print(f"items ordered: " )
         for item in self.items:
            item = item.strip()
            if item in meals2:
                name = meals2[item]['name']
                print(name)
            elif item in combos2:
                name = combos2[item]['name']
                print(name)
        


user_items = input("what did you eat? separate orders by ; and items by ,")
diff_orders = user_items.split(";")
for order in diff_orders:
    order_items = order.split(",")
    order = Order(order_items)
    order.order_summary()

		




				
				
				


