"""Relational operators as variables in code."""

__author__ = "730306940"

left_hand_side_str = input("Left-hand side: ")
left_hand_side_int = int(left_hand_side_str)
right_hand_side_str = input("Right-hand side: ")
right_hand_side_int = int(right_hand_side_str)
print(left_hand_side_str + " < " + right_hand_side_str + " is " + str(left_hand_side_int < right_hand_side_int))
print(left_hand_side_str + " >= " + right_hand_side_str + " is " + str(left_hand_side_int >= right_hand_side_int))
print(left_hand_side_str + " == " + right_hand_side_str + " is " + str(left_hand_side_int == right_hand_side_int))
print(left_hand_side_str + " != " + right_hand_side_str + " is " + str(left_hand_side_int != right_hand_side_int))