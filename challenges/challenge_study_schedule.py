def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
   
    count = 0

    for period in permanence_period:
        if None in period:
            return None
        
        start_time, end_time = period
        if isinstance(start_time, str) or isinstance(end_time, str):
            return None
        
        if start_time <= target_time <= end_time:
            count += 1
        
    return count



