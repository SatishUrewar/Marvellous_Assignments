import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score,precision_score,recall_score,f1_score




def LogisticR(X,Y):
    scaler=StandardScaler()
    xscaled=scaler.fit_transform(X)
    x_train, x_test,y_train,y_test=train_test_split(xscaled,Y,test_size=0.2,random_state=42)
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    
    accuracy=accuracy_score(y_test,y_pred)
    cnfm=confusion_matrix(y_test,y_pred)
    precision=precision_score(y_test,y_pred)
    recallscore=recall_score(y_test,y_pred)
    f1score=f1_score(y_test,y_pred)

    print("Accuracy : ",accuracy*100)
    print("Confusion Matrix : ",cnfm)
    print("F1 score : ",f1score*100)
    print("Precison Score  :",precision*100)
    print("Recall Score : ",recallscore*100)


    plt.figure(figsize=(6,4))
    sns.heatmap(cnfm,annot=True,fmt='d',cmap='Blues')
    plt.title("Confusion Matrix Logistic Regression")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    return model, scaler 



def DecisionTree(X,Y):
    scaler=StandardScaler()
    xscaled=scaler.fit_transform(X)
    x_train, x_test,y_train,y_test=train_test_split(xscaled,Y,test_size=0.2,random_state=42)
    model2=DecisionTreeClassifier()
    model2.fit(x_train,y_train)
    y_pred=model2.predict(x_test)
    
    accuracy=accuracy_score(y_test,y_pred)
    cnfm=confusion_matrix(y_test,y_pred)
    precision=precision_score(y_test,y_pred)
    recallscore=recall_score(y_test,y_pred)
    f1score=f1_score(y_test,y_pred)
    
    print("Decision Tree Metrics ")
    print("Accuracy : ",accuracy*100)
    print("Confusion Matrix : ",cnfm)
    print("F1 score : ",f1score*100)
    print("Precison Score  :",precision*100)
    print("Recall Score : ",recallscore*100)


    plt.figure(figsize=(6,4))
    sns.heatmap(cnfm,annot=True,fmt='d',cmap='Blues')
    plt.title("Confusion Matrix Decision Tree")
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    return model2, scaler 

   
       

def predict_save(model,model2,scaler):
    
    test_df = pd.read_csv("diabetes_test.csv")

    columns_to_fix = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    test_df[columns_to_fix] = test_df[columns_to_fix].replace(0, np.nan)

    test_df.fillna(test_df.median(), inplace=True)

    x_test_scaled = scaler.transform(test_df)

    predictions = model.predict(x_test_scaled)
    predictions2=model2.predict(x_test_scaled)

    test_df['Predicted_Outcome_Logistic'] = predictions
    test_df['Predicted_Outcome_Decisiontree']=predictions2

    test_df['Predicted_Outcome_Logistic'] = predictions
    test_df['Predicted_Outcome_Decisiontree'] = predictions2

    print("\n*********Predicted Diabetes Results********")
    print(test_df[['Predicted_Outcome_Logistic', 'Predicted_Outcome_Decisiontree']])

    test_df.to_csv("diabetes_predictions.csv", index=False)
    print("Predictions saved to 'diabetes_predictions.csv'")


    
def main():

    df=pd.read_csv("diabetes.csv")

    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df.describe())


    plt.figure(figsize=(6,4))
    sns.countplot(x='Outcome',data=df)
    plt.title("Distribution of target variable")
    plt.xlabel("Outcome")
    plt.ylabel("COUNT")
    plt.show


    df.hist(figsize=(12,10),bins=20,color='skyblue',edgecolor='black')
    plt.tight_layout()
    plt.show()


    columnzero=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    df[columnzero]=df[columnzero].replace(0,np.nan)
    df.fillna(df.median(),inplace=True)
    

    x=df.drop(columns=['Outcome'])
    y=df['Outcome']

    model, scaler = LogisticR(x, y)
    model2, _ = DecisionTree(x, y)

    predict_save(model, model2, scaler)
if __name__=="__main__":
    main()