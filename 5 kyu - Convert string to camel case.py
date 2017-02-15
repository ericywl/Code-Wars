import re

def to_camel_case(string):
	string_list = re.split('[_-]', string)
	camel_case_string = string_list[0]
	for word in string_list[1:]:
		camel_case_string += (word[0].upper() + word[1:].lower())
	return camel_case_string