

coins = [.25 , .1 , .05 , .01]

change = raw_input("")
change = float(change)
change = round(change , 2)
print "Rounded" , change
dollars = int(change)
print "Dollars " ,dollars
change = change - dollars
print "Total change " , change