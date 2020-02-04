base_string = 'ece_radio_receivers_section_1_'
start = 1
end = 50


output = ''

for i in range(start, end + 1):

	output = output + f"""'{base_string}{i}',
"""

print(output)