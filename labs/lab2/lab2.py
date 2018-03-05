
# coding: utf-8

# # Intro to Mathematical logic, Jupyter Notebook
# 
# ## Installation
# * pip install pyDatalog
# 
# ## Tasks
# * Extend rules for the salary at your own company. Namely add progressive tax rate depending on salary tax_rate=f(salary)
# * Add working time and calculate the total salary for every employee
# * Make filter form for employees

# In[41]:


from pyDatalog import pyDatalog
def twice(a):
    return a+a
pyDatalog.create_terms('X,Y,Z,Arr')

print('Set the X var to 1')
print(X==1)
print()
print('Assignment of 2 Vars')
print((X==True) & (Y==False))
print()

print('Assignment n times, to n values')
print(Arr.in_((0,1,2,3,4)))
print()

print('Just another case N assignment')
print(Arr.in_(range(5)))
print()

print('Filtering')
print(X.in_(range(5)) & (X<2))
print()

print('Term of function')
pyDatalog.create_terms('twice')
print((X==2) & (Y==twice(X)))
print()
print('Combination Assignment and Filtering')
print(X.in_(range(5)) & 
     Y.in_(range(5)) & 
     (Z==X*Y))
print('Filtering')
print(Y.in_(range(5)) & (Y>2))
print()
print(len(Z))


# In[45]:


from ipywidgets import interact_manual
from pyDatalog import pyDatalog
import math
pyDatalog.create_terms('employee, net_salary, tax_rate, salary, hours')
+(tax_rate[salary])
@interact_manual
def get_input(name='User', salary=100, hours = 5):
    tax_rate[salary] = salary ** 0.5
    employee[name]=salary * hours
    net_salary[X] = employee[X] - 2 * tax_rate[salary]
    print(net_salary[X]==Y)
    print('Filtering')
    #print(net_salary[X])
    #print(list(net_salary[X] == Y))
    #print users who have salary more than 500
    print(net_salary[X] > 500)
    print()


# In[40]:


print(net_salary[X]==Y)

