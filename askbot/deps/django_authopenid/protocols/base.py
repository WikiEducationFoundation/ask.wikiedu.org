class BaseProtocol(object):
    """Base class for all authentication protocols"""

    def __iter__(self):
        """makes objects iterable and enables the 'in' operator'"""
        attrs = dir(self)
        prop_names = tuple()
        for attr in attrs:
            item = getattr(self, attr)
            if hasattr(item, '__call__'):
                continue
            prop_names += (attr,)
        return iter(prop_names)
