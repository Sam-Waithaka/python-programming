import importlib
import file_changes

def changes():
    try:
        importlib.reload(file_changes)
        file_changes.print_changes()
    except:
        pass


for i in range (10):
    changes()