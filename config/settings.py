from .custom_settings import *            # NOQA

try:
    from .local_settings import *         # NOQA
except ImportError:
    pass
