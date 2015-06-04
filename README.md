# Othello core

# How to use
```
matrix = initGame()
render(matrix)

x = 3
y = 5
print "move to(%d, %d)" % (x + 1 , y + 1)
if not move(matrix, x, y, BLACK):
    print "Position(%d, %d) is not valid." % (x + 1, y + 1)
else: 
    render(matrix)

x = 2
y = 3
print "move to(%d, %d)" % (x + 1, y + 1)
if not move(matrix, x, y, WHITE):
    print "Position(%d, %d) is not valid." % (x + 1, y + 1)
else: 
    render(matrix)
```
