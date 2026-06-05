def interval_scheduling(tasks):
    """
    Given a list of tuples of tasks representing (task_name, start_time, duration) returns a list containing the
    maximum number of tasks possible and the tasks in the of (task_name, start_time, end_time)
    :param tasks: a list of tuples of tasks representing (task_name, start_time, duration)
    :return: a list of tuples of tasks representing (task_name, start_time, end_time)
    """

    sorted_tasks = sorted(tasks, key=lambda x: x[1] + x[2])
    possible_tasks = []
    current_time = 0

    for task, start, duration in sorted_tasks:
        if current_time <= start:
            current_time = start + duration
            possible_tasks.append((task, start, duration + start))

    return possible_tasks