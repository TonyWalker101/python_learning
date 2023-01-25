# receipt generating program for imaginary retail store

# inventory descriptions
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# prices
lovely_loveseat_price = 254.00

stylish_settee_price = 180.50

luxurious_lamp_price = 52.15

# tax percentage
sales_tax = 0.088

# customer one starting variables
customer_one_total = 0
customer_one_itemization = ""
customer_one_tax = 0

customer_one_total += lovely_loveseat_price
# print("Total after purchase #1: ",customer_one_total)

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
# print("Total after purchase #2: ",customer_one_total)

customer_one_itemization += ", " + luxurious_lamp_description

customer_one_tax = round(customer_one_total * sales_tax,2)
# print("Tax: ", customer_one_tax)

customer_one_total += customer_one_tax
# print("Total after tax: ", customer_one_total)

# final receipt
print("Customer One Items: ", customer_one_itemization)
print("Customer One Total: ", customer_one_total)
