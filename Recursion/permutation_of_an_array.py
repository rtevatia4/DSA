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
        str[i], str[pos] = str[pos], str[i]         # backtracking

input_string = "abc"
input_to_list = list(input_string)
permutations(input_to_list,0)


# UNique permutations of an array
"""
given abb --   unique permutatitons are abb, bab,bba
"""
def permutations_unique(str, pos, ans):
    if pos == len(str):
        ans.append(str[::])
    ignore = set()
    for i in range(pos, len(str)):
        if str[i] in ignore: continue
        ignore.add(str[i])
        str[i], str[pos] = str[pos], str[i]
        permutations_unique(str,pos+1, ans)
        str[i], str[pos] = str[pos], str[i]         # backtracking

input_string = "abb"
input_to_list = list(input_string)
ans = []
print("uNique permutations of an array")
permutations_unique(input_to_list,0, ans)
print(ans)