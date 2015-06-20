def jump_time(leaf, border, max_jump):
    # Frog can cross in a single jump
    if max_jump >= border:
        return 0
    
    position = 0

    for t in range(0, len(leaf)):
        # Frog can reach the border from current position
        if position + max_jump >= border:
            # Frog could reach the border the previous second
            return t - 1
        # Leaf closest to the border, and frog can jump
        jump_distance = leaf[t] - position
        if leaf[t] > position and jump_distance <= max_jump:
            # Frog jumps
            position = leaf[t]
        
    return -1
