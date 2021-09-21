hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#CheckPOint 1
total_price = 0
#CHeckPoint 2
for price in prices:
  total_price += price
  #CheckPoint 3
  average_price = total_price / len(prices)
  #CheckPOint 4
  print("Average Haircut Price:${0}".format (average_price))
  #Checkpoint5
  new_prices = [ price - 5 for price in prices]
  #Checkpoint 6
  print (new_prices)
  #CheckPoint 7
  total_revenue = 0
  #CheckPOint 8
  for i in range (len(hairstyles)):
#CheckPoint9
    total_revenue += prices[i] * last_week[i]
    #Checkpoint 10
  print("Total Revenue:${0}".format (total_revenue))
  #CheckPt 11
  average_daily_revenue = total_revenue / 7
  print(average_daily_revenue)
  #CheckPt 12
  cuts_under_30 = [hairstyles[i] for i in range (len(hairstyles)) if new_prices[i] < 30]