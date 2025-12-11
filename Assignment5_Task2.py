#Assignment 5
#Task 2: Demonstrate List Slicing
#creating list
lst = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {lst}")

#fetching first five element form list lst.
first_five=lst[0:5:1]
print(f"Extracted first five element: {first_five}")

#Reversing the extracted element of list first_five
reverse_extract=(first_five[-1:-6:-1])
print(f"Reverse extracted element: {reverse_extract}")