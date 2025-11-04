import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Container_Hierarchy(2).csv")

userip = input("Type package ID to get Dwell time of the package: ")

package_data = df[df['Container Id'] == userip]

if not package_data.empty:
    
    print(package_data['Dwell Time'].values[0])
    dwell_time = package_data['Dwell Time'].values[0]
    print('package is being dwelling from past {dwell_time}')
else: print('Package not found')