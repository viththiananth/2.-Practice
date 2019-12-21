print(['a', 'b', 'c'] + [1, 2, 3])

print(lambda x: x+1)

print([x**2 for x in range(10)] )

import numpy as np
f=np.arange(0,36,1)
r=f.reshape(1,6,6)

print(r[2:4,2:4])