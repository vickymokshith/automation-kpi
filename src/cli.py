import argparse
import json
from process_logs import compute_kpis


def main() -> None:
    """Entry point for the KPI CLI."""
    parser = argparse.ArgumentParser(description="Compute log KPIs")
    parser.add_argument("--log", required=True, help="Path to the log file")
    args = parser.parse_args()
    kpis = compute_kpis(args.log)
    print(json.dumps(kpis, indent=2))


if __name__ == "__main__":
    main()
