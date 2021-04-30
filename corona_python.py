from pandas import read_csv
from datetime import datetime

class counter():

	def update(self, country):
		self.minues = 1

		self.day = str(datetime.now().day-self.minues)
		self.month = str(datetime.now().month)
		self.year = str(datetime.now().year)

		if len(self.day) == 1:
		    self.day = "0" + self.day

		if len(self.month) == 1:
		    self.month = "0" + self.month

		self.date = "{}-{}-{}".format(self.month, self.day, datetime.now().year)

		try:
			self.newUrl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(self.date)

			self.newData=read_csv(self.newUrl)
		except:
			self.date = self.older(self.minues)
			self.newUrl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(self.date)

			self.newData=read_csv(self.newUrl)	

		try:
			self.date = self.older(self.minues)
			self.oldUrl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(self.date)

			self.oldData=read_csv(self.oldUrl)
		except:
			self.date = self.older(self.minues)
			self.oldUrl = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{}.csv".format(self.date)

			self.oldData=read_csv(self.oldUrl)

		self.dailyCase = self.dailyCovidData(country , 'Confirmed')
		self.dailyDeath = self.dailyCovidData(country, 'Deaths')
		self.dailyRecovered = self.dailyCovidData(country, 'Recovered')

		self.totalCase = self.covidData(country, 'Confirmed')
		self.totalDeath = self.covidData(country, 'Deaths')

	def older(self, minues):
		self.minues +=1
		self.day = str(datetime.now().day-self.minues)
		if len(self.day) == 1:
		    self.day = "0" + self.day	
		self.date = "{}-{}-{}".format(self.month, self.day, datetime.now().year)
		return self.date	

	def dailyCovidData(self, country, reqiredData):
		newData = self.newData.loc[self.newData['Country_Region'] == country]

		newTotal = 0

		for data in newData[reqiredData]:
			newTotal += data

		oldData = self.oldData.loc[self.oldData['Country_Region'] == country]

		oldTotal = 0

		for confirm in oldData[reqiredData]:
			oldTotal += confirm

		return int(newTotal - oldTotal)

	def covidData(self, country, reqiredData):
		newData = self.newData.loc[self.newData['Country_Region'] == country]

		newTotal = 0

		for data in newData[reqiredData]:
			newTotal += data

		return int(newTotal)

if __name__ == '__main__':
	cnt = input('Country: ')
	corona = corona(cnt)
	print('Daily Cases: {}\nDaily Deaths: {}\nDaily Recovereds: {}\nTotal Cases: {}\nTotal Deaths: {}'.format(
		corona.dailyCase, corona.dailyDeath, corona.dailyRecovered, corona.totalCase, corona.totalDeath))
