import sys,re

if (len(sys.argv) < 2):
	print "You must specify the search term."
else:
	# read file into string; python will close file by itself
	text = open("macbeth.txt").read()
	# seperate text by blank lines into chunks
	chunks = text.split("\n\n")
	for chunk in chunks:
		# if search text is in chunk
		if (re.search(r'%s' % sys.argv[1], chunk)):
			# print all lines that start with 4 spaces
			# -> remove character- and offtext
			print ''.join(re.findall(r'\s{4}.*', chunk))