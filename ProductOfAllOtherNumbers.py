def product_of_all_other_numbers(list_of_numbers):

    product_before_index = 1
    product_after_index = 1
    results_array = [1]*len(list_of_numbers)

    for i in range(len(list_of_numbers)):
        results_array[i] *= product_before_index
        results_array[len(list_of_numbers) - i - 1] *= product_after_index

        product_before_index *= list_of_numbers[i]
        product_after_index *= list_of_numbers[len(list_of_numbers) - i - 1]
    return results_array

print(product_of_all_other_numbers([1, 2, 6, 5, 9]))