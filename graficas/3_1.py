import matplotlib.pyplot as plt
import os.path


m=32.8/1000
w=m*9.81

i=[1, 2,3,4,5]

m_i=[0.0334, 0.0338, 0.0343, 0.0348, 0.0352]
w_i=[x *9.81 for x in m_i]

w_m=[x - w for x in w_i]
print('W_m 3_1 : ', w_m)

plt.plot(i,w_m,'--', color='black')
plt.plot(i,w_m,'*g')
plt.ylabel('W_m [N]')
plt.xlabel('i [A]')

plt.axes([1,5,0,0.5])
plt.figtext(.5,.9,'i VS W_m', fontsize=16, ha='center')
plt.figtext(.5,.85,'EXPERIMENTO 3 : L=25mm , i_B= 2A',fontsize=10,ha='center')



if os.path.isfile('3_1.png'):
    print ("File already exist.. cannot save new figure")
else:
    print ("Figure 3_1 saved...")
    plt.savefig('3_1.png')

plt.show()