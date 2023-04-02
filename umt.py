from math import comb

def make_dictionary(list_of_coordonates):
    # This function takes a list of tuples and adds them in a dictionary,
    # where x in the tuple (x,y) is the key
    # and its value is a list consisting of all the y in tuples with the same x

    # For example: [(1,6), (2,3), (1,9)] is transformed into this:
    # dictionary = {1 : [6,9], 2: [3]}

    dictionary = {}

    for punct in list_of_coordonates:
        x,y = punct
        if dictionary.get(x) == None: # if the key doesnt exist in the dictionary
            dictionary[x] = [y] # make a list out of y
        else:
            dictionary[x].append(y) # append to the already existing list of all the y

    return dictionary


def number_of_rectangles(dictionary):
    # Calculates the number of rectangles that can be created by the points in the dictionary

    # The number of rectangles that can be calculated by:
    # 1. Taking every combinations of two different x (keys) in the dictionary and finding every unique y that they have in common (list intersection)
    # => this means that we are only searching for rectangles that are parallel with the X, Y axes
    # 2. Adding to the 'nr_rectangles' variable the combinations of (length of the intersection list) choose 2

    # If the intersection has two or more values, it means that there are at least two points on each of the two lines defined by the keys, 
    # and a rectangle can be created. The function uses the comb function from the math module to calculate the number of ways 
    # to choose two points from the intersection to form a rectangle.

    nr_rectangles = 0

    for i, (x1,list_y1) in enumerate(dictionary.items()):
        for x2,list_y2 in list(dictionary.items())[i+1:]: # takes the next pair of (key, list of values) from the dictionary
            intersection = set(list_y1).intersection(list_y2)
            if len(intersection) >= 2:
                nr_rectangles += comb(len(intersection), 2) # combinations of n choose k
    
    return nr_rectangles

def main():

    sample1= [(1,1), (1,3), (2,1), (2,3), (3,1), (3,3)]
    sample2= [(1,1), (1,3), (2,1), (3,1), (3,3)]

    dictionary1 = make_dictionary(sample1)
    dictionary2 = make_dictionary(sample2)

    # for x in dictionary1.keys():
    #     print(x, dictionary1.get(x))

    print("Sample 1:", number_of_rectangles(dictionary1))
    print("Sample 2:", number_of_rectangles(dictionary2))

main()
