x = 99

for i in range(0,99):
    if i == 98:
        print "{:d} bottle of beer on the wall, {:d} bottle of beer. \n Take one down, pass it around. \n Now there are no more bottles of beer on the wall.".format(x-i,x-i)
    elif i == 97:
        print "{:d} bottles of beer on the wall, {:d} bottles of beer. \n Take one down, pass it around. \n Now there is {:d} bottle of beer on the wall.".format(x-i,x-i, x-i-1)
    else:
        print "{:d} bottles of beer on the wall, {:d} bottles of beer. \n Take one down, pass it around. \n Now there are {:d} bottles of beer on the wall.".format(x-i,x-i,x-i-1)
