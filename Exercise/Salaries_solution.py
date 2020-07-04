import pandas as pd

# read salaries data as a data frame called sal
sal = pd.read_csv("C:/Users/adarsh/Desktop/Atom/Pandas/Exercise/Salaries.csv")

# check the head of the data frame which displays 10 rows
sal.head(10)

# Use the .info() method to find out how many entries there are
sal.info() # 148654 Entries

# what's the avg base pay?
sal['BasePay'].mean() #66325.4488404877

# what is the highest amount of OvertimePay in the dataset ?
sal['OvertimePay'].max() #245131.88

# what is the job title of JOSEPH DRISCOLL ? (there is also a lowercase Joseph Driscoll)
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'] # CAPTAIN, FIRE SUPPRESSION

# How much does JOSEPH DRISCOLL make (including benefits)?
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'] #270324.91

# What is the name of highest paid person (including benefits)?
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName'] #NATHANIEL FORD
sal.loc[sal['TotalPayBenefits'].idxmax()]

# What is the name of lowest paid person (including benefits)? (observe the results)
sal.loc[sal['TotalPayBenefits'].idxmin()]

# What was the average (mean) BasePay of all employees per year? (2011-2014) ?
sal.groupby(by='Year').mean()['BasePay']

# How many unique job titles are there?
sal['JobTitle'].nunique(())

# What are the top 5 most common jobs?
sal['JobTitle'].value_counts().head()

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)
