
work_hours=[("Okey",300),("Santos",350),("Jezive",650),("Onyeka",200)]

def employee_check(work_hours):
	current_max=0
	employee_of_the_month=''

	for employee,hours in work_hours:
		if hours>current_max:
			current_max=hours
			employee_of_the_month=employee
		else:
			pass
	#final_result='The employee of the month is '+employee_of_the_month+' : '+str(current_max)+'hrs'
	return(employee_of_the_month,current_max)

employee,hours=employee_check(work_hours)
print(f"The employee of the month is {employee}, with a total work hours of {hours}hrs")
	
	