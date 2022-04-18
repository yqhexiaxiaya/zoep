# zoeppritz
This is a equation about zoep and konnt.
# zoeppritz和konnt方程求解
## 1. 使用必备
### 请自行安装numpy和matplotlib
## 2.代码注释
定义斯奈尔定律
```python
def Reflection_angle(Incidence_angle,V_1,V_2):  
    p = np.sin(Incidence_angle)/V_1  
    Reflection_angle = np.arcsin(p*V_2)  
    return Reflection_angle
```
定义zoeppritz方程
```python
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
```

 定义konnt方程
 ```python
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
```
## 3.模型定义
## 4.成图
此处语句重复，可进一步优化
:smile:
