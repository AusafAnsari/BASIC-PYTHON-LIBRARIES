import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataframe
df  = pd.DataFrame({'Branch': ['EXTC', 'ME','ME','EXTC', 'CS', 'CS','CE','CE'],
                    'Score': [80,90,78,101,99,34,40,33]})

# Plot a boxplot
sns.boxplot(x='Branch',y='Score', data=df)
plt.show()
