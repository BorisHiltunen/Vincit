# This time Scrooge has his eyes on cryptocurrency — bitcoin to be exact — and he needs a tool to
#analyze its market value for a given date range.

#Your mission, should you choose to accept it, is to create an application that meets Scrooge’s needs.
#You are free to use any technology of your choosing. The resulting application can be for example a web
#page, an API backend, a mobile application, or anything else you deem suitable.

#Additional information:
#● Both start and end dates should be included in a date range.
#● A day’s price means the price at 00:00 UTC time (use price data from as close to midnight as
#possible as the day’s price, if you don’t have a datapoint from exactly midnight).
#● Allow the user of your application to pass the start and end dates of the date range in some way,
#e.g. via input fields in a UI or as parameters to an API.

#A. How many days is the longest bearish (downward) trend within a given date range?
#● Definition of a downward trend shall be: “Price of day N is lower than price of day N-1”
#● Expected output: The maximum amount of days bitcoin’s price was decreasing in a row.
#Example: In bitcoin’s historical data from CoinGecko, the price decreased 3 days in a row for the
#inputs from 2020-01-19 and to 2020-01-21, and the price decreased for 5 days in a row for the
#inputs from 2020-03-01 and to 2021-08-01.

#B. Which date within a given date range had the highest trading volume?
#● Expected output: The date with the highest trading volume and the volume on that day in
#euros.

#C. Scrooge has access to Gyro Gearloose’s newest invention, a time machine. Scrooge
#wants to use the time machine to profit from bitcoin. The application should be able to tell
#for a given date range, the best day for buying bitcoin, and the best day for selling the
#bought bitcoin to maximize profits. If the price only decreases in the date range, your
#output should indicate that one should not buy (nor sell) bitcoin on any of the days. You
#don't have to consider any side effects of time travel or how Scrooge's massive purchases
#would affect the price history.
#● Expected output: A pair of days: The day to buy and the day to sell. In the case when one
#should neither buy nor sell, return an indicative output of your choice.

#Use CoinGecko’s public API to get the needed data
#https://www.coingecko.com/en/api/documentation

#You will only need to use the /coins/{id}/market_chart/range endpoint. Read its
#documentation to understand how it works. Note that the API returns data with different granularity
#depending on the date range's length. Tip: You should add 1 hour to the `to` input to make sure
#that you always get data for the end date as well. Scrooge’s Money Bin only holds euros, so that is
#the only fiat currency you need to consider.

#For example, the following URL can be used to fetch bitcoin’s price, market cap and volume information
#in euros (€) from January 1, 2020 to December 31, 2020:
#https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_c
#urrency=eur&from=1577836800&to=1609376400

#The answer must be returned as:
#● A link to a public Git repo in a hosting service of your choice (GitHub, GitLab etc.)
#OR
#● A Git bundle (You can create a bundle file from your repo by running: git bundle create
#myreponame.bundle --all)

#What we value:
#● Clean code
#● Ease of use — Either host your solution somewhere where it can be used immediately, or include
#clear directions (e.g. in a README file) for running your solution.
#● Simplicity — Minimize the use of external libraries and dependencies. We want to see how you
#manage with a programming language of your choice, not how many packages you are able to
#import. You are of course highly encouraged to use any conveniences or standard library utilities
#that ship with your chosen language. It's also fine to build your solution around a single 3rd party
#library or framework, if that adds value to your solution.
#● Extensibility — Scrooge only wants these three features for now, but very likely wants to hire us
#to add capabilities to the application after it has proved its value to him.

#Vincit will review the code, and we like readable and maintainable code that follows good coding
#conventions. You may ask if you have any questions. Have fun coding!

#Code starts here!

#Venv is needed for the module to work

#How to get the data:
from datetime import datetime, date
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

#Correct way to use datetime date delta
#start_date = datetime.date(2020, 1, 1)
#end_date = datetime.date(2020, 1, 4)
#delta = datetime.timedelta(days=1)

#missions
#1. downward trend
#2. Highest trading volume
#3. Time machine

#IMPORTANT
#1 day from query time = 5 minute interval data
#1 - 90 days from query time = hourly data
#above 90 days from query time = daily data (00:00 UTC)

#1 hour = 3600
#day = 86400
#week = 604800
#month = 2629743

day = 0
month = 0
year = 0
point = f"{day}-{month}-{year}"
#Test
#print(point)

class Application:
    def __init__(self):
        pass
    def time(self):
        pass
    def processTime(self, date):
        pass
    #Maybe not needed
    def getDays(self, start: str, finish: str):
        year1 = f"{start[6]}{start[7]}{start[8]}{start[9]}"
        year2 = f"{finish[6]}{finish[7]}{finish[8]}{finish[9]}"
        month1 = f"{start[3]}{start[4]}"
        month2 = f"{finish[3]}{finish[4]}"
        day1 = f"{start[0]}{start[1]}"
        day2 = f"{finish[0]}{finish[1]}"

        d1 = date(int(year1), int(month1), int(day1))
        d2 = date(int(year2), int(month2), int(day2))
        minus = d1 - d2
        amount = ""
        if str(minus)[0] == "-":
            for letter in str(minus):
                if letter == "d":
                    break
                elif letter == "-":
                    continue
                else:
                    amount = amount + letter
        #+1 since the first day counts too
        return int(amount) + 1

    def correctFormForDatetime(self, date):
        year = f"{date[6]}{date[7]}{date[8]}{date[9]}"
        month = f"{date[3]}{date[4]}"
        day = f"{date[0]}{date[1]}"
        #is tuple and should be integer?
        return int(year), int(month), int(day)

    def correctFormForDatetime2(self, day, month, year):
        #is tuple and should be integer?
        return int(year), int(month), int(day)

    def correctFormForCrypto(self, year, month, day):
        return f"{day}-{month}-{year}"

    def correctFormForCrypto2(self, day, month, year):
        stime = f"{day}/{month}/{year}"
        timestamp = datetime.strptime(stime, "%d/%m/%Y").timestamp()
        return timestamp

    def correctFormForCrypto3(self, date):

        year = f"{date[6]}{date[7]}{date[8]}{date[9]}"
        month = f"{date[3]}{date[4]}"
        day = f"{date[0]}{date[1]}"

        stime = f"{day}/{month}/{year}"
        timestamp = datetime.strptime(stime, "%d/%m/%Y").timestamp()
        return timestamp

    def convertTimestampToDate(self, timestamp):
        #print(timestamp)
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object

    def correctDateForm(self, date):
        new_date = str(date)
        year = f"{new_date[0]}{new_date[1]}{new_date[2]}{new_date[3]}"
        month = f"{new_date[5]}{new_date[6]}"
        day = f"{new_date[8]}{new_date[9]}"

        correctForm = f"{day}-{month}-{year}"
        return correctForm

#!1!

    #Downward trend
    def getDownwardTrend1(self, start, finish):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        count = 0

        start_date = datetime.date(self.correctFormForDatetime(start)[0], self.correctFormForDatetime(start)[1], self.correctFormForDatetime(start)[2])
        end_date = datetime.date(self.correctFormForDatetime(finish)[0], self.correctFormForDatetime(finish)[1], self.correctFormForDatetime(finish)[2])
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            #print(self.correctDateForm(start_date))
            start_date += delta
            data = cg.get_coin_history_by_id(id='bitcoin',date=self.correctDateForm(start_date))
            #print(data["market_data"]["current_price"]["eur"])
            list1.append(data["market_data"]["current_price"]["eur"])
        
        #print("1")
        #print(list1)

        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] > list1[count]:
                    list2.append(list1[count])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list2 = []
            else:
                if list1[count] > list1[count+1] and count < len(list1):
                    if list1[count] not in list2:
                        list2.append(list1[count])
                    list2.append(list1[count+1])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list2 = []
            count += 1
        #print("1")
        #print(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)
        #print(list4)
        

    #Downward trend
    def getDownwardTrend2(self, year1, month1, day1, year2, month2, day2):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        count = 0

        start_date = datetime.date(year1, month1, day1)
        end_date = datetime.date(year2, month2, day2)
        delta = datetime.timedelta(days=1)

        while start_date <= end_date:
            #print(self.correctDateForm(start_date))
            start_date += delta
            data = cg.get_coin_history_by_id(id='bitcoin',date=self.correctDateForm(start_date))
            #print(data["market_data"]["current_price"]["eur"])
            list1.append(data["market_data"]["current_price"]["eur"])
        
        #print("1")
        #print(list1)

        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] > list1[count]:
                    list2.append(list1[count])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list2 = []
            else:
                if list1[count] > list1[count+1] and count < len(list1):
                    if list1[count] not in list2:
                        list2.append(list1[count])
                    list2.append(list1[count+1])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list2 = []
            count += 1
        #print("1")
        #print(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)
        #print(list4)

#!2!

    #Downward trend
    def getDownwardTrend3(self, start, finish):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        count = 0
        most = 0

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=start, to_timestamp=finish)
        for price in data["prices"]:
            list1.append(price[1])

        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] > list1[count]:
                    list2.append(list1[count])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list5.append((len(list2), "-1", list2))
                    list2 = []
            else:
                if list1[count] > list1[count+1]:
                    if list1[count] not in list2:
                        list2.append(list1[count])
                    list2.append(list1[count+1])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list5.append((len(list2), "-1", list2))
                    list2 = []
            count += 1

        #print("1")
        #rint(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)
        #print("4")
        #print(list4)
        #print("5")
        #print(list5)

        for quantity in list3:
            if quantity > most:
                most = quantity
        return most

    #Downward trend
    def getDownwardTrend4(self, year1, month1, day1, year2, month2, day2):

        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        count = 0
        most = 0

        date1 = self.correctFormForCrypto2(day1, month1, year1)
        date2 = self.correctFormForCrypto2(day2, month2, year2)

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)
        for price in data["prices"]:
            list1.append(price[1])
        
        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] > list1[count]:
                    list2.append(list1[count])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list5.append((len(list2), list2))
                    list2 = []
            else:
                if list1[count] > list1[count+1]:
                    if list1[count] not in list2:
                        list2.append(list1[count])
                    list2.append(list1[count+1])
                else:
                    #print(count)
                    #print(list2)
                    list3.append(len(list2))
                    list4.append((count, list2))
                    list5.append((len(list2), list2))
                    list2 = []
            count += 1

        #print("1")
        #print(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)
        #print("4")
        #print(list4)
        #print("5")
        #print(list5)

        for quantity in list3:
            if quantity > most:
                most = quantity
        return most

    def getHighestTradingVolume(self, start, finish):

        highest = 0

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=start, to_timestamp=finish)
        for volume in data["total_volumes"]:
            if volume[1] > highest:
                highest = volume[1]
        return highest
    
    def getHighestTradingVolume2(self, year1, month1, day1, year2, month2, day2):

        date1 = self.correctFormForCrypto2(day1, month1, year1)
        date2 = self.correctFormForCrypto2(day2, month2, year2)

        highest = 0

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)
        for volume in data["total_volumes"]:
            if volume[1] > highest:
                highest = volume[1]
        return highest

    #remember to add 1 hour to the to_timestamp
    def whenToBuyAndSell1(self, start, finish):
        pass
    def whenToBuyAndSell2(self, year1, month1, day1, year2, month2, day2):

        list1 = []
        list2 = []
        list3 = []
        count = 0
        most = 0
        sum = 0

        date1 = self.correctFormForCrypto2(day1, month1, year1)
        date2 = self.correctFormForCrypto2(day2, month2, year2)

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)
        for price in data["prices"]:
            list1.append(price[1])
        
        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] > list1[count]:
                    list2.append(list1[count])
                else:
                    for price in list2:
                        sum += price
                    list3.append(sum)
                    list2 = []
                    sum = 0
            else:
                if list1[count] > list1[count+1]:
                    if list1[count] not in list2:
                        list2.append(list1[count])
                    list2.append(list1[count+1])
                else:
                    for price in list2:
                        sum += price
                    list3.append(sum)
                    list2 = []
                    sum = 0
            count += 1

        #print("1")
        #print(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)

        for amount in list3:
            if amount > most:
                most = amount
        return most
    def whenToBuyAndSell3(self, start: str, finish:str):

        list1 = []
        list2 = []
        list3 = []
        count = 0
        most = (0, 0)
        sum = 0

        now = datetime.now()

        date1 = self.correctFormForCrypto3(start)
        date2 = self.correctFormForCrypto3(finish)
        if date2 != now.strftime("%d-%b-%Y (%H:%M:%S.%f)"):
            date2 += 3600
        date3 = self.correctFormForCrypto3(start)

        #print(date3)
        #print(self.convertTimestampToDate(date3))

        #hours_added = datetime.timedelta(hours = hours)
        #future_date_and_time = date3 + hours_added
        #print(future_date_and_time)
        #print(date3)
        #print(hours_added)
        #print(future_date_and_time)

        #Think how to get the dates for the prices

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)
        for price in data["prices"]:
            list1.append(price[1])

        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] > list1[count]:
                    list2.append(list1[count])
                    date3 = date3 + 3600.0
                    list3.append((date3, sum))
                    list2 = []
                    sum = 0
                else:
                    for price in list2:
                        sum += price
                    date3 = date3 + 3600.0
                    list3.append((date3, sum))
                    list2 = []
                    sum = 0
            else:
                if list1[count] > list1[count+1]:
                    if list1[count] not in list2:
                        list2.append(list1[count])
                    list2.append(list1[count+1])
                else:
                    for price in list2:
                        sum += price
                    list3.append((date3, sum))
                    list2 = []
                    sum = 0
            date3 = date3 + 3600.0
            count += 1

        #print(len(list1))
        #print(date3)
        #print(date3 - date2)
        #print(self.convertTimestampToDate(date3))

        #print("1")
        #print(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)

        for amount in list3:
            #print(amount)
            print(self.convertTimestampToDate(amount[0]))
            print(amount[1])
            if amount[1] > most[1]:
                most = amount
        return (self.convertTimestampToDate(most[0]), most[1])

    #if more than 6 days +1 hour
    def whenToBuyAndSell4(self, year1, month1, day1, year2, month2, day2):

        list1 = []
        list2 = []
        list3 = []
        count = 0
        most = (0, 0, 0, 0, 0)
        sum = 0

        now = datetime.now()

        date1 = self.correctFormForCrypto2(day1, month1, year1)
        date2 = self.correctFormForCrypto2(day2, month2, year2)
        if date2 != now.strftime("%d-%b-%Y (%H:%M:%S.%f)"):
            date2 += 3600
        date3 = self.correctFormForCrypto2(day1, month1, year1)

        #print(date3)
        #print(self.convertTimestampToDate(date3))

        #hours_added = datetime.timedelta(hours = hours)
        #future_date_and_time = date3 + hours_added
        #print(future_date_and_time)
        #print(date3)
        #print(hours_added)
        #print(future_date_and_time)

        #Think how to get the dates for the prices

        number = 0

        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)
        for price in data["prices"]:
            list1.append(price[1])

        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] < list1[count]:
                    list2.append(list1[count])
                    date3 = date3 + 3600.0
                    list3.append(tuple(("sell", date3, sum)))
                    list2 = []
                    sum = 0
                else:
                    for price in list2:
                        if number == 0:
                            sum += price
                        elif number == len(list2)-1:
                            sum = price - sum
                        number += 1
                        
                    date3 = date3 + 3600.0
                    list3.append(tuple(("sell", date3, sum)))
                    list2 = []
                    sum = 0
                    number = 0
            else:
                if list1[count] > list1[count+1]:
                    if list1[count] not in list2:
                        list2.append(list1[count])
                        list3.append(tuple(("buy", date3, sum)))
                    list2.append(list1[count+1])
                else:
                    for price in list2:
                        if number == 0:
                            sum += price
                        elif number == len(list2)-1:
                            sum = price - sum
                            print(sum)
                        number += 1

                    list3.append(tuple(("sell", date3, sum)))
                    list2 = []
                    number = 0
                    sum = 0
            date3 = date3 + 3600.0
            count += 1

        #print(len(list1))
        #print(date3)
        #print(date3 - date2)
        #print(self.convertTimestampToDate(date3))

        #print("1")
        #print(list1)
        #print("2")
        #print(list2)
        #print("3")
        #print(list3)

        this_one = (0, 0, 0)

        for amount in list3:
            #print(amount)
            #print(self.convertTimestampToDate(amount[0]))
            #print(amount[2])
            if amount[0] == "buy":
                this_one = amount
            if amount[2] > most[4]:
                most = (this_one[0], this_one[1], amount[0], amount[1], amount[2])
                print(most[0], self.convertTimestampToDate(most[1]), most[2], self.convertTimestampToDate(most[3]), most[4])
        return (most[0], self.convertTimestampToDate(most[1]), most[2], self.convertTimestampToDate(most[3]), most[4])

    #Vaan upward trend
    def whenToBuyAndSell5(self, year1, month1, day1, year2, month2, day2):

        list1 = []
        list2 = []
        list3 = []
        count = 0
        most = (0, 0, 0, 0, 0)
        sum = 0
        number = 0

        now = datetime.now()
        date1 = self.correctFormForCrypto2(day1, month1, year1)
        date2 = self.correctFormForCrypto2(day2, month2, year2)

        if date2 != now.strftime("%d-%b-%Y (%H:%M:%S.%f)"):
            date2 += 3600

        date3 = self.correctFormForCrypto2(day1, month1, year1)
        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)

        for price in data["prices"]:
            list1.append(price[1])

        #while count < len(list1):
        #    if count == len(list1)-1:
        #        pass
        #    else:
        #        if list1[count-1] > list1[count]:
        #            pass
        #    count += 1

        while count < len(list1):
            if count == len(list1)-1:
                if list1[count-1] < list1[count]:
                    list2.append(list1[count])
                    date3 = date3 + 3600.0
                    list3.append(tuple(("sell", date3, sum)))
                    list2 = []
                    sum = 0
                else:
                    for price in list2:
                        if number == 0:
                            sum += price
                        elif number == len(list2)-1:
                            sum = price - sum
                        number += 1
                        
                    date3 = date3 + 3600.0
                    list3.append(tuple(("sell", date3, sum)))
                    list2 = []
                    sum = 0
                    number = 0
            else:
                if list1[count] < list1[count+1]:
                    if list1[count] not in list2:
                        list2.append(list1[count])
                        list3.append(tuple(("buy", date3, sum)))
                    list2.append(list1[count+1])
                else:
                    for price in list2:
                        if number == 0:
                            sum += price
                        elif number == len(list2)-1:
                            sum = price - sum
                            print(sum)
                        number += 1

                    list3.append(tuple(("sell", date3, sum)))
                    list2 = []
                    number = 0
                    sum = 0
            date3 = date3 + 3600.0
            count += 1

        this_one = (0, 0, 0)

        for amount in list3:
            if amount[0] == "buy":
                this_one = amount
            if amount[2] > most[4]:
                most = (this_one[0], this_one[1], amount[0], amount[1], amount[2])
                print(most[0], self.convertTimestampToDate(most[1]), most[2], self.convertTimestampToDate(most[3]), most[4])
        return (most[0], self.convertTimestampToDate(most[1]), most[2], self.convertTimestampToDate(most[3]), most[4])

    def whenToBuyAndSell6(self, year1, month1, day1, year2, month2, day2):

        list1 = []
        list2 = []
        count = 0

        now = datetime.now()
        date1 = self.correctFormForCrypto2(day1, month1, year1)
        date2 = self.correctFormForCrypto2(day2, month2, year2)

        if date2 != now.strftime("%d-%b-%Y (%H:%M:%S.%f)"):
            date2 += 3600

        date3 = self.correctFormForCrypto2(day1, month1, year1)
        date4 = self.correctFormForCrypto2(day1, month1, year1)
        data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=date1, to_timestamp=date2)

        for price in data["prices"]:
            list1.append(price[1])

        #Think about the dates
        #Why is the lowest 27?
        print(self.convertTimestampToDate(date3))
        lowest = "buy", date3, 1000000000
        while count < len(list1):
            if list1[count] < lowest[2]:
                lowest = "buy", date3, list1[count]
            date3 += 3600
            date4 += 3600
            count += 1
        print(self.convertTimestampToDate(date3))
        print(self.convertTimestampToDate(lowest[1]))
        
        #IMPORTANT
        #from_timestamp
        #to_timestamp
        data2 = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=lowest[1], to_timestamp=date2)
        
        for price in data2["prices"]:
            list2.append(price[1])
        
        count = 0
        highest = "sell", date4, 0
        while count < len(list2):
            if list2[count] > highest[2]:
                highest = "sell", date4, list1[count]
            date4 = date4 + 3600.0
            count += 1

        answer = (lowest[0], self.convertTimestampToDate(lowest[1]), lowest[2], highest[0], self.convertTimestampToDate(highest[1]), highest[2])

        return answer

if __name__ == "__main__":
    app = Application()
    #app.getDownwardTrend1("01-12-2020", "03-12-2020")
    start = (2020, 1, 1)
    finish = (2020, 1, 4)
    #app.getDownwardTrend2(2020, 1, 1, 2020, 1, 15)
    #print(app.getDays("13-07-2020", "24-07-2020"))
    #print(app.correctDateForm("2020-01-04"))
    #app.getHighestTradingVolume("01-12-2020", "03-12-2020")
    #app.getHighestTradingVolume2(2020, 1, 1, 2020, 1, 15)

    #IMPORTANT
    #if stime = "30/10/2021"
    # and stime2 = "30/11/2021"
    #data shows 747 hours 
    #Meaning there are 3 too many
    #and now its 21 a clock so does that matter?

    #btw it seems that every week there is one hour more
    #why?
    #IMPORTANT

    stime = "29/11/2021"
    stime2 = "30/11/2021"
    #stime2 = "30/11/2021"
    timestamp1 = datetime.strptime(stime, "%d/%m/%Y").timestamp()
    timestamp2 = datetime.strptime(stime2, "%d/%m/%Y").timestamp()
    data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp=timestamp1, to_timestamp=timestamp2)
    #data = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='eur', from_timestamp='1577836800', to_timestamp='1609376400')
    #print(len(data["prices"]))
    #print(data)

    #Doesn't work but maybe not needed?
    #print(app.getDownwardTrend1(timestamp1, timestamp2))
    #print(app.getDownwardTrend2(2021, 11, 29, 2021, 11, 30))

    #print(app.getDownwardTrend3(timestamp1, timestamp2))
    #print(app.getDownwardTrend4(2021, 11, 29, 2021, 11, 30))
    #print(app.getHighestTradingVolume(timestamp1, timestamp2))
    #print(app.getHighestTradingVolume2(2021, 11, 29, 2021, 11, 30))
    #app.whenToBuyAndSell1(stime, stime2)
    #app.whenToBuyAndSell2(2021, 11, 29, 2021, 11, 30)
    #print(app.whenToBuyAndSell3("29-11-2021", "30-11-2021"))
    #print(app.whenToBuyAndSell4(2021, 11, 29, 2021, 11, 30))

    print(app.whenToBuyAndSell6(2021, 11, 25, 2021, 11, 30))

    #print(app.convertTimestampToDate(timestamp1))