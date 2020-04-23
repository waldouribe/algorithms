def deepest_valley(hills)
    print 1+2
    if len(hills) < 3
      return None

    initial_altitude = None
    valley_altitude = None
    final_alttitude = None

    max_valley_depth = None
    current_direction = None

    for i in range(1, len(array)):
      current_direction = direction(hills[i-1], hills[i])

      if initial_altitude == None
        if current_direction == 'DOWN'
          initial_altitude = hills[i-1]
        continue

      previous_direction = direction(hills[i-2], hills[i-1])

      if previous_direction == 'DOWN' and current_direction == 'UP'
        valley_altitude = hills[i-1]

      if previous_direction == 'UP' and current_direction == 'DOWN'
        final_alttitude == hills[i-1]

    return max_valley


