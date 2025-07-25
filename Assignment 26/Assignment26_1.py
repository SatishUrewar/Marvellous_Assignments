import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def playpredictor(datapath):
    
    df=pd.read_csv(datapath)
    print(df)
    print("Data Loaded Successfully")

    df.drop(columns=['Unnamed: 0'],inplace=True)
    print(df)
    print("removing unamed column")

    LE=LabelEncoder()
    df['Whether']=LE.fit_transform(df["Whether"])
    df['Temperature']=LE.fit_transform(df['Temperature'])
    df['Play']=LE.fit_transform(df['Play'])
    print("Data encoded Successfully")

    print(df)

    x=df[['Whether','Temperature']]
    y=df['Play']

    print("Model Training")
    x_train, x_test,y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    model=KNeighborsClassifier(n_neighbors=3)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    
    print("Model Testing")
    accuracy=accuracy_score(y_test,y_pred)

    print("Accuracy of play predictor :",accuracy*100)

    CheckAccuracy(x,y)

def CheckAccuracy(X,Y):
    x_train, x_test,y_train, y_test=train_test_split(X,Y,test_size=0.5,random_state=42)
    accuracy_scores=[]
    k_range=range(1,10)
    for k in k_range:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accurcy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accurcy)
        print("Value of k is :", k)
        print("Accuracy is :", accurcy*100)
        print()

    best_k=k_range[accuracy_scores.index(max(accuracy_scores))]
    accuracy_scores.append(accurcy)

    print("Best value of k is : ",best_k)


def main():
    playpredictor("PlayPredictor.csv")


if __name__=="__main__":
    main()