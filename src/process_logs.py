import datetime
from collections import defaultdict


def parse_line(line: str):
    """Parse a log line and return a timestamp and severity level.

    The expected format is ISO timestamp followed by a severity word.
    """
    parts = line.strip().split()
    if not parts:
        raise ValueError("Empty log line")
    # First part is the timestamp, second is the level
    timestamp_str = parts[0]
    level = parts[1] if len(parts) > 1 else "INFO"
    timestamp = datetime.datetime.fromisoformat(timestamp_str)
    return timestamp, level


def compute_kpis(path: str):
    """Compute KPIs from a log file.

    KPIs include total requests, number of errors, error rate, and peak requests per minute.

    Args:
        path: Path to the log file.

    Returns:
        Dictionary of KPI values.
    """
    total_requests = 0
    errors = 0
    per_minute_counts = defaultdict(int)
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            timestamp, level = parse_line(line)
            total_requests += 1
            if level.upper() == "ERROR":
                errors += 1
            minute_bucket = timestamp.replace(second=0, microsecond=0)
            per_minute_counts[minute_bucket] += 1
    peak_rpm = max(per_minute_counts.values()) if per_minute_counts else 0
    error_rate = errors / total_requests if total_requests > 0 else 0
    return {
        "total_requests": total_requests,
        "errors": errors,
        "error_rate": error_rate,
        "peak_rpm": peak_rpm,
    }
