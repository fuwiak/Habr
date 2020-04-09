import requests
import pandas as pd
import matplotlib.pylab as plt


number_of_pages = 100
#number_of_ads = number_of_pages * per_page

#job_title = ['data scientist', 'Data Analyst']
job_title = ["'Deep learning' not 'Machine learning'"]
for job in job_title:
	data=[]
	for i in range(number_of_pages):
	    url = 'https://api.hh.ru/vacancies'
	    par = {'text': job, 'area':'113','per_page':'10', 'page':i}
	    r = requests.get(url, params=par)
	    e=r.json()
	    data.append(e)
	    vacancy_details = data[0]['items'][0].keys()
	    df = pd.DataFrame(columns= list(vacancy_details))
	    ind = 0
	    for i in range(len(data)):
	    	for j in range(len(data[i]['items'])):
	    		df.loc[ind] = data[i]['items'][j]
	    		ind+=1
	csv_name = job+".csv"
	
	df.to_csv(csv_name)


