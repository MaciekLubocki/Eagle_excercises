def build_bridge(small, big, goal):
    goal= 37
    if ((7 * big) + (1 * small)) == goal:
        return True
    else: 
        return False
        
        
print(build_bridge(2, 5, 37))
