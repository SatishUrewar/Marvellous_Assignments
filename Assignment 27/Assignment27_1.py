import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def AdvertiseRegression(datapath):
    df=pd.read_csv(datapath)

    print("Dataset Sample is : ")
    print(df.head)

    print("Clean the dataset")
    df.drop(columns= ['Unnamed: 0'],inplace=True)

    print("Updated data set is: ")
    print(df.head())

    print("Missing Values in Each Columns",df.isnull().sum())

    x=df[['TV','radio','newspaper']]
    y=df['sales']

    x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.5,random_state=42)

    model=LinearRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)


    print("\nPredicted vs Actual Sales:")
    result = pd.DataFrame({'Predicted': y_pred, 'Actual': y_test.values})
    print(result.head(10))  


def main():
    AdvertiseRegression("Advertising.csv")
    

if __name__=="__main__":
    main()

