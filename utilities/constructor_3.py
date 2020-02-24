
start = 1
end = 29
mode = 'normal'

template = 'source3.electronic_devices_semiconductors_'
suffix = '(),'

for i in range(start, end + 1):
	if mode == 'normal':

		print(f"""{template}{i}{suffix}""")
	if mode == 'combination':

		print(f"""{template}{2*i - 1}_{2*i}{suffix}""")