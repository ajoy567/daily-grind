def count_levels(lines: list[str]) -> dict[str, int]:
    """
    Count the occurrences of each log level in the given lines.

    Args:
        lines (list[str]): A list of log lines.

    Returns:
        dict[str, int]: A dictionary with log levels as keys and their counts as values.
    """
    
    level_counts: dict[str, int] = {}
    
    for line in lines:
        words = line.split()
        if not words:
            continue
        level = words[0].upper()
        if level in level_counts:
            level_counts[level] += 1
        else:
            level_counts[level] = 1
    return level_counts
    
logs = [
    "INFO server started",
    "INFO user logged in",
    "WARN disk usage at 85%",
    "ERROR db timeout",
    "INFO user logged out",
    "ERROR payment failed",
    "WARN slow response",
    "info health check ok",
]

print(count_levels(logs))  # Output: {'INFO': 4, 'WARN': 2, 'ERROR': 2}

def level_percentage(level_counts: dict[str, int]) -> dict[str, float]:
    """
    Calculate the percentage of each log level based on their counts.

    Args:
        level_counts (dict[str, int]): A dictionary with log levels as keys and their counts as values.

    Returns:
        dict[str, float]: A dictionary with log levels as keys and their percentage as values.
    """
    
    total_logs = sum(level_counts.values())
    if total_logs == 0:
        return {level: 0.0 for level in level_counts}
    
    percentages: dict[str, float] = {}
    for level, count in level_counts.items():
        percentages[level] = (count / total_logs) * 100
    return percentages

percentages = level_percentage(count_levels(logs))

for level, percentage in percentages.items():
    print(f"{level}: {percentage:.2f}%")
    if percentage > 80:
        print(f"Warning: {level} logs exceed 80% of total logs. Possible issue detected.")