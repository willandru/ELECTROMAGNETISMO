import matplotlib.pyplot as plt
import os.path


m=36.7/1000
w=m*9.81
i=[1,2,3,4,5]
w_i=[0.369,0.377,0.386,0.392,0.404]

w_m=[x - w for x in w_i]
print('W_m 1_1 : ', w_m)


plt.plot(i,w_m,'--', color='black')
plt.plot(i,w_m,'*r')
plt.ylabel('W_m [N]')
plt.xlabel('i [A]')

plt.axes([1,5,0,0.5])
plt.figtext(.5,.9,'i VS W_m', fontsize=16, ha='center')
plt.figtext(.5,.85,'EXPERIMENTO 1 : L=50mm , i_B= 2A',fontsize=10,ha='center')


if os.path.isfile('1_1.png'):
    print ("File already exist.. cannot save new figure")
else:
    print ("Figure 1_1 saved...")
    plt.savefig('1_1.png')


plt.show()