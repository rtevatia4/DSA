
# Below is the implementation of the above approach

def printSubsequence(input, output):
    # if the input is empty print the output string
    if len(input) == 0:
        print(output)
        freq = [0] * 26
        for ch in output:
            freq[ord(ch)-97] += 1
        good = True
        for item in freq:
            if item != max(freq) and item != 0:
                print("NG")
                good = False
                break
        if good:
            seq[0] += 1
        return

    # output is passed with including the
    # 1st character of input string
    printSubsequence(input[1:], output+input[0])

    # output is passed without including the
    # 1st character of input string
    printSubsequence(input[1:], output)

seq = [0]
output = ""
input = "aabb"
printSubsequence(input, output)
print(seq[0])
 
# Driver code
# output is set to null before passing in
# as a parameter

