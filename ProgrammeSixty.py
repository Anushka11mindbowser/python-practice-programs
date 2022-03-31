#Approach One : Using inbuilt dictionary functions

my_dict ={'harry potter': 'j.k.rowling', 'famous five' : 'enid blyton', 'the da vinci code': 'dan brown', 'the alchemist': 'paulo cohelo', '1984':'george orwell'}
if 'harry potter' in my_dict.keys():
    del my_dict['harry potter']
    print(my_dict)

#Approach Two: Using

def delete_items(param):
    if param.get('the alchemist', 0):
        del param['the alchemist']
    print(param)

print(delete_items(my_dict))