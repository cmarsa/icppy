# object_id
'''
Different objects can be verified using the
built-in Python function `id` , which returns a unique integer identifier for an
object. This function allows us to test for object equality.
'''

techs = ['MIT', 'Caltech']
ivys = ['Harvard', 'Yale', 'Brown']
print('techs: ', techs)
print('ivys: ', ivys)
print('')

univs = [techs, ivys]
univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
print('univs = [techs, ivys]')
print("univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]")
print('univs: ', univs)
print('univs1: ', univs1)
print('')

print('test value equality: ', univs == univs1)              #test value equality
print('test object equality: ', id(univs) == id(univs1))      #test object equality
print('Id of Univs =', id(univs))
print('Id of Univs1 =', id(univs1))
print('')

techs.append('RPI')
print('techs.append(\'RPI\')')
print('techs: ', techs)
print('ivys: ', ivys)
print('univs: ', univs)
print('univs1: ', univs1)
print('')