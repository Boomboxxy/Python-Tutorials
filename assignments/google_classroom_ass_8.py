def reverse(*args):
# will reverse each argument given
    print([i[-1::-1] for i in args])
reverse('abc','tuv','xyz')
