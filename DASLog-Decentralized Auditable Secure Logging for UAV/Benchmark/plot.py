import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d

fig = plt.figure()
# set directory
df1 = pd.read_excel('tree_sheets_a.xlsx', 'df_1' )
df11 = pd.read_excel('tree_sheets_a1.xlsx', 'df_11' )

# set plot
xnew = np.linspace(df1['C'].min(), df1['C'].max(), 8)
f_cubic = interp1d(df1['C'], df1['A'], kind='cubic')
plt.plot(xnew, f_cubic(xnew), '--o', label='Merkle tree+hashchain+encryption', linewidth=3)
plt.scatter(xnew, f_cubic(xnew), s=100, marker='o')
xnew1 = np.linspace(df11['C'].min(), df11['C'].max(), 8)
f_cubic1 = interp1d(df11['C'], df11['A1'], kind='cubic')
plt.plot(xnew1, f_cubic1(xnew1), '--^',label='Merkle tree', linewidth=3)
plt.scatter(xnew1, f_cubic1(xnew1), s=100, marker='^')
plt.grid()
plt.xticks(np.arange(0,10001,1000))

# set label
plt.xlabel('Number of Log records', fontsize=18)
plt.ylabel('Proof generation time (s)', fontsize=18)

plt.legend(fontsize=12)
plt.show()
fig.savefig('pgt.pdf')
fig.savefig('pgt.png')
#'''
fig = plt.figure()
# set directory
df2 = pd.read_excel('tree_sheets_b.xlsx', 'df_2')
df5 = pd.read_excel('tree_sheets_bhc.xlsx', 'df_5')
xnew2 = np.linspace(df2['C'].min(), df2['C'].max(), 8)
f_cubic2 = interp1d(df2['C'], df2['B'], kind='cubic')
plt.plot(xnew2, f_cubic2(xnew2), '--^', label='Hashchain+Merkle tree', linewidth=3)
plt.scatter(xnew2, f_cubic2(xnew2), s=100)
xnew5 = np.linspace(df5['C'].min(), df5['C'].max(), 8)
f_cubic5 = interp1d(df5['C'], df5['Bhc'], kind='cubic')
plt.plot(xnew5, f_cubic5(xnew5), '--^', label='Hashchain', linewidth=3)
plt.scatter(xnew5, f_cubic5(xnew5), s=100, marker='^')
plt.grid()
plt.xticks(np.arange(0,10001,1000))

# set label
plt.xlabel('Number of Log records', fontsize=18)
plt.ylabel('verification time (s)', fontsize=18)
#plt.title('Logging system project')
plt.legend(fontsize=12)
plt.show()
fig.savefig('vt.pdf')
fig.savefig('vt.png')
#'''
fig = plt.figure()
# set directory
df3 = pd.read_excel('tree_sheets_tr.xlsx', 'df_3')
df4 = pd.read_excel('tree_sheets_js.xlsx', 'df_4')
xnew4 = np.linspace(df4['C'].min(), df4['C'].max(), 8)
f_cubic4 = interp1d(df4['C'], df4['js'], kind='cubic')
plt.plot(xnew4, f_cubic4(xnew4), '--o', label='Merkle tree JSON file', linewidth=3)
plt.scatter(xnew4, f_cubic4(xnew4), s=100)
plt.legend(prop={"size":16})
xnew3 = np.linspace(df3['C'].min(), df3['C'].max(), 8)
f_cubic3 = interp1d(df3['C'], df3['tr'], kind='cubic')
plt.plot(xnew3, f_cubic3(xnew3), '--^', label='Entire Merkle tree', linewidth=3)
plt.scatter(xnew3, f_cubic3(xnew3), s=100, marker='^')
plt.legend(prop={"size":16})
plt.grid()
plt.xticks(np.arange(0,10001,1000))

# set label
plt.xlabel('Number of Log records', fontsize=18)
plt.ylabel('Proof Size (KB)', fontsize=18)
#plt.title('Logging system project')
plt.legend(fontsize=12)
plt.show()
fig.savefig('ps.pdf')
fig.savefig('ps.png')
#'''

fig.savefig('multipleplots.png')


