# If Else statement
if 5<2:
	print("Greater")
else:
	print("Smaller")

# If Else Statement in Single Line
print("Greater") if 5<2 else print("Smaller")

# If Else Statement with Rest of the Code
if 5<2:
	print("Greater")
else:
	print("Smaller")
print("Rest of The Code")

# If Else Statement with Group of Statement
if 5<2:
	print("Greater")
	print("5 is greater than 2")
else:
	print("Smaller")
	print("Statement 2")
print("Rest of The Code")

# Nested If  Else Statement
a = 5
b = 2
c = 6
d = 3
if a>b:
	print("a is greater than b")
	if(c>d):
		print("c is Greater than d")
	else:
		print("d is Greater than c")
else:
	print("b is greater than a")
print("Rest of The Code")

# If Else statement with Logical Operator
if 5>2 and 7<3:
	print("If statement with Logical Operator")
	print("Statement 2")
else:
	print("Else Statement")
print("Rest of the Code")

			