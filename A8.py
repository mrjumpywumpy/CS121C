import random
from timeit import default_timer


def curve_scores(number_list):
    """
    Curves the Numbers of a list to 100
    :param number_list: A list of numbers
    :return: curved_list: The list of all the numbers curved towards 100
    """

    curved_list = []
    biggest_number = 0
    for number in number_list:  # Finding the biggest number in the list
        if number > biggest_number:
            biggest_number = number
    curve_by = 100 - biggest_number  # Finding how much to curve by, by doing 100 minus the biggest number
    for number in number_list:
        curved_list.append(number + curve_by)  # Going through each number and adding the original number to the
        # curve_by and appending that to the curved_list
    return curved_list


def contains_duplicate(string_list):
    """
    Checks for duplicates of values in a list
    :param string_list: A list of strings
    :return: True or False
    """

    for index_search in range(len(string_list)):  # Looping through each string in the list
        for index_find in range(index_search+1, len(string_list)):  # Checking if the current string is in the list
            if string_list[index_search] == string_list[index_find]:  # If there's a duplicate return True
                return True
    return False  # If it's not in the list, return False


def list_to_string(number_list):
    """
    Changes a list to a string
    :param number_list: A list of numbers
    :return: The list now as a string instead of a list
    """

    string_list = '['  # Creates a string with the starting [
    for index in range(len(number_list)):  # Loops over the list by index
        if not index == (len(number_list) - 1):  # Checking if it's not the last one, to know when to add a ','
            string_list += str(number_list[index]) + ", "
        else:  # If it's the last one don't add a ','
            string_list += str(number_list[index])
    string_list += ']'
    return string_list


def find_smallest_positive_multiple_of_three(number_list):
    """
    Finds the smallest positive multiple of 3
    :param number_list: A list of integers
    :return: The smallest positive multiple of 3
    """

    multiple_of_three = None
    for number in number_list:  # Looping over each number in the list
        if number > 0 and number % 3 == 0 and (multiple_of_three == None or number < multiple_of_three):
            # Makes sure that a number is positive and that it's a multiple of 3. If it is then it checks if the current
            # stored multiple of 3 is None or less then the current number
            multiple_of_three = number

    return multiple_of_three


def sequential_search(target_integer, number_list):
    """
    Does a sequential search of a list, looking of a specific number
    :param target_integer: The desired number
    :param number_list: The list of numbers to check
    :return: True or False
    """

    for number in number_list:  # Looks at each number in the list
        if target_integer == number:  # Checks if that number is the same as the target number
            return True
    return False


def binary_search(target_integer, number_list):
    """
    Does a binary search over a list of numbers
    :param target_integer: The desired number
    :param number_list: A list of sorted numbers
    :return: True or False
    """

    # The initial start and stop indexes are the first (0) and the last (len - 1)
    start_index = 0
    stop_index = len(number_list) - 1
    while start_index <= stop_index:   # Runs until the stop index is less than the start index
        middle_index = (start_index + stop_index) // 2  # Sets the middle index between the start and stop

        if number_list[middle_index] == target_integer:  # Checks if the middle is the target number
            return True
        elif number_list[middle_index] < target_integer:  # If the middle is less then the target number then move stop
            stop_index = middle_index - 1
        else:  # If middle is more than the target then move the start
            start_index = middle_index + 1
    return False


def measure_search_times():
    """
    Measures the time for sequential vs. binary searches
    :return: None, just prints the results
    """
    by_ten = 1000  # By ten is how many numbers each loop it'll look through, it'll multiply by 10 each time
    while by_ten <= 10000000:  # Goes until the amount of numbers is more than 10000000
        large_test_loop = list(range(by_ten))  # Creates the list from the range from 0 to current by_ten
        number_of_random = 50  # How many random numbers to check against list
        random.shuffle(large_test_loop)  # Shuffling the list to not have it be in order
        start_time = default_timer()  # Starts the timer
        for count in range(number_of_random):  # Running sequential search for the given number of randoms
            sequential_search(random.randint(0, by_ten), large_test_loop)
        end_time = default_timer()  # Ending the timer
        average_time_sequential = (end_time - start_time) / number_of_random  # Averaging by dividing by # of tests
        start_time = default_timer()  # Starts timer
        large_test_loop.sort()  # Sort the list
        for count in range(number_of_random):  # Runs it for the number of random numbers
            binary_search(random.randint(0, by_ten), large_test_loop)
        end_time = default_timer()  # Ending the timer
        average_time_binary = (end_time - start_time) / number_of_random  # Averaging by dividing by # of tests
        print("For a list of", by_ten, " numbers the time for binary search is:", f'{average_time_binary:.8f}',
              'and the average time for sequential search is:', f'{average_time_sequential:.8f}')
        # Prints the results
        by_ten = by_ten * 10  # Goes to the next by 10


def main():
    number_list_1 = [1, 3, 5, 8, 9, 11, 13, 15, 18, 20, 23]
    number_list_2 = [69, 60, 63, 57, 85, 99]
    number_list_three = [-3, -6, 0, 3, 6]
    string_list_1 = ['the', 'boy', 'the']
    string_list_2 = ['I', 'You', 'He', 'She', 'They', 'We']
    empty_list = []
    print('Testing curve_scores(number_list_1), expecting [78, 80, 82, 85, 86, 88, 90, 92, 95, 97, 100], and got', curve_scores(number_list_1))
    print('Testing curve_scores(number_list_2), expecting [70, 61, 64, 58, 86, 100], and got', curve_scores(number_list_2))
    print('Testing curve_scores(empty_list), expecting [], and got', curve_scores(empty_list))
    print('Testing contains_duplicate(string_list_1), expecting True, and got', contains_duplicate(string_list_1))
    print('Testing contains_duplicate(string_list_2), expecting False, and got', contains_duplicate(string_list_2))
    print('Testing contains_duplicate(empty_list), expecting False, and got', contains_duplicate(empty_list))
    print("Testing list_to_string(number_list_1) and type(list_to_string(number_list_1)), expecting '[1, 3, 5, 8, 9, 11, 13, 15, 18, 20, 23]' and <class 'str'> and got")
    print(list_to_string(number_list_1), "and ", type(list_to_string(number_list_1)))
    print("Testing list_to_string(number_list_2) and type(list_to_string(number_list_1)), expecting '[69, 60, 63, 57, 85, 99]' and <class 'str'> and got")
    print(list_to_string(number_list_2), "and", type(list_to_string(number_list_2)))
    print("Testing list_to_string(empty_list) and type(list_to_string(empty_string)), expecting '[]' and <class 'str'> and got")
    print(list_to_string(empty_list), 'and', type(list_to_string(empty_list)))
    print("Testing find_smallest_positive_multiple_of_three(number_list_three), expecting 3 and got", find_smallest_positive_multiple_of_three(number_list_three))
    print("Testing find_smallest_positive_multiple_of_three(number_list_1), expecting 3 and got", find_smallest_positive_multiple_of_three(number_list_1))
    print("Testing find_smallest_positive_multiple_of_three(number_list_2, expecting 57 and got", find_smallest_positive_multiple_of_three(number_list_2))
    print("Testing find_smallest_positive_multiple_of_three(empty_list), expecting None and got", find_smallest_positive_multiple_of_three(empty_list))
    measure_search_times()


if __name__ == "__main__":
    main()

# Sorted, looking for 10 random numbers
# For a list of 1000  numbers the time for binary search is: 0.00000147 and the average time for sequential search is: 0.00000560
# For a list of 10000  numbers the time for binary search is: 0.00000130 and the average time for sequential search is: 0.00006385
# For a list of 100000  numbers the time for binary search is: 0.00000195 and the average time for sequential search is: 0.00057268
# For a list of 1000000  numbers the time for binary search is: 0.00000275 and the average time for sequential search is: 0.00512946
# For a list of 10000000  numbers the time for binary search is: 0.00000422 and the average time for sequential search is: 0.06936940

# With the list already sorted, the binary is faster, but as it continues going the difference becomes more and more,
# by the end of it, being a very significant difference


# Unsorted, looking for 10 random numbers
# For a list of 1000  numbers the time for binary search is: 0.00000823 and the average time for sequential search is: 0.00000919
# For a list of 10000  numbers the time for binary search is: 0.00008511 and the average time for sequential search is: 0.00007351
# For a list of 100000  numbers the time for binary search is: 0.00110313 and the average time for sequential search is: 0.00074502
# For a list of 1000000  numbers the time for binary search is: 0.01903421 and the average time for sequential search is: 0.01400121
# For a list of 10000000  numbers the time for binary search is: 0.27985995 and the average time for sequential search is: 0.27104137

# With the list unsorted, the binary and sequential are much closer together and the differences between them is
# Probably mostly up to chance from the looks of it.


# Unsorted, looking for 50 random numbers
# For a list of 1000  numbers the time for binary search is: 0.00000232 and the average time for sequential search is: 0.00000827
# For a list of 10000  numbers the time for binary search is: 0.00001919 and the average time for sequential search is: 0.00007910
# For a list of 100000  numbers the time for binary search is: 0.00022434 and the average time for sequential search is: 0.00078037
# For a list of 1000000  numbers the time for binary search is: 0.00373210 and the average time for sequential search is: 0.01385831
# For a list of 10000000  numbers the time for binary search is: 0.05256304 and the average time for sequential search is: 0.22556212

# With the list unsorted and looking for 50 random numbers instead of 10, the binary ends up being significantly faster
# than the other ones, though not as big of a difference as with sorted and looking for 10 numbers.