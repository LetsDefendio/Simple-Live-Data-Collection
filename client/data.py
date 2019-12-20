import subprocess



def getData(command):
	command = command.split()
	data = subprocess.check_output(command)
	return(data)


options = {
"systemDate":"date",
"osVersion":"cat /etc/issue",
"kernelVersion":"uname -a",
"uptime":"w",

}


a=getData(options["kernelVersion"])
print(a)

def collectData(select):
	
	if select == "systemDate":
		command = "date"

	elif select == "osVersion":
		command = "cat /etc/issue"

	elif select == "kernelVersion":
		pass

	return(getData(command))


#print(collectData("osVersion"))


