def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func