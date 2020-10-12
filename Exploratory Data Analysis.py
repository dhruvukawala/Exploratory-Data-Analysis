import pandas as pd

airline=pd.read_excel('Airline.xlsx')

airline_data=airline.copy()

airline_data.insert(4,'safety',"")

for i in range(0,len(airline_data['incidents_85_99']),1):
    if(airline_data['incidents_85_99'][i]==0):
        airline_data['safety'][i]="Safe"
    elif(airline_data['incidents_85_99'][i]<=5):
        airline_data['safety'][i]="Risky"
    else: airline_data['safety'][i]="Danger"



#Frequency tables
    
#two-way tables

print(pd.crosstab(index=airline_data['airline'],columns=airline_data['safety']))

print(pd.crosstab(index=airline_data['safety'],columns='count'))

#probability

print(pd.crosstab(index=airline_data['airline'],columns=airline_data['safety'],normalize=True))


#marginal probability

print(pd.crosstab(index=airline_data['airline'],columns=airline_data['safety'],margins=True,normalize='index'))


#correlation



