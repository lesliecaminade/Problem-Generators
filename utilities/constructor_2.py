base_string = 'boylestad_4_'
start = 1
end = 35


output = ''

for i in range(start, end + 1):

	output = output + f"""'{base_string}{i}',
"""

print(output)