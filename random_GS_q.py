'''
Given a 2-D String array of student-marks find the student with the highest average and output his average score. If the average is in decimals, floor it down to the nearest integer.

Example 1:
----------
Input:  [{"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]
Output: 99
Explanation: Since Jessica's average is greater than Bob's, Mike's and Jason's average.
'''


def maxAvg(marks):
    avg_map = {}

    for name,mark in marks:
        if name in avg_map:
            c = avg_map[name][0]
            m = avg_map[name][1]
            avg_map[name] = [c+1,m+int(mark)]
        else:
            avg_map[name] = [1,int(mark)]
    
    max_avg = float("-inf")
    name = ""
    for k,v in avg_map.items():
        c = v[0]
        m = v[1]
        a = m//c
        if a > max_avg:
            max_avg = a
            name = k

    return [name,max_avg]

scores = [("Bob","87"), ("Mike", "35"),("Bob", "52"), ("Jason","35"), ("Mike", "55"), ("Jessica", "99")]
print(maxAvg(scores))