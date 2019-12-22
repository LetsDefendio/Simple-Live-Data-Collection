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
"userAccounts":"cat /etc/passwd",
"groups":"cat /etc/group",
"routingTable":"netstat",
"networkConnections":"netstat -anp",
"loadedDrivers":"lsmod",

}


def getValue(command):
	value = getData(options[command])
	return(value)


def collectData(select):
	
	if select == "systemDate":
		command = "date"

	elif select == "osVersion":
		command = "cat /etc/issue"

	elif select == "kernelVersion":
		pass

	return(getData(command))


#print(collectData("osVersion"))

