import math

def get_highest_product_of_three(input_integers):
    highest_product_of_3 = 0
    highest_product_of_2 = 0
    highest_number = 0
    lowest_product_of_2 = 0
    lowest_number = 0

    for i in range(len(input_integers)):
        highest_product_of_3 = max(highest_product_of_3, highest_product_of_2 * input_integers[i])
        highest_product_of_2 = max(highest_product_of_2, highest_number * input_integers[i])
        highest_number = max(highest_number, input_integers[i])

        lowest_product_of_2 = max(lowest_product_of_2, lowest_number * input_integers[i])
        lowest_number = min(lowest_number, input_integers[i])

        highest_product_of_3 = max(lowest_product_of_2 * highest_number, highest_product_of_3)

    return highest_product_of_3

print(get_highest_product_of_three([1,1,-8,1,10,2,5,6,-7,-7]))