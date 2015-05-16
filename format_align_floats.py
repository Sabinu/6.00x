job_IDs = ['13453', '123', '563456']
memory_used = [30, 150.54, 20.6]
memory_units = ['MB', 'GB', 'MB']

for i in range(len(job_IDs)):
    print("Job {item:15} {value[0]:>6}.{value[1]:<6} {units:3}".format(item=job_IDs[i]+':', 
    	value=str(memory_used[i]).split('.') if '.' in str(memory_used[i]) else (memory_used[i], '0'),
    	units=memory_units[i]))

print('='*60)

for i in range(len(job_IDs)):
    print("Job {item:15} {value[0]:>6}{value[1]:1}{value[2]:<3} {units:3}".format(item=job_IDs[i]+':', 
    	value=str(memory_used[i]).partition('.'),
    	units=memory_units[i]))


