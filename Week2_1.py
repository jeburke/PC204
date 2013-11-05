def print_range(start, end):
    if start < end:
        print start
        start += 1
        print_range(start, end)
    elif end < start:
        print end
        end += 1
        print_range(start, end)
    else:
        print end
    
#start = 9
#end = 4
#print_range(start, end)

startString = raw_input("Enter start number:")
start = int(startString)
endString = raw_input("Enter end number:")
end = int(endString)
print_range(start, end)
