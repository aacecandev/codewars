import weakref

class Foo(object):
    pass

x = weakref.proxy(Foo())
