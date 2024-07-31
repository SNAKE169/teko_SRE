
# Rate Limiting Function

This Python script implements a rate limiting function to control the number of requests that can be processed within a given time frame. The function takes the number of requests, the rate limit per hour, and a list of timestamps in ISO-8601 format, and returns a list of boolean values indicating whether each request is allowed based on the rate limit.

## Usage

### Function Definition

The function `rate_limit` is defined to handle the rate limiting logic. It converts the timestamps from ISO-8601 format to datetime objects, keeps track of requests within the last hour, and checks if adding a new request would exceed the rate limit.

### Example Usage

Here is an example of how to use the `rate_limit` function:

1. Define the number of requests `N` and the rate limit per hour `R`.
2. Prepare a list of timestamps in ISO-8601 format.
3. Call the `rate_limit` function with these parameters to get the results.

```
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
```

### Output

The `results` list will contain boolean values indicating whether each request is allowed or not. For the provided example, the output will be:

```
[True, True, True, False, True, False, True, True, False, False]
```

## Explanation

1. **Conversion of Timestamps**: The input timestamps are converted from ISO-8601 format to `datetime` objects for easier manipulation.
2. **Tracking Requests**: A list, `request_times`, is maintained to keep track of the timestamps of the requests within the last hour.
3. **Removing Old Requests**: For each incoming request, the function removes timestamps from `request_times` that are older than one hour from the current timestamp.
4. **Rate Limiting Check**: It checks if the current number of requests within the last hour is less than the rate limit `R`. If yes, the current request is accepted (`True`) and its timestamp is appended to `request_times`. If not, the request is rejected (`False`).

## Requirements

- Python 3.6 or higher

## Running the Script

To run the script, change the input according to your preference, simply run ```python rate_limit.py```. 
The output will be printed to the console.
