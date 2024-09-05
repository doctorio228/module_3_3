def print_params(a=1,b='ctr',c=True):
    print(f' a: {a},b: {b}, c: {c}')
print_params()
print_params(2)
print_params(2,'not')
print_params(2,'not',False)
print_params(b=25)
print_params(c=[1,2,3])
values_list = [True,1,"klj"]
values_dict = {'a': 'lol', 'b': 5, 'c': False}
print_params(**values_dict)
print_params(*values_list)
values_list_2 = [43.34,'tor']
print_params(*values_list_2, 42)

