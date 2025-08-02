import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score,roc_curve

def main():
    dataset=load_breast_cancer()
    x=pd.DataFrame(dataset.data,columns=dataset.feature_names)
    y=pd.Series(dataset.target)

    print("Shape od data ",x.shape)
    print("First 5 rows of data",x.head())

    x_train, x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

    dt_model=DecisionTreeClassifier()
    dt_model.fit(x_train,y_train)

    rf_model=RandomForestClassifier()
    rf_model.fit(x_train,y_train)

    gb_model=GradientBoostingClassifier()
    gb_model.fit(x_train,y_train)
   
    y_pred_dt = dt_model.predict(x_test)
    y_pred_rf = rf_model.predict(x_test)
    y_pred_gb = gb_model.predict(x_test)

    y_prob_dt = dt_model.predict_proba(x_test)[:, 1]
    y_prob_rf = rf_model.predict_proba(x_test)[:, 1]
    y_prob_gb = gb_model.predict_proba(x_test)[:, 1]

    acc_dt = accuracy_score(y_test, y_pred_dt)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    acc_gb = accuracy_score(y_test, y_pred_gb)

    auc_dt = roc_auc_score(y_test, y_prob_dt)
    auc_rf = roc_auc_score(y_test, y_prob_rf)
    auc_gb = roc_auc_score(y_test, y_prob_gb)
    
    print("Decision Tree Accuracy and ROC-AUC : ",acc_dt*100,auc_dt*100)
    print("Gradient boosting Accuracy and ROC-AUC : ",acc_gb*100,auc_gb*100)
    print("Random Forest Accuracy and ROC-AUC : ",acc_rf*100,auc_rf*100)

    cm_dt = confusion_matrix(y_test, y_pred_dt)
    cm_rf = confusion_matrix(y_test, y_pred_rf)
    cm_gb = confusion_matrix(y_test, y_pred_gb)

    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Confusion Matrices (0: Malignant, 1: Benign)', fontsize=16)

    
    sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Blues', ax=axes[0])
    axes[0].set_title('Decision Tree')
    axes[0].set_xlabel('Predicted')
    axes[0].set_ylabel('Actual')

    
    sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Greens', ax=axes[1])
    axes[1].set_title('Random Forest')
    axes[1].set_xlabel('Predicted')
    axes[1].set_ylabel('Actual')

    
    sns.heatmap(cm_gb, annot=True, fmt='d', cmap='Oranges', ax=axes[2])
    axes[2].set_title('Gradient Boosting')
    axes[2].set_xlabel('Predicted')
    axes[2].set_ylabel('Actual')

    plt.show()


    fpr_dt, tpr_dt, _ = roc_curve(y_test, y_prob_dt)
    fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
    fpr_gb, tpr_gb, _ = roc_curve(y_test, y_prob_gb)

    plt.figure(figsize=(10, 7))
    plt.plot(fpr_dt, tpr_dt)
    plt.plot(fpr_rf, tpr_rf,  linewidth=2)
    plt.plot(fpr_gb, tpr_gb, linestyle='--')


    plt.plot([0, 1], [0, 1], 'k--', label='Chance (AUC = 0.50)')

    plt.title('ROC Curve')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.legend()
    plt.show()


    importance1 = pd.Series(dt_model.feature_importances_,index=x.columns)
    importance1 = importance1.sort_values(ascending=False)

    importance1.plot(kind='bar', figsize=(10,6), title="Feature Imporatnce of Decision Tree")
    plt.show()

    importance2 = pd.Series(rf_model.feature_importances_,index=x.columns)
    importance2 = importance2.sort_values(ascending=False)

    importance2.plot(kind='bar', figsize=(10,6), title="Feture Imporatnce of Random Forest")
    plt.show()

    importance3 = pd.Series(gb_model.feature_importances_,index=x.columns)
    importance3 = importance3.sort_values(ascending=False)

    importance3.plot(kind='bar', figsize=(10,6), title="Feture Imporatnce of Gradient Boosting")
    plt.show()




    
if __name__=="__main__":
    main()