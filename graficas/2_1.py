import matplotlib.pyplot as plt
import os.path




m=32.8/1000
w=m*9.81
print('w: ',w)

i=[1,2,3,4,5]
w_i=[0.324, 0.326,0.328,0.331, 0.333]

w_m=[x - w for x in w_i]
print('W_m 2_1 : ', w_m)




plt.plot(i,w_m,'--', color='black')
plt.plot(i,w_m,'*b')
plt.ylabel('W_m [N]')
plt.xlabel('i [A]')

plt.axes([1,5,0,0.5])
plt.figtext(.5,.9,'i VS W_m', fontsize=16, ha='center')
plt.figtext(.5,.85,'EXPERIMENTO 2 : L=12.5mm , i_B= 2A',fontsize=10,ha='center')





if os.path.isfile('2_1.png'):
    print ("File already exist.. cannot save new figure")
else:
    print ("Figure 2_1 saved...")
    plt.savefig('2_1.png')


#plt.show()