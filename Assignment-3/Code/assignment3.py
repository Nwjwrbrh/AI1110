import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
table=pd.read_excel (r'Table.xlsx')
print(table)
plt.bar(x = table['SECTION'],
height=table['Number of girls per thousand boys'],color='lightgreen')
plt.ylabel('Number of girls per thousand boys')
plt.title('Section Vs Number of girls per thousand boys', size='14')
plt.grid()
plt.xticks(rotation=60)
plt.show()