import random

def One_or_Zero(value):
# Функция для кодирования
  if value == 'robot':
    return 0
  else:
    return 1


lst = ['robot']*10
lst += ['human']*10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

onehot_data = pd.get_dummies(data['whoAmI']) # реализация OneHot через встроенную функцию
onehot_data_Myself_func = data['whoAmI'].apply(One_or_Zero) # реализация OneHot через собственную функцию
data['whoAmI_onehot'] = onehot_data_Myself_func
data.head()
