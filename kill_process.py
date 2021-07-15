import os

def tasklist_result(command):
	result = os.popen(command,'r')
	result_print = result.read()
	return result_print

def taskkill_result(kill_command,pid):
	kill_command_x = kill_command + str(pid)
	kill_result = os.popen(kill_command_x,'r')
	kill_result_print = kill_result.read()
	return kill_result_print


if __name__ == '__main__':
	# application_name = input("input process name：") 
	application_name = 'Motrix'
	command = "tasklist | findstr {}".format(application_name)
	kill_command = "taskkill /t /f /im "
	result_print = tasklist_result(command)
	if len(result_print) == 0:
		print("{}相关进程不存在".format(application_name))
		exit()
	else:
		print(result_print)
	pid = result_print.split(' ')
	pid = [i for i in pid if(len(str(i)) !=0 )] #去掉list中的空元素，那么第二个元素就一定是pid
	print(pid)
	try:
		for i in range(1,len(pid)+1,5):
			kill_result_print = taskkill_result(kill_command,pid[i])
			# print(kill_result_print)
			if len(kill_result_print) == 0:
				print("{}相关进程已经被删除".format(application_name))
			else:
				print(kill_result_print)
	except:
		 print("kill process{} end".format(application_name))
