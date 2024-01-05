#!/usr/bin/python3


blocks = ( 'A','B','C','1','2','3','4','J','5','6','7','8' )
yr = 2017
bidx = 3
ayr = "%d-%d"%(yr,yr+1)
while yr<2024 or bidx!=0:
    print("insert into academic_cal (block, year, academic_yr) VALUES ('%s',%d,'%s');"%(blocks[bidx],yr,ayr))
    bidx = (bidx+1)%len(blocks);
    if bidx == 9:
        yr+=1
    if bidx == 0:
        ayr = "%d-%d"%(yr,yr+1)
