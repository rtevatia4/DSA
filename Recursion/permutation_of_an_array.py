"""
A permutation is a rearrangement of members of a sequence into a new sequence. 
For example, there are 24 permutations of [a, b, c, d]. Some of them are [b, a, d, c], [d, a, b, c] and [a, d, b, c].
4 elements here so 4! arrangements
"""

def permutations(str, pos):
    if pos == len(str):
        print(str)
    for i in range(pos, len(str)):
        str[i], str[pos] = str[pos], str[i]
        permutations(str,pos+1)
        str[i], str[pos] = str[pos], str[i]

input_string = "abc"
input_to_list = list(input_string)
permutations(input_to_list,0)