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

  

      amit_marks=df[df['Name']=='Amit'][['Math','Science','English']].iloc[0]
      subjects=amit_marks.index
      marks=amit_marks.values
      
      plt.figure(figsize=(8,6))
      plt.plot(subjects,marks, marker='o',linestyle='-',color='green')
      plt.xlabel('Subject')
      plt.ylabel('Marks')
      plt.title("Amit Marks across all subject")
      plt.show()

      

      
if __name__=="__main__":
    main()