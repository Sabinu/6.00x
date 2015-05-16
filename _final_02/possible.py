
# PROBLEM 4-1  (1 point possible)
# Solid Walls
    if x+dx > leftEdge and x+dx < rightEdge:
        x += dx
    if y+dy > bottomEdge and y+dy < topEdge:
        y += dy

# PROBLEM 4-2  (1 point possible)
# None of Above
    if x+dx < rightEdge and x+dx > leftEdge:
        x += dx
    elif x+dx > rightEdge:
        x = leftEdge
    elif x+dx < leftEdge:
        x = rightEdge
    if y+dy < topEdge and y+dy > bottomEdge:
        y += dy
    elif y+dy > topEdge:
        y = topEdge
    elif y+dy < bottomEdge:
        y = bottomEdge

# PROBLEM 4-3  (1 point possible)
# Small Planet
    if x+dx > leftEdge and x+dx < rightEdge:
        x += dx
    elif x+dx > rightEdge:
        x = leftEdge + (x+dx - rightEdge)
    elif x+dx < leftEdge:
        x = rightEdge - (leftEdge - (x+dx))

    if y+dy > bottomEdge and y+dy < topEdge:
        y += dy
    elif y+dy > topEdge:
        y = bottomEdge + (y+dy - topEdge)
    elif y+dy < bottomEdge:
        y = topEdge - (bottomEdge - (y+dy))

# PROBLEM 4-4  (1 point possible)
# None of Above
    if x+dx < rightEdge and x+dx > leftEdge:
        x += dx
    elif x+dx > rightEdge:
        x = bottomEdge
    elif x+dx < leftEdge:
        x = topEdge
    if y+dy < topEdge and y+dy > bottomEdge:
        y += dy
    elif y+dy > topEdge:
        y = leftEdge
    elif y+dy < bottomEdge:
        y = rightEdge

# PROBLEM 4-5  (1 point possible)
# None of Above
    if x+dx > rightEdge:
        x = y
    if x+dx < leftEdge:
        x = y
    if x+dx < rightEdge and x+dx > leftEdge:
        x += dx
    if y+dy > topEdge:
        y = x
    if y+dy < bottomEdge:
        y = x
    if y+dy < topEdge and y+dy > bottomEdge:
        y += dy

# PROBLEM 4-6  (1 point possible)
# None of Above
    if x+dx > rightEdge:
        x, y = (rightEdge-leftEdge)/2
    if x+dx < leftEdge:
        x, y = (rightEdge-leftEdge)/2
    if x+dx < rightEdge and x+dx > leftEdge:
        x += dx
    if y+dy > topEdge:
        x, y = (rightEdge-leftEdge)/2
    if y+dy < bottomEdge:
        x, y = (rightEdge-leftEdge)/2
    if y+dy < topEdge and y+dy > bottomEdge:
        y += dy

# PROBLEM 4-7  (1 point possible)
# Back Home
    if x+dx < rightEdge and x+dx > leftEdge\
       and y+dy < topEdge and y+dy > bottomEdge:
        x += dx
        y += dy
    else:
        x = leftEdge + (rightEdge-leftEdge)/2
        y = bottomEdge + (topEdge-bottomEdge)/2