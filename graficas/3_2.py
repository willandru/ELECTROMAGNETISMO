import matplotlib.pyplot as plt
import os.path


m=32.8/1000
w=m*9.81

i_b=[1,1.5,2,2.5,3]

m_i=[33.3, 33.6, 33.8, 34,34.3]
m_kg = [x / 1000 for x in m_i]
w_i= [x*9.81 for x in m_kg]

w_m=[x - w for x in w_i]
print('W_m 3_2 : ', w_m)

plt.plot(i_b,w_m,'--', color='black')
plt.plot(i_b,w_m,'*g')
plt.ylabel('W_i [N]')
plt.xlabel('i_b [A]')

plt.axes([1,5,0,0.5])
plt.figtext(.5,.9,'i_b VS W_m', fontsize=16, ha='center')
plt.figtext(.5,.85,'EXPERIMENTO 3 : L=25mm , i= 2A',fontsize=10,ha='center')


if os.path.isfile('3_2.png'):
    print ("File already exist.. cannot save new figure")
else:
    print ("Figure 3_2 saved...")
    plt.savefig('3_2.png')

plt.show()