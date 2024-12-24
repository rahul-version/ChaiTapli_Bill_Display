def menu():
    # Menu Of CHai ki Tapli
    dict1 ={'Samosa': 15 ,'Idli': 30 ,'Maggie': 50 ,'Dosa': 70 ,'Tea': 10 ,'Coffee': 20 ,'Sandwich': 35 ,'Colddrink': 25 ,'String': 20 ,'Chole bhatore': 30 ,'Paneer tikka': 40}
    order ={}
    TotalPrice = 0      # Initialize total Price 
    print("###     Welcome to CHai Ki Tapli     ###")
    for key,value in dict1.items():    # Display OF the MENU!!!!
        print(f"{key:15} ₹ {value}")
   
    while True :        # Using While LOOP
        order={}
        item_name = input('Enter the item you want or "End" to finish: ').capitalize()  
        
        if item_name.lower() =="end":       # Ending IF END Read!!!
            break
        else:
            if item_name not in dict1:       # If Item Not Found in Menu 
                print("NOT IN MENU")
            else:
                item_quantity = int(input("Enter the Quantity 0f Item: "))     # Taking input of Quantity 
                order[item_name] = item_quantity
        
    
        for i in order.keys():        
            TotalPrice += order[i]*dict1[i]      # Calculating the Total price 
    return f"Total Price: {TotalPrice}"  # At the end displa the total price 
print(menu())
        
