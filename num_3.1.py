# coding:UTF-8
# User  :yqhe
# Date  :2022/2/9 11:59
import numpy as np
import matplotlib.pyplot as plt

'''
1.斯奈尔定律
2.zoeppritz方程求解
3.konnt方程求解
4.定义模型并求解
5.成图
'''

'''1.斯奈尔定律（Snell's Refraction Law）'''
#入射角Incidence_angle，反射角Reflection_angle
def Reflection_angle(Incidence_angle,V_1,V_2):
    p = np.sin(Incidence_angle)/V_1
    Reflection_angle = np.arcsin(p*V_2)
    return Reflection_angle

'''2.zoeppritz方程求解'''
#系数矩阵Coefficient_matrix1，振幅Amplitude1
#振幅Amplitude1 = [[R_pp],[R_ps],[T_ps],[T_pp]]的转置
def Amplitude1(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1):
    Coefficient_matrix1 = [[np.sin(alpha_1), np.cos(beta_1), -np.sin(alpha_2), np.cos(beta_2)],
                          [np.cos(alpha_1), -np.sin(beta_1), np.cos(alpha_2), np.sin(beta_2)],
                          [np.sin(2*alpha_1), (V_p1/V_s1)*np.cos(2*beta_1), (rho_2/rho_1)*(V_s2**2/V_s1**2)*(V_p1/V_p2)*np.sin(2*alpha_2), -(rho_2/rho_1)*(V_p1/V_s1)*np.cos(2*beta_2)],
                          [np.cos(2*beta_1), -(V_s1/V_p1)*np.sin(2*beta_1), -(rho_2/rho_1)*(V_p2/V_p1)*np.cos(2*beta_2), -(rho_2/rho_1)*(V_s2/V_p1)*np.sin(2*beta_2)]]
    Z = [[-np.sin(alpha_1)],
         [np.cos(alpha_1)],
         [np.sin(2*alpha_1)],
         [-np.cos(2*beta_1)]]
    Amplitude_1 = np.linalg.solve(Coefficient_matrix1,Z)
    return Amplitude_1

'''3.konnt方程求解'''
#系数矩阵Coefficient_matrix2，振幅Amplitude2
#振幅Amplitude2=[[A_2/A_1],[A_3/A_1],[A_4/A_1],[A_5/A_1]]的转置
def Amplitude2(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1):
    Coefficient_matrix2=[[np.sin(alpha_1),(V_p1/V_s1)*np.cos(beta_1),-(V_p1/V_p2)*np.sin(alpha_2),(V_p1/V_s2)*np.cos(beta_2)],
                         [np.cos(alpha_1),-(V_p1/V_s1)*np.sin(beta_1),(V_p1/V_p2)*np.cos(alpha_2),(V_p1/V_s2)*np.sin(beta_2)],
                         [np.sin(2*alpha_1),(V_p1**2/V_s1**2)*np.cos(2*beta_1),(V_p1**2/V_p2**2)*(V_s2**2/V_s1**2)*(rho_2/rho_1)*np.sin(2*alpha_2),-(rho_2/rho_1)*(V_p1**2/V_s1**2)*np.cos(2*beta_2)],
                         [np.cos(2*beta_1),-np.sin(2*beta_1),-(rho_2/rho_1)*np.cos(2*beta_2),-(rho_2/rho_1)*np.sin(2*beta_2)]]
    K=[[-np.sin(alpha_1)],
       [np.cos(alpha_1)],
       [np.sin(2*alpha_1)],
       [-np.cos(2*beta_1)]]
    Amplitude_2=np.linalg.solve(Coefficient_matrix2,K)
    return Amplitude_2

'''4.定义模型并求解'''
Incidence_angle = np.deg2rad(np.arange(0,90,1)) #定义参数

'''模型1'''
rho_1 = 2.45
rho_2 = 2.08
V_p1 = 3100
V_p2 = 2500
V_s1 = 1280
V_s2 = 1265
zoep_Ampl_1=[]
konnt_Ampl_1=[]
'''开始求解'''
for alpha_1 in Incidence_angle:
    beta_1 =  Reflection_angle(alpha_1,V_p1,V_s1) #使用斯奈尔定律求其他参数
    alpha_2 =  Reflection_angle(alpha_1,V_p1,V_p2)
    beta_2 =  Reflection_angle(alpha_1,V_p1,V_s2)
    Amp1=Amplitude1(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1) #调用zoeppritz方程求解振幅
    zoep_Ampl_1.append(Amp1)
    Amp2=Amplitude2(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1)#调用konnt方程求解振幅
    konnt_Ampl_1.append(Amp2)
    continue
#print(zoep_Ampl_1)
#print(konnt_Ampl_1)

'''模型2'''
rho_1 = 1.6
rho_2 = 2.4
V_p1 = 1500
V_p2 = 2060
V_s1 = 1280
V_s2 = 1650
zoep_Ampl_2=[]
konnt_Ampl_2=[]
'''开始求解'''
for alpha_1 in Incidence_angle:
    beta_1 =Reflection_angle(alpha_1,V_p1,V_s1) #使用斯奈尔定律求其他参数
    alpha_2 =Reflection_angle(alpha_1,V_p1,V_p2)
    beta_2 =Reflection_angle(alpha_1,V_p1,V_s2)
    Amp1=Amplitude1(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1) #调用zoeppritz方程求解振幅
    zoep_Ampl_2.append(Amp1)
    Amp2=Amplitude2(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1)#调用konnt方程求解振幅
    konnt_Ampl_2.append(Amp2)
    continue
#print(zoep_Ampl_2)
#print(konnt_Ampl_2)

'''模型3'''
rho_1 =2.45
rho_2 =1.35
V_p1 = 2560
V_p2 = 1980
V_s1 = 1860
V_s2 = 1300
zoep_Ampl_3=[]
konnt_Ampl_3=[]
'''开始求解'''
for alpha_1 in Incidence_angle:
    beta_1 =Reflection_angle(alpha_1,V_p1,V_s1) #使用斯奈尔定律求其他参数
    alpha_2 =Reflection_angle(alpha_1,V_p1,V_p2)
    beta_2 =Reflection_angle(alpha_1,V_p1,V_s2)
    Amp1=Amplitude1(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1) #调用zoeppritz方程求解振幅
    zoep_Ampl_3.append(Amp1)
    Amp2=Amplitude2(alpha_1,alpha_2,beta_1,beta_2,V_p1,V_p2,rho_2,rho_1,V_s2,V_s1)#调用konnt方程求解振幅
    konnt_Ampl_3.append(Amp2)
    continue
#print(zoep_Ampl_3)
#print(konnt_Ampl_3)

'''5.成图'''
#Amplitude1 = [[R_pp],[R_ps],[T_ps],[T_pp]]的转置
R_pp_1= [-i[0] for i in zoep_Ampl_1]
R_ps_1= [i[1] for i in zoep_Ampl_1]
R_pp_2= [-i[0] for i in zoep_Ampl_2]
R_ps_2= [i[1] for i in zoep_Ampl_2]
R_pp_3= [-i[0] for i in zoep_Ampl_3]
R_ps_3= [i[1] for i in zoep_Ampl_3]

plt.figure(1)
ax1 = plt.subplot()
ax1.plot(np.rad2deg(Incidence_angle), R_pp_1, color='tab:blue')      #第1条曲线  numpy.rad2deg将弧度转化为度，例如将Π/3转化为60°
ax1.plot(np.rad2deg(Incidence_angle), R_ps_1, color='tab:red')      #第2条曲线
ax1.set_title('Model_1')
ax1.set(xlim=[0,90])
plt.legend(['R_pp_1','R_ps_1']) #加图例
plt.xlabel('Incidence_angle')
plt.ylabel('Reflection coefficient')

plt.figure(2)
ax2 = plt.subplot()
ax2.plot(np.rad2deg(Incidence_angle), R_pp_2, color='tab:blue')
ax2.plot(np.rad2deg(Incidence_angle), R_ps_2, color='tab:red')
ax2.set_title('Model_2')
ax2.set(xlim=[0,90])
plt.legend(['R_pp_2','R_ps_2'])
plt.xlabel('Incidence_angle')
plt.ylabel('Reflection coefficient')

plt.figure(3)
ax3 = plt.subplot()
ax3.plot(np.rad2deg(Incidence_angle), R_pp_3, color='tab:blue')
ax3.plot(np.rad2deg(Incidence_angle), R_ps_3, color='tab:red')
ax3.set_title('Model_3')
ax3.set(xlim=[0,90])
plt.legend(['R_pp_3','R_ps_3'])
plt.xlabel('Incidence_angle')
plt.ylabel('Reflection coefficient')

plt.show()