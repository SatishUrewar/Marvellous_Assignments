import pandas as pd
import matplotlib.pyplot as plt

def main():
      data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
      df=pd.DataFrame(data)

      df['Total']=df['Math']+df['Science']+df['English']
      print("Total marks is :",df)

      plt.figure(figsize=(8,6))
      plt.bar(df['Name'],df['Total'],color='skyblue')
      plt.xlabel('Names of student')
      plt.ylabel('Total marks of student')
      plt.title("Student names vs total")
      plt.show()

      

      
if __name__=="__main__":
    main()