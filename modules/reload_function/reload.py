'''Simple program to show how to reload an imported mpdule, since multiple import statements
of the same module, will only be loaded once.'''

import importlib
import sample

importlib.reload(sample)
importlib.reload(sample)
importlib.reload(sample)
importlib.reload(sample)
