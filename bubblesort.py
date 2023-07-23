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
    try:
        orientation = int(
            input("Please enter 1 if you would like the sort to be in increasing order and 2 for decreasing order: "))
        choice = int(
            input("Please enter 1 for sorting integers and 2 for sorting multiple strings by the first letter: "))
        if choice == 1:
            try:
                elements = input("Please enter the elements with a space in between them: ").split()
                inp_arr = [int(element) for element in elements]
                output = bubble_sort(inp_arr)
                if orientation == 2:
                    output.reverse()
                choice_2 = int(input("Please enter 1 to get the minimum element, 2 for the maximum element, 3 for both, and 4 for neither: "))
                if choice_2 == 1:
                    if orientation == 2:
                        print(f"The sorted integers are: {output}. The minimum integer is {output[-1]}. Have a nice day!")
                    else:
                        print(f"The sorted integers are: {output}. The minimum integer is {output[0]}. Have a nice day!")
                elif choice_2 == 2:
                    if orientation == 2:
                        print(f"The sorted integers are: {output}. The maximum integer is {output[0]}. Have a nice day!")
                    else:
                        print(f"The sorted integers are: {output}. The maximum integer is {output[-1]}. Have a nice day!")
                elif choice_2 == 3:
                    if orientation == 2:
                        print(f"The sorted integers are: {output}. The minimum integer is {output[-1]} and the maximum integer is {output[0]}. Have a nice day!")
                    else:
                        print(f"The sorted integers are: {output}. The minimum integer is {output[0]} and the maximum integer is {output[-1]}. Have a nice day!")
                elif choice_2 == 4:
                    print(f"The sorted integers are: {output}. Have a nice day!")
            except ValueError:
                print("Invalid input, please try again with a valid input.")
        elif choice == 2:
            try:
                elements = input("Please enter the elements with a space in between each: ").split()
                output = bubble_sort(elements)
                if orientation == 2:
                    output = output[::-1]
                    print(output)
                choice_2 = int(input("Please enter 1 to get the minimum element, 2 for the maximum element, 3 for both, and 4 for neither: "))
                if choice_2 == 1:
                    if orientation == 2:
                        print(f"The sorted elements are: {output}. The minimum element is {output[-1]}. Have a nice day!")
                    else:
                        print(f"The sorted elements are: {output}. The minimum element is {output[0]}. Have a nice day!")
                elif choice_2 == 2:
                    if orientation == 2:
                        print(f"The sorted elements are: {output}. The maximum element is {output[0]}. Have a nice day!")
                    else:
                        print(
                            f"The sorted elements are: {output}. The maximum element is {output[-1]}. Have a nice day!")
                elif choice_2 == 3:
                    if orientation == 2:
                        print(f"The sorted elements are: {output}. The minimum element is {output[-1]} and the maximum element is {output[0]}. Have a nice day!")
                    else:
                        print(f"The sorted elements are: {output}. The minimum element is {output[0]} and the maximum element is {output[-1]}. Have a nice day!")
                elif choice_2 == 4:
                    print(f"The sorted elements are: {output}. Have a nice day!")
            except ValueError:
                print("Invalid input, please try again with a valid input.")
    except ValueError:
        print("Invalid input, please try again with valid input.")




