# Ensure unicity of object
# To be used like this
# class MyClass(BaseClass, metaclass=Singleton):
#    pass


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
