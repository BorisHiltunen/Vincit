from flask import Flask

from App import Application

app2 = Flask(__name__)

@app2.route('/')
def main():
    return "working"
    #return redirect(url_for('/get/getDownTrend/<dates>'))
    #return redirect(url_for('/get/HighestTradingVolume/<dates>'))
    #return redirect(url_for('/get/BuyAndSellDates/<dates>'))

"""@app2.route('/get/getDownTrend/<dates>/')
def getDownTrend(dates):
    return Application.getDownwardTrend1(dates)

@app2.route('/get/HighestTradingVolume/<dates>/')
def getHighestTradingVolume(dates):
    return Application.getDownwardTrend1(dates)

@app2.route('/get/BuyAndSellDates/<dates>/')
def getBuyAndSellDates(dates):
    #print(start,finish)
    #print(finish)
    return Application.getHighestTradingVolume1(dates) 
    #return  '{} {} {}'.format(Application.getHighestTradingVolume1(start, finish))
    #return '{} {}'.format(start, finish)
    #print('{}, {}'.format(start, finish))
    #return Application.getHighestTradingVolume1('{}, {}'.format(start, finish))  """

#start: str, finish:str
#"12-06-2021", "20-05-2021"

@app2.route('/get/DownTrend/')
def getDownTrend():
    return Application.getDownwardTrend1("25-11-2021|30-11-2021")

@app2.route('/get/HighestTradingVolume/')
def getHighestTradingVolume():
    return Application.getDownwardTrend1("25-11-2021|30-11-2021")

@app2.route('/get/BuyAndSellDates/')
def getBuyAndSellDates():
    print(Application.getHighestTradingVolume1("25-11-2021|30-11-2021") )
    return Application.getHighestTradingVolume1("25-11-2021|30-11-2021") 

if __name__ == "__main__":
    app2.run()