regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.  #(?=...) Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
#regex_alternating_repetitive_digit_pair = r"(\d)\d*\1"

import re
P = input()
print (re.match(regex_integer_in_range, P))
print (re.findall(regex_alternating_repetitive_digit_pair, P))
print (bool(re.match(regex_integer_in_range, P))
       and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

'''
explanation:
(\d)(?=\d\1):
(\d): Match and capture a digit in group #1
(?=: Start lookahead
\d: Match any digit
\1: Back-reference to captured group #1
): End lookahead

input sample:
137370
'''