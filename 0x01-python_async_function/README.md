# Title: Python Async Function
This project demonstrates the use of asynchronous coroutines and tasks in 
Python using the asyncio library.

## Files
0. `0-basic_async_async_syntax.py`: Contains the `wait_random` coroutine
 that waits for a random delay and returns it.
1. `1-concurrent_coroutines.py`: Contains the `wait_n` coroutine
 that spawns `wait_random` n times and returns a list of all the 
 delays in ascending order.
2. `2-measure_runtime.py`: Contains the `measure_time` function that measures
 the total execution time for `wait_n(n, max_delay)` and returns 
 total_time / n. Your function should return a float.
3. `3-task.py`: Contains the `task_wait_random` function that takes an integer
 max_delay and returns a asyncio.Task.
4. `4-tasks.py`: Contains the `task_wait_n` coroutine that spawns 
`task_wait_random` n times and returns a list of all the delays in 
ascending order.

## Usage
Each python file can be run independently. For example, 
`0-basic_async_syntax.py`, use the following command:
```bash
python3 0-basic_async_syntax.py
You can replace 0-basic_async_syntax.py with the name of any other Python
 file in this project to run it.

Requirements
- Python 3.7+
- asyncio library

Author
Yours Truly
Congo J Migue