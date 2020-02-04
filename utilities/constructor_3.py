
start = 1
end = 23

template = 'source2.engineering_electronic_devices_thyristors_'
suffix = '(),'

for i in range(start, end + 1):
	print(f"""{template}{i}{suffix}""")