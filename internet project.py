import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data_df = pd.read_csv(r'C:\Users\Reggie\Desktop\vs code test project\internet_usage_by_countries.csv')
print(data_df)
#identyfying the data
print(data_df.dtypes)
print(data_df.describe)
print(data_df.columns)
print(data_df.columns[data_df.isna().any()])
data_df.drop(data_df.columns[[1]],axis=1,inplace=True)
print(data_df)
# preparing the data
data_df = data_df[['Year', 'Country Name', 'Individuals using the Internet (% of population)']].copy()
data_df2 = data_df[data_df['Year'] > 1999][data_df['Year'] < 2021]
data_df2['Year'].astype(str)
# making year and country the indexes and filling with population
data_df2.set_index(['Year', 'Country Name'])
raw_df = data_df2.set_index(['Year', 'Country Name']).unstack()['Individuals using the Internet (% of population)']
print(raw_df.columns[raw_df.isna().any()])
print(raw_df)

# analysis
# total population in the year 2020
internet_users = raw_df['World'][2020]
print('the number of people using the internet is', int(internet_users))

# population growth
year2016 = raw_df['World'][2016]
growth = abs(internet_users - year2016)
if year2016 < internet_users:
    print('the growth in users of the internet has increased by', growth.round())
elif year2016 > internet_users:
    print('There has been a decrease in internet users in the past 5 years of about', growth.round())
else:
    print('None')

# Ghana population to Nigeria
ghana = raw_df['Ghana'].sum()
nigeria = raw_df['Nigeria'].sum()
if ghana > nigeria:
    print('for the past 20 years Ghana has had more internet users than Nigeria ',
          abs(ghana.round()), 'with a difference of about', abs(ghana-nigeria).round())
elif ghana < nigeria:
    print('for the past 20 years Nigeria has had more internet users than Ghana ',
          abs(nigeria.round()),'with a difference of about', abs(ghana-nigeria).round())
else:
    print('None')

# identifying a growing population
# prepare the dataset for this tabulation
raw_df.drop(raw_df.columns[[1,2,5,9,262]], axis=1, inplace=True)
del raw_df['Caribbean small states']
del raw_df['Central Europe and the Baltics']
del raw_df['Channel Islands']
del raw_df['Early-demographic dividend']
del raw_df['East Asia & Pacific']
del raw_df['East Asia & Pacific (IDA & IBRD countries)']
del raw_df['East Asia & Pacific (excluding high income)']
del raw_df['Europe & Central Asia']
del raw_df['Europe & Central Asia (IDA & IBRD countries)']
del raw_df['Europe & Central Asia (excluding high income)']
del raw_df['European Union']
del raw_df['Fragile and conflict affected situations']
del raw_df['Heavily indebted poor countries (HIPC)']
del raw_df['High income']
del raw_df['IBRD only']
del raw_df['IDA blend']
del raw_df['IDA only']
del raw_df['IDA total']
del raw_df['Late-demographic dividend']
del raw_df['West Bank and Gaza']
del raw_df['Upper middle income']
del raw_df['Sub-Saharan Africa (excluding high income)']
del raw_df['Sub-Saharan Africa (IDA & IBRD countries)']
del raw_df['Sub-Saharan Africa']
del raw_df['South Asia (IDA & IBRD)']
del raw_df['South Asia']
del raw_df['Small states']
del raw_df['Pre-demographic dividend']
del raw_df['Post-demographic dividend']
del raw_df['Pacific island small states']
del raw_df['Other small states']
del raw_df['Not classified']
del raw_df['North America']
del raw_df['Middle income']
del raw_df['Middle East & North Africa (excluding high income)']
del raw_df['Middle East & North Africa (IDA & IBRD countries)']
del raw_df['Middle East & North Africa']
del raw_df['Lower middle income']
del raw_df['Least developed countries: UN classification']
del raw_df['Latin America & the Caribbean (IDA & IBRD countries)']
del raw_df['Latin America & Caribbean (excluding high income)']
del raw_df['Latin America & Caribbean']
del raw_df['IDA & IBRD total']
del raw_df['Euro area']
del raw_df['OECD members']
del raw_df['Low & middle income']
del raw_df['Low income']
# which country had the highest internet users on the year 2020
country = raw_df[20:21]
print(country.to_markdown())
maxvalue = country.max(axis=1)
print(maxvalue)
print('the country with the highest number of internet users is '
      'the United Arab Emirates, with 100 users')

# graphs
# line chart between ghana & nigeria
sns.set_style('ticks')
plt.subplots(figsize= [10,6])
plt.plot(raw_df['Ghana'],raw_df['Nigeria'], 'xg')
plt.xlabel('Ghana')
plt.ylabel('Nigeria')
plt.title('Ghana users to Nigeria users', fontsize=15)
plt.show()
print('this line graph clearly shows ghana internet users match up to'
      ' that of nigeria.')

# heatmap showing countries user census
plt.title('No of internet users in a sample of countries', fontsize=15)
sns.heatmap(raw_df,annot= False, cmap='Blues')
plt.show()

# pie chart to show internet users in west africa
raw_df.reset_index(inplace=True)
five = raw_df[raw_df['Year']>2015]
data = five['Ghana']
labels=[2016,2017,2018,2019,2020]
plt.subplots(figsize= [10,6])
colors = sns.color_palette('pastel')
plt.pie(data, colors=colors, autopct="%.f%%",labels=labels,
        explode=[0.05]*5,pctdistance=0.5)
plt.title('Internet users in Ghana over the past five years', fontsize=15)
plt.show()


# horizontal bar chart to display internet usage between ghana and its neighbours
sns.set_style('dark')
plt.subplots(figsize= [12,6])
plt.barh(raw_df['Year'],raw_df['Ghana'], color= 'red',height=0.9)
plt.barh(raw_df['Year'],raw_df['Togo'], color='blue',height=0.7)
plt.barh(raw_df['Year'],raw_df['Burkina Faso'], color='green',height=0.4)
plt.barh(raw_df['Year'],raw_df["Cote d'Ivoire"], color= 'black',height=0.15)
plt.legend(['Ghana', 'Nigeria','Burkina Faso',"Cote d'Ivoire"])
plt.title('Ghana and Neighbouring countries')
plt.show()

# write tha data to a new excel file

raw_df.to_csv('internet users.csv')
