import os
import csv
#make sure I can open file before starting
csvpath= os.path.join('/Users/stevene/Desktop/python_challenge/PyBank/budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
   #skip header
    csv_header = next(csvreader)
    month = []
    revenue = []
    revenue_delta = []
    monthly_change = []
    
    print(f"Header: {csv_header}")  
#Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 # append profit_loss
        revenue_delta.append(profit_loss)
    Total = sum(revenue_delta)
  
    monthly_change = Total / len(revenue_delta)
    print(monthly_change)
    
    
#Greatest Increase/decrease
    profit_inc = max(revenue_delta)
    print(profit_inc)
    x = revenue_delta.index(profit_inc)
    month_inc = month[x+1]
    

    profit_dec = min(revenue_delta)
    print(profit_dec)
    y = revenue_delta.index(profit_dec)
    month_dec = month[y+1]


#Print Results 

print(f'Financial Analysis')

print(f'----------------------------')


print("Total Months: " + str(len(month)))

print("Total Revenue: $ " + str(total_revenue))
      
print("Average Change : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_inc} (${profit_inc})")

print(f"Greatest Decrease in Profits: {month_dec} (${profit_dec})")


print(f'-------------------------------')
 
#Use ex 5 from 2 session
#print .txt!!!!! This took for ever to figure out all I was missing was line85 :/  
PyBank_txt = os.path.join('/Users/stevene/Desktop/python_challenge/PyBank/PyBank.txt')
with open (PyBank_txt, 'w', newline='') as text:
    write = csv.writer(text)
    write.writerows([
            ["Financial Analysis for budget_data.csv"],
            ["-------------------------------------"],
            ["Total Revenue: $" + str(total_revenue)],
            ["Total Months:" + str(len(month))],
            ["Average Revenue Change:" + str(monthly_change)],
            ["Greatest Increase in Profit:" + str(month_inc) + "($ " + str(profit_inc) + ")"],
            ["Greatest Increase in Profit:" + str(month_dec) + "($ " + str(profit_dec) + ")"]])

print(write)
