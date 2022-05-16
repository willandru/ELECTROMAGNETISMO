import matplotlib.pyplot as plt
import os.path

m=36.7/1000
w=m*9.81
i_b=[1, 1.5, 2, 2.5, 3]
m_i=[0.0376, 0.0381, 0.0386, 0.039, 0.0395]

w_i=[x *9.81 for x in m_i]

w_m=[x - w for x in w_i]
print('W_m 1_2 : ', w_m)



plt.plot(i_b,w_m,'--', color='black')
plt.plot(i_b,w_m,'*r')
plt.ylabel('W_m [N]')
plt.xlabel('i_b [A]')

plt.axes([1,5,0,0.5])
plt.figtext(.5,.9,'i_b VS W_m', fontsize=16, ha='center')
plt.figtext(.5,.85,'EXPERIMENTO 1 : L=50mm , i= 2A',fontsize=10,ha='center')


if os.path.isfile('1_2.png'):
    print ("File already exist.. cannot save new figure")
else:
    print ("Figure 1_2 saved...")
    plt.savefig('1_2.png')

plt.show()