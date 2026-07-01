def person(**kargs):
    for i in kargs.items():
        print(i)
    return
person(name='anu',age=23,place='kochi')