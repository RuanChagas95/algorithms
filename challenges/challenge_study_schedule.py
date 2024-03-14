def study_schedule(permanence_period, target_time):
    count = 0
    if not (isinstance(target_time, int)):
        return None
    for start, end in permanence_period:
        if not (isinstance(start, int)
                and isinstance(end, int)):
            return None
        if (start <= target_time <= end):
            count += 1
    return count
