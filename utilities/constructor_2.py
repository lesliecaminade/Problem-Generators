base_string = 'rgs_'
start = 1
end = 37


output = ''

for i in range(start, end + 1):

	output = output + f"""'{base_string}{i}',
"""

print(output)