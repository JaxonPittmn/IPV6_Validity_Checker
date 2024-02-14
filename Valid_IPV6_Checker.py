
acceptableDigits = ["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

alreadyDone = False

def Challenge():
	addressLenChecker = ""
	address = input("Enter An IPv6 Address:\n")
	print(" ")

	if ":" in address:
		address = address.split(":")
	else:
		return False

	for group in address:
		for i in range((4 - len(group))):
			currGroup = address.index(group)
			group = "0" + group
			address[currGroup] = group

	for group in address:
		for letter in group:
			addressLenChecker += letter
			
	if not len(addressLenChecker) <= 32:
		return False
	
	for group in address:
		for letter in group:
			if letter in acceptableDigits:
				continue
			else:
				return False
	return True
	
if Challenge():
	print("CORRECT")
	alreadyDone = True
else:
	print("WRONG")
	alreadyDone = True