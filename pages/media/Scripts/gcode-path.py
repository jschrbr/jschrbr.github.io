import os
import csv

#Rename g-code .nc to .csv then open file path.
fi = open(os.path.expanduser("~/CAM/Codes/G-code/G-code.csv"))
#Read g-code
gcode = csv.reader(fi)
#Create empty .csv, open file path for writing.
fo = open(os.path.expanduser("~/CAM/Codes/Path/path.csv"), "wb")     
# write to csv.
path = csv.writer(fo, delimiter='	', quotechar='"', quoting=csv.QUOTE_NONE)

#For loop, using replace to comma seperate values
for row in gcode:
    row = str(row)
    
    # seperates x and y values with a comma. Comment out when running final path
#    row1 = row.replace( "Y", ", Y" )
#    
#    
##    Uncomment for final path file
##    row12 = row.replace( "Y", ", " )
##    row13 = row12.replace("Z", "0, 0, ")
##    row1 = row13.replace("X", "")
#
#    row2 = row1.replace( "G01" , "")
#    row3 = row2.replace( "G00" , "")
#    
##    Toggle comment for final path
#    row4 = row3.replace( "F", ", F" )
##    row4 = row3.replace( "F", ", " )
#    
#    
#    #Write to .csv
#    path.writerow(row4)
#    print(row4)

    row1 = row.replace(";", ", ")
    row2 = row1.replace("'", "")
    row3 = row2.replace("]", "], ")
    path.writerow(row3)
    print(row3)
    
# close files
fi.close
fo.close