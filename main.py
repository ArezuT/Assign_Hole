# Returns minimum time required to place mice in holes using the Greedy approach. We can put every mouse to its nearsest hole to minimize the time. This can be doen by sorting the positions of mice and holes.

def assignHole(mice, holes):

    # Base - num of mice and holes should be the same
    if len(mice) != len(holes):
      return "Number of mice and holes not the same"

    # Sort first
    mice.sort()
    holes.sort()

    #Finding max difference between the mice and hole
    max_diff = 0

    for i in range(len(mice)):
      if max_diff < abs(mice[i] - holes[i]):
        max_diff = abs(mice[i] - holes[i])

    return max_diff

mice = [4, -4, 2]
holes = [4, 0 ,5]

#The required answer is returned from the function
min_time = assignHole(mice, holes)

print ("The last mouse gets into the hole in time:", min_time)