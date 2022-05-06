# Ensure unicity of object
# To be used like this
# class MyClass(BaseClass, metaclass=Singleton):
#    pass


class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]
