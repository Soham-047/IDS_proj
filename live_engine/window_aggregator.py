import time
from collections import deque

WINDOW_SIZE = 5  # seconds
flow_window = deque()

def add_flow(flow):
    """
    Add a flow to the sliding window
    """
    now = time.time()
    flow["timestamp"] = now
    flow_window.append(flow)

    # Remove expired flows
    while flow_window and now - flow_window[0]["timestamp"] > WINDOW_SIZE:
        flow_window.popleft()


def aggregate_features():
    """
    Aggregate behavior from flows in the window
    """
    if not flow_window:
        return None

    total_flows = len(flow_window)
    total_orig_bytes = sum(f["orig_bytes"] for f in flow_window)
    total_resp_bytes = sum(f["resp_bytes"] for f in flow_window)
    avg_duration = sum(f["duration"] for f in flow_window) / total_flows

    return [
        total_flows,
        total_orig_bytes,
        total_resp_bytes,
        avg_duration
    ]
    return features

