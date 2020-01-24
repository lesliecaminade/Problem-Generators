base_string = 'boylestad_11_'
start = 1
end = 14


output = ''

for i in range(start, end + 1):

	output = output + f"""'{base_string}{i}',
"""

print(output)