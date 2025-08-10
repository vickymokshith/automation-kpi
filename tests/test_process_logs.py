import tempfile
from src.process_logs import compute_kpis


def test_compute_kpis() -> None:
    """Compute KPIs on a small synthetic log and verify keys and counts."""
    log_content = "\n".join([
        "2025-08-10T00:00:00 INFO Start",
        "2025-08-10T00:01:00 ERROR Something failed",
        "2025-08-10T00:01:30 INFO Continue",
    ])
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(log_content)
        f.flush()
        kpis = compute_kpis(f.name)
    assert set(kpis.keys()) == {"total_requests", "errors", "error_rate", "peak_rpm"}
    assert kpis["total_requests"] == 3
    assert kpis["errors"] == 1
    assert abs(kpis["error_rate"] - 1/3) < 1e-6
