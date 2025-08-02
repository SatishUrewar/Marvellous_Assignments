import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def main():

    df_true=pd.read_csv("True.csv")
    df_fake=pd.read_csv("Fake.csv")
    
    df_fake['label']=0
    df_true['label']=1

    df=pd.concat([df_fake,df_true] ,ignore_index=True)
  
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)


    df=df[['text','label']]
    df.dropna(subset='text',inplace=True)

    print("first 5 rows of dataset",df.head())

    x=df['text']
    y=df['label']

    x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    vectorizer=TfidfVectorizer(stop_words='english',max_df=0.7)

    x_train_tfidf=vectorizer.fit_transform(x_train)

    x_test_tfidf=vectorizer.transform(x_test)

    log_clf = LogisticRegression(random_state=42)
    dt_clf = DecisionTreeClassifier(random_state=42)

    hard_voting_clf = VotingClassifier(
        estimators=[('lr', log_clf), ('dt', dt_clf)], voting='hard'
    )

    soft_voting_clf = VotingClassifier(
        estimators=[('lr', log_clf), ('dt', dt_clf)], voting='soft'
    )

   
    log_clf.fit(x_train_tfidf, y_train)
    dt_clf.fit(x_train_tfidf, y_train)
    hard_voting_clf.fit(x_train_tfidf, y_train)
    soft_voting_clf.fit(x_train_tfidf, y_train)

    y_pred_lr = log_clf.predict(x_test_tfidf)
    y_pred_dt = dt_clf.predict(x_test_tfidf)
    y_pred_hard = hard_voting_clf.predict(x_test_tfidf)
    y_pred_soft = soft_voting_clf.predict(x_test_tfidf)

    print("Logistic Regression:", accuracy_score(y_test, y_pred_lr) * 100)
    print("Decision Tree:", accuracy_score(y_test, y_pred_dt) * 100)
    print("Hard Voting Classifier:", accuracy_score(y_test, y_pred_hard) * 100)
    print("Soft Voting Classifier:", accuracy_score(y_test, y_pred_soft) * 100)
    

    cm = confusion_matrix(y_test, y_pred_soft)

    plt.figure(figsize=(7, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix for Soft Voting Classifier')
    plt.show()


        
        

if __name__=="__main__":
    main()