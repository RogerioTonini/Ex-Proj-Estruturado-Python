import sys
import site


print(site.getsitepackages())
print('')
print('')
for path in sys.path:
    print(path)
