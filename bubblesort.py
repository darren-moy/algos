def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        # upper bound is size - i - 1 because on every iteration, the last item should be in its place so no need to iterate
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:                       # swap if current item is greater than the item to the right (pushing greatest int to the right)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":

    choice = int(input("Please enter 1 for sorting integers and 2 for sorting multiple strings by the first letter: "))
    if choice == 1:
        try:
            elements = input("Please enter the elements with a space in between them: ").split()
            inp_arr = [int(element) for element in elements]
            output = bubble_sort(inp_arr)
            print(f"The sorted integers are: {output}. Have a nice day!")
        except ValueError:
            print("Invalid input, please try again with a valid input.")
    elif choice == 2:
        try:
            elements = input("Please enter the elements with a space in between each: ").split()
            output = bubble_sort(elements)
            print(f"The sorted strings are {output}. Have a nice day!")
        except ValueError:
            print("Invalid input, please try again with valid input.")

    else:
        print("You did not enter a valid choice. Please try again.")


