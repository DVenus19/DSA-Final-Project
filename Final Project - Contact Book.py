print("^^^^^^^^^^^^^Donasco,Venus M.^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^BSCOE 2-2^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^Final Project - Contact Book^^^^^^^^^^^^^")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot_value = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def print_directory(names, phone_numbers):
    print("\nName\t\t\tPhone Number\n")
    for i in range(len(names)):
        print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

def add_contact(names, phone_numbers):
    name = input("Enter name: ")
    phone_number = int(input("Enter phone number: "))
    names.append(name)
    phone_numbers.append(phone_number)
    print("Contact Added Successfully.")

def search_contact(names, phone_numbers):
    search_term = input("Enter search term: ")
    if search_term in names:
        index = names.index(search_term)
        print("Name: {}, Phone Number: {}".format(search_term, phone_number))
    else:
        print("Name not Found,please try again")

def delete_contact(names, phone_numbers):
    delete_name = input("Enter name to delete: ")
    if delete_name in names:
        index = names.index(delete_name)
        del names[index]
        del phone_numbers[index]
        print("Contact Deleted Successfully.")
    else:
        print("Name Not Found")

names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Name: ")
    phone_number = int(input("Phone Number: "))
    names.append(name)
    phone_numbers.append(int(phone_number))

print_directory(names, phone_numbers)

while True:
    print("Menu Options:\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Sort by Merge Sort\n5. Sort by Insertion Sort\n6. Sort by Quick Sort\n7. Sort by Bubble Sort\n8. Exit")
    choice = int(input("Enter your Choice: "))

    if choice == 1:
        add_contact(names, phone_numbers)
        print_directory(names, phone_numbers)

    elif choice == 2:
        search_contact(names, phone_numbers)

    elif choice == 3:
        delete_contact(names, phone_numbers)
        print_directory(names, phone_numbers)

    elif choice == 4:
        merge_sort(names)
        print_directory(names, phone_numbers)

    elif choice == 5:
        insertion_sort(names)
        print_directory(names, phone_numbers)

    elif choice == 6:
        quick_sort(names, 0, len(names)-1)
        print_directory(names, phone_numbers)

    elif choice == 7:
        bubble_sort(names)
        print_directory(names, phone_numbers)

    elif choice == 8:
        print("Thank You!, Exiting program...")
        break

    else:
        print("Invalid choice. Please enter a valid choice.")