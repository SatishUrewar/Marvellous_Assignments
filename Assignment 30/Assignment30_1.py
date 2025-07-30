import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score,classification_report,roc_curve

def main():
    df=pd.read_csv("bank-full.csv",sep=';')
    print(df)

    print(df.head())
    print(df.info())

    print(df.describe())
    print(df.isin(['unknown']).sum())
    print(df['y'].value_counts())


    plt.figure(figsize=(6,4))
    sns.countplot(x='y', data=df)
    plt.title("class distribution (y)")
    plt.xlabel("Subscribed to term Deposit")
    plt.ylabel('count')
    plt.show()


    for col in df.select_dtypes(include=['object']).columns:
        if df[col].isin(['unknown']).any():
            mode=df[col].mode()[0]
            df[col]=df[col].replace('unknown',mode)
            print(f"Repalced 'unknown' in '{col}' with mode'{mode}'")

    
    le=LabelEncoder()

    categorical_column=df.select_dtypes(include=['object']).columns

    for col in categorical_column:
        df[col]=le.fit_transform(df[col])

    print(df)

    x=df.drop('y', axis=1)
    y=df['y']

    scaler=StandardScaler()
    xscaled=scaler.fit_transform(x)

    x_train,x_test,y_train,y_test=train_test_split(xscaled,y,test_size=0.2,random_state=42)
     

    logistic = LogisticRegression()
    rf = RandomForestClassifier()
    knn = KNeighborsClassifier()

    models = {
        "Logistic Regression": logistic,
        "Random Forest": rf,
        "K-Nearest Neighbors": knn
    }

    model_preds = {}
    model_probs = {}

    
    for name, model in models.items():
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        y_prob = model.predict_proba(x_test)[:, 1]

        model_preds[name] = y_pred
        model_probs[name] = y_prob

        print(f"\n***** {name} *****")
        print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        print("ROC AUC Score:", roc_auc_score(y_test, y_prob) * 100)
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

    
    for name in model_preds:
        cm = confusion_matrix(y_test, model_preds[name])
        cmap = 'Blues' if name == "Logistic Regression" else ('Greens' if name == "K-Nearest Neighbors" else 'Oranges')

        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap=cmap)
        plt.title(f"{name} - Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.tight_layout()
        plt.show()


    plt.figure(figsize=(8, 6))
    for name in model_probs:
        fpr, tpr, _ = roc_curve(y_test, model_probs[name])
        auc = roc_auc_score(y_test, model_probs[name])
        plt.plot(fpr, tpr, label=f"{name} (AUC = {auc:.2f})")

    plt.plot([0, 1], [0, 1], 'k--')  
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curves for All Models")
    plt.legend()
    plt.tight_layout()
    plt.show()

  
    
     
if __name__=="__main__":
    main()