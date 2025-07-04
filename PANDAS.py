import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice','Bob','Charlie','Ansari','Billi'],
    'Age': [25,30,35,18,90],
    'City': ['New york','Paris','London','Achalpur','Paratwada'],
    'College': ['JDID','IIT DELHI','LONDON UNIVERSITY','GPA','GPA']
}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Access a column
print(df['Name'])

# Basic statics
print(df['Age'].mean()) # Average age

# Filter rows 
print(df[df['Age'] >= 18])