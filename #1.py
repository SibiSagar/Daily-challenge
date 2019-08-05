'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

'''


list_numbers=[int(i) for i in input().split()]

k=int(input())

def istrue(list_number,k):
    for j in list_numbers:
        if k-j in list_numbers:
            return True
        return False


print(istrue(list_numbers,k))