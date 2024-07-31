from datetime import datetime, timedelta

def rate_limit(N, R, timestamps):
    # Convert the timestamps from ISO-8601 format to datetime objects
    times = [datetime.fromisoformat(ts.replace("Z", "+00:00")) for ts in timestamps]
    
    # Initialize a list to keep track of the requests within the last hour
    request_times = []
    
    results = []
    for current_time in times:
        # Remove timestamps that are older than 1 hour from the current time
        one_hour_ago = current_time - timedelta(hours=1)
        request_times = [time for time in request_times if time > one_hour_ago]
        
        # Check if adding the current request would exceed the rate limit
        if len(request_times) < R:
            results.append(True)
            request_times.append(current_time)
        else:
            results.append(False)
    
    return results

# Example usage with provided timestamps
N = 10
R = 3
timestamps = [
    "2022-01-20T00:13:05Z",
    "2022-01-20T00:27:31Z",
    "2022-01-20T00:45:27Z",
    "2022-01-20T01:00:49Z",
    "2022-01-20T01:15:45Z",
    "2022-01-20T01:20:01Z",
    "2022-01-20T01:50:09Z",
    "2022-01-20T01:52:15Z",
    "2022-01-20T01:54:00Z",
    "2022-01-20T02:00:00Z"
]

results = rate_limit(N, R, timestamps)
print(results)
