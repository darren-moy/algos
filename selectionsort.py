import sys
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        minimum_idx = i

        # Find the index of the minimum element in the remaining unsorted part of the array
        for j in range(i + 1, n):
            if arr[j] < arr[minimum_idx]:
                minimum_idx = j

        # Swap the minimum element with the current element
        arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]

    return arr


def checkinp(message):
    inp = input(message)
    if inp.isnumeric():
        inp = int(inp)
        if inp in [1,2]:
            return inp
        else:
            print('The input you gave was not a choice. Please try again.')
            sys.exit(1)
    else:
        print('The input you gave was not an integer. Please try again.')
        sys.exit(1)


def printfunc(sortedarr, choice_2, orientation):
    if choice_2 == 1:
        if orientation == 2:
            print(f"The sorted elements are: {sortedarr}. The minimum element is {sortedarr[-1]}. Have a nice day!")
        else:
            print(f"The sorted elements are: {sortedarr}. The minimum element is {sortedarr[0]}. Have a nice day!")
    elif choice_2 == 2:
        if orientation == 2:
            print(f"The sorted elements are: {sortedarr}. The maximum element is {sortedarr[0]}. Have a nice day!")
        else:
            print(f"The sorted elements are: {sortedarr}. The maximum element is {sortedarr[-1]}. Have a nice day!")
    elif choice_2 == 3:
        if orientation == 2:
            print(f"The sorted elements are: {sortedarr}. The minimum element is {sortedarr[-1]}. The maximum element is {sortedarr[0]}. Have a nice day!")
        else:
            print(f"The sorted elements are: {sortedarr}. The minimum element is {sortedarr[0]}. The maximum element is {sortedarr[-1]}. Have a nice day!")
    elif choice_2 == 4:
        print(f"The sorted elements are: {sortedarr}. Have a nice day!")


def main():
    orientation = checkinp("Please enter 1 for sorting in increasing order and 2 for decreasing order: ")
    choice = checkinp("Please enter 1 for sorting integers and 2 for sorting multiple strings by their first letter: ")

    if choice == 1: # sorting integer array
        inputarr = input("Please enter the elements with a space in between: ").split()
        if all(ele.isdigit() for ele in inputarr):
            int_arr = [int(element) for element in inputarr]
            elements = selection_sort(int_arr)
        else:
            print("You did not enter all integers. Please try again.")
            sys.exit(1)
    else:           # sorting string array
        inputarr = input("Please enter the elements with a space in between: ").split()
        if (ele.isdigit() for ele in inputarr):
            print("You did not enter only strings or characters. Please try again.")
            sys.exit(1)
            elements = selection_sort(inputarr)
        else:
            elements = selection_sort(inputarr)

    if orientation == 2:
        elements = elements[::-1]

    choice_2 = input("Please enter 1 to get the minimum element, 2 for the maximum element, 3 for both, and 4 for neither: ")
    if choice_2.isnumeric():
        choice_2 = int(choice_2)
        if choice_2 in [1, 2, 3, 4]:
            choice_2 = choice_2
    printfunc(elements, choice_2, orientation)


if __name__ == "__main__":
    main()
