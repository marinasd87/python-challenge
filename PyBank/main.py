#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:40:45 2020

@author: marinaduarte
"""

import csv


        
with open ('/Users/marinaduarte/Documents/python-challenge/PyBank/Resources/budget_data.csv','r') as csvFile:
    csvreader = csv.reader(csvFile)

    header = next(csvreader)
    PL = []
    date = []
    pl_change = []

    #Calculate total months and total amount
    for row in csvreader:

        PL.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $",sum(PL))


    #Calculate average
    for i in range(0,len(PL)):
        pl_change.append(PL[i] - PL[i-1])   
        avg_pl_change = sum(pl_change)/len(pl_change)
        
        #calculate max and min pl change
        max_pl_change = max(pl_change)

        min_pl_change = min(pl_change)
        
        #Getting date of max and min
        max_pl_change_date = str(date[pl_change.index(max(pl_change))])
        min_pl_change_date = str(date[pl_change.index(min(pl_change))])


    print("Average Change: $",round(avg_pl_change))
    print("Greatest Increase in Profits:", max_pl_change_date,"($",max_pl_change,")")
    print("Greatest Decrease in Profits:", min_pl_change_date,"($",min_pl_change,")")


#Calculate the change
#for row in csvreader:
    #prevmonth_row = csvreader[row[0]]
    #prevmonth_pl = prevmonth_row[1]
    #nextmonth_row = csvreader[row + 1]
    #nextmonth_pl = nextmonth_row[1]
        
    #monthly_change = nextmonth_pl - prevmonth_pl
    #row.append("ChangePL")
    #csvwriter.writerow(monthly_change)
        
        
#with open ('/Users/marinaduarte/Documents/python-challenge/PyBank/Resources/budget_data_1.csv','r') as csvFile2:   
     #csvreader2 = csv.reader(csvFile2)
     #header = next(csvreader2)
     #for row in csvreader:
         #tot = sum([int(row[2]) for row in csvreader2])
         #count = sum(1 for line in csvreader2)
         #average = tot / count
         
         #print(f"Average Change: {average}")
         
#Create a function?
#def greatest_increase():
    #with open ('/Users/marinaduarte/Documents/python-challenge/PyBank/Resources/budget_data_1.csv','r') as csvFile2:   
     #csvreader2 = csv.reader(csvFile2)
     #header = next(csvreader2)
     #for row in csvreader2:
         #date1 = row[0]
         #change1 = row[2]
         #print(f" {date1} ($ {change1} )")

         #print("Greatest Increase in Profits: " + str(greatest_increase(max(change1))))         
         #print("Greatest Increase in Profits: " + str(greatest_increase(min(change1))))
         
txtfile = open('/Users/marinaduarte/Documents/python-challenge/PyBank/results.txt', 'w') 
print("Financial Analysis", file = txtfile)
print("-----------------------------------", file = txtfile)
print("Total Months:", len(date), file = txtfile)
print("Total: $", sum(PL), file = txtfile)
print("Average Change: $", round(avg_pl_change), file = txtfile)
print("Greatest Increase in Profits:", max_pl_change_date,"($", max_pl_change,")", file = txtfile)
print("Greatest Decrease in Profits:", min_pl_change_date,"($", min_pl_change,")", file = txtfile)
txtfile.close()