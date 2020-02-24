base_string = 'jma_15_'
start = 1
end = 9


output = ''

for i in range(start, end + 1):

	output = output + f"""'{base_string}{i}',
"""

print(output)