import matplotlib.pyplot as plt
import os.path



w_m=[0.004905, 0.00981, 0.017658]
L=[ 0.0125, 0.025, 0.05,]





plt.plot(L,w_m,'--', color='black')
plt.plot(L,w_m,'*y')
plt.ylabel('W_m [N]')
plt.xlabel('L [m]')

plt.axes([1,5,0,0.5])
plt.figtext(.5,.9,'W_m vs L', fontsize=16, ha='center')
plt.figtext(.5,.85,'i=2 [A] y i_b=2 [A]',fontsize=10,ha='center')


if os.path.isfile('ff.png'):
    print ("File already exist.. cannot save new figure")
else:
    print ("Figure ff saved...")
    plt.savefig('ff.png')
plt.show()
