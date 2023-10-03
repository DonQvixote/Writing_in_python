import os
import csv

output_path = os.path.join('.','new.csv')

with open(output_path,'w',newline='') as my_file:
    my_writer= csv.writer(my_file)

    my_writer.writerows([['id','Name','SSN'],
        ['1','Jose','1222'], ['2','Andres','4587'],['3','Sofia','2599']])

