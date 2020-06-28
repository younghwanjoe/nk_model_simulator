import pylab
import numpy as np
import random
import time
import itertools
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D


Record_total_val_C=[]

N=int(input("Input N (recommended not more than 6): "))

period=100
Simul_Val_C=[0 for i in range(period)]
Simul_Val_DC=[0 for i in range(period)]
Simul_Val_RI=[0 for i in range(period)]
print ('''
       Interaction matrix: 1 - random or 2 - block_diagonal or 3 - custom
      ''')
which_matrix = int(input("Choose interaction matrix (1 or 2 or 3, Recommended 1): "))
K = int(input("Input K (integer from 0 to N-1): "))
while K >= N:
    K = int(input("Input K (integer from 0 to N-1): "))

D=int(input("Input Number of Division(divisor of N): "))
while N%D != 0:
    D=int(input("Input Number of Division(divisor of N): "))
simulsize=int(input("Input Number of simulation: "))
for simulation in range(simulsize):

    print(simulation)
    if which_matrix==1:

        def matrix_rand(N, K):

            Int_matrix_rand = np.zeros((N, N))
            for aa1 in np.arange(N):
                Indexes_1 =list(range(N))

                Indexes_1.remove(aa1)
                np.random.shuffle(Indexes_1)
                Indexes_1.append(aa1)

                Chosen_ones = Indexes_1[-(K+1):]  # this takes the last K+1 indexes
                for aa2 in Chosen_ones:
                    Int_matrix_rand[aa1, aa2] = 1
            return(Int_matrix_rand)
        Matrix=matrix_rand(N,K)

    elif which_matrix == 2:
        K=2

        Int_matrix = np.array([[1,1,1,0,0,0], \
                               [1,1,1,0,0,0], \
                               [1,1,1,0,0,0], \
                               [0,0,0,1,1,1], \
                               [0,0,0,1,1,1], \
                               [0,0,0,1,1,1]])
        Matrix=Int_matrix
    elif which_matrix == 3:

        K=3

        Int_matrix = np.array([[1,1,1,1,0,0,0,0], \
                               [1,1,1,1,0,0,0,0], \
                               [1,1,1,1,0,0,0,0], \
                               [1,1,1,1,0,0,0,0], \
                               [0,0,0,0,1,1,1,1], \
                               [0,0,0,0,1,1,1,1], \
                               [0,0,0,0,1,1,1,1], \
                               [0,0,0,0,1,1,1,1]])
        """
        Int_matrix = np.array([[1,1,0,0,0,0,0,0], \
                               [1,1,0,0,0,0,0,0], \
                               [0,0,1,1,0,0,0,0], \
                               [0,0,1,1,0,0,0,0], \
                               [0,0,0,0,1,1,0,0], \
                               [0,0,0,0,1,1,0,0], \
                               [0,0,0,0,0,0,1,1], \
                               [0,0,0,0,0,0,1,1]])
        
        Int_matrix = np.array([
            [1,1,1,1,1,1,0,0,0,0,0,0], \
            [1,1,1,1,1,1,0,0,0,0,0,0], \
            [1,1,1,1,1,1,0,0,0,0,0,0], \
            [1,1,1,1,1,1,0,0,0,0,0,0], \
            [1,1,1,1,1,1,0,0,0,0,0,0], \
            [1,1,1,1,1,1,0,0,0,0,0,0], \
            [0,0,0,0,0,0,1,1,1,1,1,1], \
            [0,0,0,0,0,0,1,1,1,1,1,1], \
            [0,0,0,0,0,0,1,1,1,1,1,1], \
            [0,0,0,0,0,0,1,1,1,1,1,1], \
            [0,0,0,0,0,0,1,1,1,1,1,1], \
            [0,0,0,0,0,0,1,1,1,1,1,1]])
        """
        """
        Int_matrix = np.array([[1,1,1,1,0,0,0,0], \
                               [1,1,1,1,0,0,0,0], \
                               [1,1,1,1,0,0,0,0], \
                               [1,1,1,1,0,0,0,0], \
                               [0,0,0,0,1,1,1,1], \
                               [0,0,0,0,1,1,1,1], \
                               [0,0,0,0,1,1,1,1], \
                               [0,0,0,0,1,1,1,1]])
        
        Int_matrix = np.array([[1,1,0,0,0,0,0,0], \
                               [1,1,0,0,0,0,0,0], \
                               [0,0,1,1,0,0,0,0], \
                               [0,0,1,1,0,0,0,0], \
                               [0,0,0,0,1,1,0,0], \
                               [0,0,0,0,1,1,0,0], \
                               [0,0,0,0,0,0,1,1], \
                               [0,0,0,0,0,0,1,1]])
        
        Int_matrix = np.array([
                               [1,1,1,1,1,1,0,0,0,0,0,0],\
                               [1,1,1,1,1,1,0,0,0,0,0,0],\
                               [1,1,1,1,1,1,0,0,0,0,0,0],\
                               [1,1,1,1,1,1,0,0,0,0,0,0],\
                               [1,1,1,1,1,1,0,0,0,0,0,0],\
                               [1,1,1,1,1,1,0,0,0,0,0,0],\
                               [0,0,0,0,0,0,1,1,1,1,1,1],\
                               [0,0,0,0,0,0,1,1,1,1,1,1],\
                               [0,0,0,0,0,0,1,1,1,1,1,1],\
                               [0,0,0,0,0,0,1,1,1,1,1,1],\
                               [0,0,0,0,0,0,1,1,1,1,1,1],\
                               [0,0,0,0,0,0,1,1,1,1,1,1]])
        Int_matrix = np.array([
                                [1,1,0,0,0,0,0,0,0,0,0,0], \
                                [1,1,0,0,0,0,0,0,0,0,0,0], \
                                [0,0,1,1,0,0,0,0,0,0,0,0], \
                                [0,0,1,1,0,0,0,0,0,0,0,0], \
                                [0,0,0,0,1,1,0,0,0,0,0,0], \
                                [0,0,0,0,1,1,0,0,0,0,0,0], \
                                [0,0,0,0,0,0,1,1,0,0,0,0], \
                                [0,0,0,0,0,0,1,1,0,0,0,0], \
                                [0,0,0,0,0,0,0,0,1,1,0,0], \
                                [0,0,0,0,0,0,0,0,1,1,0,0], \
                                [0,0,0,0,0,0,0,0,0,0,1,1], \
                                [0,0,0,0,0,0,0,0,0,0,1,1]])
        """
        Matrix=Int_matrix
    #print(Matrix)
    NK_land_origin = np.random.rand(2**N, N)
    NK_land=NK_land_origin
    #print(NK_land_origin)


    Local_list=[]
    for i in range(2**N):
        tmp=[]
        k=i
        for j in range (N):
            tmp.append(i%2)
            i//= 2

        #print(k,'th is',tmp)
        Local_list.append(tmp)

    Inter_list=[]
    for i in range(2**(K+1)):
        tmp=[]
        k=i
        for j in range (K+1):
            tmp.append(i%2)
            i//= 2

            #print(k,'th is',tmp)
        Inter_list.append(tmp)
    #print(Inter_list)

    Matrix_inter=[]
    for i in range(N):
        tmp_one=[]
        for j in range(N):
            if Matrix[i][j]==1:
                tmp_one.append(j)
        Matrix_inter.append(tmp_one)
    #print(Matrix_inter)


    Interaction_index_list=[]


    for index_Matrix_inter in range(N):
        tmp2=[]


        for index_Inter_list in range(2**(K+1)):
            tmp=[]
            for index_Local_list in range(2**N):
                pick=0


                for index_list in range(K+1):

                    if Local_list[index_Local_list][Matrix_inter[index_Matrix_inter][index_list]]==Inter_list[index_Inter_list][index_list]:
                        pick=pick+1
                if pick==K+1:
                    tmp.append(index_Local_list)
            tmp2.append(tmp)

        #print(tmp2)
        Interaction_index_list.append(tmp2)

    for index_ai in range(N):


        for index_Inter_list in range(2**(K+1)):

            for index_samevalue in range(2**(N-K-1)):
                NK_land[Interaction_index_list[index_ai][index_Inter_list][index_samevalue]][index_ai]=NK_land_origin[Interaction_index_list[index_ai][index_Inter_list][0]][index_ai]

                #print(NK_land)

    ########################################################################################################################
    #^^    Making Land
    #||    &Giving landom value
    ########################################################################################################################
    NK_val_C=[]
    for i in range(2**N):
        NK_val_C.append(float(sum(NK_land[i])/N))

        #print(i,'th is',NK_val_C[i])

    Global_peak=max(NK_val_C)



    Neighbor_list=[]

    for i in range(2**N):

        tmp=[]
        tmp2=[]
        for j in range(2**N):
            pick=0
            for k in range(N):

                if Local_list[j][k] != Local_list[i][k]:

                    pick =pick +1

            if pick == 1:
                tmp.append(j)
                tmp2.append(j+1)
        Neighbor_list.append(tmp)
        #print(i,'th\'s neigbor are',tmp2)

    current_position=random.randrange(0,2**N-1)
    current_position_DC=current_position
    #print('Global Peak',max(NK_val_C))
    #print('start point is',current_position,'and it\'s Neighbor are',Neighbor_list[current_position],'th and it\'s value is',NK_val_C[current_position])



    def WhereToMove_C(current_position):
        p=random.choice(Neighbor_list[current_position])
        if NK_val_C[current_position] < NK_val_C[p]:
            return p
        else:
            return current_position
    ########################################################################################################################
    #^^    Centralized Moving
    #||
    ########################################################################################################################
    Local_list_DC=[]

    for i in range(len(Local_list)):
        tmp=[]
        for k in range(0,N,N//D):
            tmp.append(Local_list[i][k:k+N//D])
        Local_list_DC.append(tmp)
        #print(i,'th is',Local_list_DC[i])



    for i in range(2**N):
        for k in range(0,N,N//D):
            tmp.append(Local_list[i][k:k+N//D])

    Local_list_DC_TotalDivision=[[] for i in range(D)]


    for i in range(D):
        for k in range(2**N):
            Local_list_DC_TotalDivision[i].append(Local_list_DC[k][i])
            #print('i is',i,Local_list_DC_TotalDivision[i][k])



    NK_val_C_DC=[[] for i in range(D)]
    for i in range(2**N):
        j=0
        for k in range(0,N,N//D):
            NK_val_C_DC[j].append(float(sum(NK_land[i][k:k+N//D])/(N/D)))
            j+=1

    def Find_neighbor_DC(Division_number,current_position):

        tmp=[]

        start=Division_number*(N//D)


        for i in range(int(N/D)):
            A=Local_list[current_position][:]
            if  A[start+i]==0:
                A[start+i]=1
                tmp.append(Local_list.index(A))
            else:
                A[start+i]=0
                tmp.append(Local_list.index(A))


        return tmp
    Neighbor_list_DC=[[] for i in range(D)]

    for i in range(2**N):
        for j in range(D):
            Neighbor_list_DC[j].append(Find_neighbor_DC(j,i))

            #print(i,'th',Neighbor_list_DC[1][i])



    def WhereToMove_DC(Division_number,current_position_DC):
        p=random.choice(Neighbor_list_DC[Division_number][current_position_DC])
        if NK_val_C_DC[Division_number][p]>NK_val_C_DC[Division_number][current_position_DC]:
            return p
        else:
            return current_position_DC

    def Find_next_index(current_position_DC):
        tmp=[]
        for i in range(D):
            tmp.append(WhereToMove_DC(i,current_position_DC))
        #print(tmp)
        for i in range(2**N):
            pick=0
            for j in range(D):

                if Local_list_DC[tmp[j]][j]== Local_list_DC[i][j]:
                    pick+=1
            if pick==D:
                return i
    ########################################################################################################################
    #^^    Decentralized Moving
    #||
    ########################################################################################################################

    Record_index_C=[current_position]
    Record_val_C=[]
    Record_index_DC=[current_position]
    Record_val_DC=[]

    Record_index_RI=[current_position]
    Record_val_RI=[]

    Record_total_val_C=[]
    Record_total_val_DC=[]
    Record_total_val_RI=[]
    for i in range(period):

        a=WhereToMove_C(Record_index_C[i])
        Record_index_C.append(a)
        Record_val_C.append(NK_val_C[Record_index_C[i]])
        #print(i,'th',a,NK_val_C[Record_index_C[i]])

    #print(Record_index_C)
    #print('Centralized way is',Record_val_C)
    #print('Centralized way is',Record_val_C[0],Record_val_C[9],Record_val_C[99],'global peak is ',Global_peak)

    for i in range(period):
        a=Find_next_index(current_position_DC)
        Record_index_DC.append(a)
        Record_val_DC.append(NK_val_C[Record_index_DC[i]])
        #print(i,'th',a,NK_val_C[Record_index_DC[i]])
    #print(Record_index_DC)
    #print('Decentralized way is',Record_val_DC)
    #print('Decentralized way is',Record_val_DC[0],Record_val_DC[9],Record_val_DC[99],'global peak is ',Global_peak)


    for i in range(period):
        if i <25:
            Record_index_RI.append(Find_next_index(current_position_DC))
            Record_val_RI.append(NK_val_C[Record_index_DC[i]])


        if i >=25:
            Record_index_RI.append(WhereToMove_C(Record_index_RI[i]))
            Record_val_RI.append(NK_val_C[Record_index_RI[i]])



    #print(Record_index_RI)
    #print('Reintergrater way is',Record_val_RI)
    #print('Reintergrater way is',Record_val_RI[0],Record_val_RI[9],Record_val_RI[99],'global peak 1
    # is ',Global_peak)

    Percent_val_C=[]
    Percent_val_DC=[]
    Percent_val_RI=[]


    for i in range(period):
        Percent_val_C.append(float(Record_val_C[i]/Global_peak))
        Percent_val_DC.append(float(Record_val_DC[i]/Global_peak))
        Percent_val_RI.append(float(Record_val_RI[i]/Global_peak))


    for i in range(period):
        Simul_Val_C[i]=Simul_Val_C[i]+float(Percent_val_C[i]/simulsize)
        Simul_Val_DC[i]=Simul_Val_DC[i]+float(Percent_val_DC[i]/simulsize)
        Simul_Val_RI[i]=Simul_Val_RI[i]+float(Percent_val_RI[i]/simulsize)

print(Simul_Val_C)
print(Simul_Val_DC)
print(Simul_Val_RI)
listx=np.arange(period)


if which_matrix==1:
    pylab.figure(1)
    pylab.title('Performance on Nondecomposable Landscapes')
    pylab.xlabel('Period')
    pylab.ylabel('Performance')
    line1,= pylab.plot(listx,Simul_Val_C,label='Centralized')
    line2,= pylab.plot(listx,Simul_Val_DC,marker='x',label='Decentralized')
    line3,= pylab.plot(listx,Simul_Val_RI,label='Reintegrator')
    plt.legend()
    plt.show()
elif which_matrix==2:
    pylab.figure(1)
    pylab.title('Performance on Decomposable Landscapes')
    pylab.xlabel('Period')
    pylab.ylabel('Performance')
    line1,= pylab.plot(listx,Simul_Val_C,label='Centralized')
    line2,= pylab.plot(listx,Simul_Val_DC,marker='x',label='Decentralized')
    line3,= pylab.plot(listx,Simul_Val_RI,label='Reintegrator')
    plt.legend()
    plt.show()
elif which_matrix==3:
    pylab.figure(1)
    pylab.title('Performance on Decomposable Landscapes')
    pylab.xlabel('Period')
    pylab.ylabel('Performance')
    line1,= pylab.plot(listx,Simul_Val_C,label='Centralized')
    line2,= pylab.plot(listx,Simul_Val_DC,marker='x',label='Decentralized')
    line3,= pylab.plot(listx,Simul_Val_RI,label='Reintegrator')
    plt.legend()
    plt.show()



