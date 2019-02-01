
import numpy as np

boxes = open("input/inputDay2.txt",'r')

## Part 1
sqFtWrappingPaper = 0
for line in boxes:
	dimensions = line.rstrip().split('x')
	dimensions = map(int, dimensions)
	shiftedDimensions = dimensions[1:] + dimensions[:1] # Shift dimensions so you can multiply them in order to calculate surfaces
	surfaces = np.multiply(dimensions, shiftedDimensions) # Element-wise product
	sqFtWrappingPaper += sum(2 * surfaces)
	sqFtWrappingPaper += min(surfaces)
	
print(sqFtWrappingPaper)


## Part 2
boxes.seek(0) # Set the UNIX read-write pointer back to the beginning
ftRibbon = 0
for line in boxes:
	dimensions = line.rstrip().split('x')
	dimensions = map(int, dimensions)
	smallestDimensions = sorted(dimensions)[:-1]
	ftRibbon += sum(2 * smallestDimensions)
	ftRibbon += np.product(dimensions)

print(ftRibbon)


boxes.close()
