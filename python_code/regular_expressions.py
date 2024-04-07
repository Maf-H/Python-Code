#  Copyright (c) 24-06/04/2024, 16:48.
#  @author Mesfin Haftu

import re
"""
(x)? optional
(x)| or
(x)* zero or more times repetition
(x)+ one or more times repetition
(x){n, m} n - m times repetition of string x
re.compile(r'.at')   .(dot) is called wildcard it to any character except newline
re.compile(r'\d$') returns if the string last number if ends with digit (0 - 9).
re.compile(r'^\d+$') used to check if the whole string is number.

"""

#                             group(1)   group(2)   group(3)
phoneNumRegex = re.compile(r'(\+\d\d\d)-(\d\d\d)-(\d\d\d\d\d\d)')
mobile = phoneNumRegex.search('My number is +251-911-615532.')
print(f"Phone-> {mobile.group(0)}\nCountry code: {mobile.group(1)}\nRegion: {mobile.group(2)}\nMain:   {mobile.group(3)}")
Country_code, Region, Main = mobile.groups()
print(Country_code, Region, Main)

bat_regex = re.compile(r'Bat( man|mobile|copter|amimal)')  # | uses as or operator.
output = bat_regex.search('Bat man movie is streaming.')
print(output.group(0))

phoneNumRegex = re.compile(r'(\+\d\d\d )?\d\d\d \d\d\d\d\d\d')  # (wo)? is optional
output_1 = phoneNumRegex.search('0911 615532')
output_2 = phoneNumRegex.search('+251 911 994200')

print(output_1.group())
print(output_2.group())


