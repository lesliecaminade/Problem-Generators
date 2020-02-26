base_string = 'example_2_'
start = 1
end = 21


output = ''

for i in range(start, end + 1):

	output = output + f"""'{base_string}{i}',
"""

print(output)