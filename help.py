from random import shuffle, randint

def zip_zap(a,b):
	if(len(a) != len(b)):
		return None
	return [[a[i],b[i]] for i in range(len(a))]

def is_sorted(arr):
    for i in range(1, len(arr)):
        if(arr[i - 1] < arr[i]):
            return False
    return True

def q_sort(array, compare):
    """Sort the array by using quicksort."""
    shuffle(array)
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]

        for x in array:
            if compare(x) < compare(pivot):
                less.append(x)
            elif compare(x) == compare(pivot):
                equal.append(x)
            else:
                greater.append(x)

        # Don't forget to return something!
        return q_sort(less, compare)+equal+q_sort(greater, compare)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

def validate(name):
    if(type(name) != str or len(name) <= 0):
        return None
    letters = [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
    if(sum([i in letters for i in name]) < len(name)):
        return None
    return name