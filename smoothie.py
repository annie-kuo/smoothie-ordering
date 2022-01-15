# Annie Kuo

# Smooth Smoothies Smoothie Ordering System
# This program takes smoothie orders according to the user's inputs
# and displays the total amount payable with appropriate tax amounts listed

#Define global variables
SMOOTHIE1_NAME = "Pineapple Banana"
SMOOTHIE2_NAME = "Almond Basil"
SMOOTHIE3_NAME = "Purple Surprise"
SMOOTHIE4_NAME = "Onion Toffee"

SMOOTHIE1_COST = 4.99
SMOOTHIE2_COST = 6.49
SMOOTHIE3_COST = 3.99
SMOOTHIE4_COST = 9.99

SIZE1_NAME = "small"
SIZE2_NAME = "medium"
SIZE3_NAME = "large"
SIZE4_NAME = "galactic"

SIZE1_COST = -2.0
SIZE2_COST = 0.0
SIZE3_COST = 2.0
SIZE4_COST = 100.0

TOPPING1_NAME = "no topping"
TOPPING2_NAME = "cinnamon"
TOPPING3_NAME = "chocolate shavings"
TOPPING4_NAME = "shredded coconut"

TOPPING1_COST = 0.0
TOPPING2_COST = 1.0
TOPPING3_COST = 1.0
TOPPING4_COST = 1.0

#Define functions
def pose_question_with_costs(question, option1, cost1, option2, cost2, option3, cost3, option4, cost4):
    """(str, str, float, str, float, str, float, str, float) -> str
    
    The function presents the question to the user and displays the four options and costs.
    The function returns the option selected according to the user's input.
    
    >>> pose_question_with_costs("Which size would you like?", "small", -2.0, "medium", 0.0, "large", 2.0, "galactic", 100.0)
    Which size would you like?
    1)  $-2.0   small
    2)  $0.0    medium
    3)  $2.0    large
    4)  $100.0  galactic
    Your choice (1-4): 3
    You have selected large.
    'large'
    >>> pose_question_with_costs("Which smoothie would you like?", "Pineapple Banana", 4.99, "Almond Basil", 6.49, "Purple Surprise", 0.99, "Onion Toffee", 9.99)
    Which smoothie would you like?
    1)  $4.99   Pineapple Banana
    2)  $6.49   Almond Basil
    3)  $0.99   Purple Surprise
    4)  $9.99   Onion Toffee
    Your choice (1-4): 2
    You have selected Almond Basil.
    'Almond Basil'
    >>> pose_question_with_costs("Which topping would you like?", "no topping", 0.0, "cinnamon", 1.0, "chocolate shavings", 1.0, "shredded coconut", 1.0)
    Which topping would you like?
    1)  $0.0    no topping
    2)  $1.0    cinnamon
    3)  $1.0    chocolate shavings
    4)  $1.0    shredded coconut
    Your choice (1-4): hello
    ''
    """
    # display the question and the options with their associated cost and option number
    print(question)
    print("1)\t$" + str(cost1) + "\t" + option1)
    print("2)\t$" + str(cost2) + "\t" + option2)
    print("3)\t$" + str(cost3) + "\t" + option3)
    print("4)\t$" + str(cost4) + "\t" + option4)
    
    # take input from the user
    option_chosen = input("Your choice (1-4): ")
    
    # return the option's name
    if option_chosen == "1":
        print("You have selected " + option1 + ".")
        return option1
    elif option_chosen == "2":
        print("You have selected " + option2 + ".")
        return option2
    elif option_chosen == "3":
        print("You have selected " + option3 + ".")
        return option3
    elif option_chosen == "4":
        print("You have selected " + option4 + ".")
        return option4
    else:
        return ""
    

def calculate_subtotal(smoothie_type, smoothie_size, topping):
    """ (str, str, str) -> float

    The function calculates and returns the price of the smoothie according to the smoothie type, size and topping.
    The function returns the subtotal as a floating point number rounded to two decimal places.
    
    >>> calculate_subtotal(SMOOTHIE1_NAME, SIZE4_NAME, TOPPING4_NAME)
    15.99
    >>> calculate_subtotal(SMOOTHIE2_NAME, SIZE3_NAME, TOPPING1_NAME)
    8.49
    >>> calculate_subtotal(SMOOTHIE3_NAME, SIZE2_NAME, TOPPING2_NAME)
    1.99
    """
    # determine the cost of the smoothie type chosen
    if smoothie_type == SMOOTHIE1_NAME:
        type_cost= SMOOTHIE1_COST
    elif smoothie_type == SMOOTHIE2_NAME:
        type_cost= SMOOTHIE2_COST
    elif smoothie_type == SMOOTHIE3_NAME:
        type_cost= SMOOTHIE3_COST
    elif smoothie_type == SMOOTHIE4_NAME:
        type_cost= SMOOTHIE4_COST
    
    # determine the cost of the size chosen
    if smoothie_size == SIZE1_NAME:
        size_cost= SIZE1_COST
    elif smoothie_size == SIZE2_NAME:
        size_cost= SIZE2_COST
    elif smoothie_size == SIZE3_NAME:
        size_cost= SIZE3_COST
    elif smoothie_size == SIZE4_NAME:
        size_cost= SIZE4_COST
    
    # determine the cost of the topping
    if topping == TOPPING1_NAME:
        topping_cost= TOPPING1_COST
    else:
        topping_cost= TOPPING2_COST
    
    # calculate and return the subtotal
    SUBTOTAL= round(type_cost + size_cost + topping_cost,2)
    return SUBTOTAL


def print_receipt(subtotal, smoothie_type, smoothie_size, topping):
    """ (float, str, str, str) -> float
    
    The function prints out the customer's receipt by displaying the customer's order,
    and then the subtotal, followed by the tax and the total.
    
    >>> print_receipt(110.99, SMOOTHIE4_NAME, SIZE4_NAME, TOPPING4_NAME)
    You ordered a galactic Onion Toffee smoothie with shredded coconut
    Smoothie cost: $ 110.99
    GST:    $ 5.55
    QST:    $ 11.07
    Total:  $ 127.61
    127.61
    >>> print_receipt(6.99, SMOOTHIE1_NAME, SIZE3_NAME, TOPPING1_NAME)
    You ordered a large Pineapple Banana smoothie
    Smoothie cost: $ 6.99
    GST:    $ 0.35
    QST:    $ 0.7
    Total:  $ 8.04
    8.04
    >>> print_receipt(2.99, SMOOTHIE3_NAME, SIZE1_NAME, TOPPING4_NAME)
    You ordered a small Purple Surprise smoothie with shredded coconut
    Smoothie cost: $ 2.99
    GST:    $ 0.15
    QST:    $ 0.3
    Total:  $ 3.44
    3.44
    """
    # display the customer's order
    if topping == TOPPING1_NAME:
        user_order= smoothie_size + " " + smoothie_type + " smoothie"
    else:
        user_order= smoothie_size + " " + smoothie_type + " smoothie with " + topping
    print("You ordered a " + user_order)

    # display the order's subtotal
    print("Smoothie cost: $" , subtotal)
    
    # calculate and display the taxes
    order_GST= 0.05*subtotal
    order_QST= 0.09975*subtotal
    print("GST:    $", round(order_GST,2))
    print("QST:    $", round(order_QST,2))
    
    # calculate, display, and return the total
    total= round(subtotal + order_GST + order_QST,2)
    print("Total:  $", total)
    return total
    

def order():
    """ ()-> NoneType

    The function welcomes the user and takes the user's order from the user's input. The function then prints the receipt.
    The function will only allow the smoothie type to be the fourth option (Onion Toffee).
    The function will return if the user's input is invalid (not a from the options given).
    
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $4.99   Pineapple Banana
    2)  $6.49   Almond Basil
    3)  $3.99   Purple Surprise
    4)  $9.99   Onion Toffee
    Your choice (1-4): 1
    You have selected Pineapple Banana.
    Unfortunately, we are out of Pineapple Banana
    You will be served Onion Toffee smoothie.
    Which size would you like?
    1)  $-2.0   small
    2)  $0.0    medium
    3)  $2.0    large
    4)  $100.0  galactic
    Your choice (1-4): 1
    You have selected small.
    Which topping would you like?
    1)  $0.0    no topping
    2)  $1.0    cinnamon
    3)  $1.0    chocolate shavings
    4)  $1.0    shredded coconut
    Your choice (1-4): 1
    You have selected no topping.
    You ordered a small Onion Toffee smoothie
    Smoothie cost: $ 7.99
    GST:    $ 0.4
    QST:    $ 0.8
    Total:  $ 9.19
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $4.99   Pineapple Banana
    2)  $6.49   Almond Basil
    3)  $3.99   Purple Surprise
    4)  $9.99   Onion Toffee
    Your choice (1-4): 4
    You have selected Onion Toffee.
    Which size would you like?
    1)  $-2.0   small
    2)  $0.0    medium
    3)  $2.0    large
    4)  $100.0  galactic
    Your choice (1-4): 5
    Sorry, that is not a valid option.
    >>> order()
    Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $4.99   Pineapple Banana
    2)  $6.49   Almond Basil
    3)  $3.99   Purple Surprise
    4)  $9.99   Onion Toffee
    Your choice (1-4): 2
    You have selected Almond Basil.
    Unfortunately, we are out of Almond Basil
    You will be served Onion Toffee smoothie.
    Which size would you like?
    1)  $-2.0   small
    2)  $0.0    medium
    3)  $2.0    large
    4)  $100.0  galactic
    Your choice (1-4): 4
    You have selected galactic.
    Which topping would you like?
    1)  $0.0    no topping
    2)  $1.0    cinnamon
    3)  $1.0    chocolate shavings
    4)  $1.0    shredded coconut
    Your choice (1-4): 1
    You have selected no topping.
    You ordered a galactic Onion Toffee smoothie
    Smoothie cost: $ 109.99
    GST:    $ 5.5
    QST:    $ 10.97
    Total:  $ 126.46
    >>> order()
   Welcome to Smooth Smoothies Smoothie Ordering System
    Have you tried our new Onion Toffee smoothie?
    Which smoothie would you like?
    1)  $4.99   Pineapple Banana
    2)  $6.49   Almond Basil
    3)  $3.99   Purple Surprise
    4)  $9.99   Onion Toffee
    Your choice (1-4): hello
    Sorry, that is not a valid option.
    """
    # welcome the customer to Smooth Smoothies and recommend Onion Toffee
    print("Welcome to Smooth Smoothies Smoothie Ordering System")
    print("Have you tried our new Onion Toffee smoothie?")
    
    # ask customer what type of smoothie they would like
    order_type= pose_question_with_costs("Which smoothie would you like?", SMOOTHIE1_NAME, SMOOTHIE1_COST, SMOOTHIE2_NAME, SMOOTHIE2_COST, SMOOTHIE3_NAME, SMOOTHIE3_COST, SMOOTHIE4_NAME, SMOOTHIE4_COST)
    if order_type == "":
        print("Sorry, that is not a valid option.")
        return
    if order_type != SMOOTHIE4_NAME:
        print("Unfortunately, we are out of" , order_type)
        print("You will be served Onion Toffee smoothie.")
        order_type = SMOOTHIE4_NAME
        
    # ask customer which size of smoothie they would like
    order_size= pose_question_with_costs("Which size would you like?", SIZE1_NAME, SIZE1_COST, SIZE2_NAME, SIZE2_COST, SIZE3_NAME, SIZE3_COST, SIZE4_NAME, SIZE4_COST)
    if order_size == "":
        print("Sorry, that is not a valid option.")
        return
    
    # ask customer which topping they would like
    order_topping= pose_question_with_costs("Which topping would you like?", TOPPING1_NAME, TOPPING1_COST, TOPPING2_NAME, TOPPING2_COST, TOPPING3_NAME, TOPPING3_COST, TOPPING4_NAME, TOPPING4_COST)
    if order_topping == "":
        print("Sorry, that is not a valid option.")
        return
    
    # display the receipt
    SUBTOTAL= calculate_subtotal(order_type, order_size, order_topping)
    print_receipt(SUBTOTAL, order_type, order_size, order_topping)