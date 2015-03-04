import sys

def calc (number, result):
	if number == 0:
		results.append(result)
		return
	elif (number % 2) == 0: # even
		# end with 0
		calc(number / 2, "0" + result)
		# end with 2 
		calc((number - 2) / 2, "2" + result)
	else: # odd
		# end with 1
		calc((number - 1) / 2, "1" + result)

if (len(sys.argv) < 2):
	print "You must specify the search term."
else:
	results = []
	calc(int(sys.argv[1]), "")
	print results
	
