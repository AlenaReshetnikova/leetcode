# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
def is_valid(s: str) -> bool:
    number = "1234567890*+/- "
    first = "[{("
    second = "]})"
    true = []
    for i in range(len(s)):
        if s[i] not in number:
            if s[i] in first:
                true.append(first.find(s[i]))
            else:
                back_skobka_index = second.find(s[i])
                if true == []:
                    return False
                if back_skobka_index != true[-1]:
                    return False
                else:
                    del true[-1]
    if true!= []:
        return False
    return True


tests_for_true = ["2+2*2", "2+1-(34+2+1)* 25", "()","2+1-(34+2+1)* 25", "[2+{3-4}*7] "]
tests_for_false = ["}", "[{]}", "}}{{","25/(32+11)*[12-54}-3*{3-5]", "((23-4) * 3"]
print('have to be true')
for i in range(len(tests_for_true)):
   print(is_valid(tests_for_true[i]))
print('have to be false')
for i in range(len(tests_for_false)):
    print(is_valid(tests_for_false[i]))