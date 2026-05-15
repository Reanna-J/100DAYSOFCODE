#Debugging exercise
""" My Debugging Approach:
Describe the Problem – Clearly define what’s going wrong.
Reproduce the Bug – Try to trigger the error consistently.
Play Computer – Step through the code manually.
Fix the Error – Identify and correct the faulty logic.
Use print
Use a debugger """
import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
