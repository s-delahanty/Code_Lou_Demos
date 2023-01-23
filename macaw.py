# How many macaws does it take to lift a coconut?
import math
perc = 1/3
coco_wt = 1450
macaw_wt = 900
macaw_limit = macaw_wt * perc
num_macaws = coco_wt/macaw_limit
math.ceil(num_macaws)
print(num_macaws)