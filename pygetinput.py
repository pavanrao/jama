import sqlite3

input("meaning of life: ")
#x = raw_input("enter a comma seperated string")

conn = sqlite3.connect('jama.db')
c = conn.cursor()

while 1:
	store=raw_input("Enter Store Name: (q to quit)")
	if store in ["Q","q"]: break
	print "Store: "+store
	date=raw_input("enter date(yyyymmdd): ")

	while 1:	
		print("enter comma seperated values of items purchased: \n item,brand,quantity,count,cost,due\n x to quit\n")
		input_str=raw_input("")
		if input_str in ["x","X"]: break
		item,brand,quantity,count,cost,due = input_str.split(',')
		print item,brand,quantity,count,cost 
		c.execute("INSERT INTO purchase_temp  VALUES("+date+",'"+store+"','"+item+"','"+brand+"',"+quantity+","+count+","+cost+",'"+due+"')")
		conn.commit()
conn.close()

