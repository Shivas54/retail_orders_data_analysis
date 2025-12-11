


#read data from the file and handle null values
import pandas as pd
df = pd.read_csv('retail_orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()




#rename columns names ..make them lower case and replace space with underscore
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)





#derive new columns discount , sale price and profit
df['discount']=df['list_price']*df['discount_percent']/100

df['sale_price']= df['list_price']-df['discount']

df['profit']=df['sale_price']-df['cost_price']

df


df.dtypes

#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")





#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)




