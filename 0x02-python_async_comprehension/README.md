## Python Async Comprehension Project
This project demonstrates the use of asynchronous comprehensions in Python.
It consists of three tasks, each building upon the previous one.

## Task 0: Aync Generator
This task involves creating a coroutine called `async_generator` that takes no arguments. The coroutine loops 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10.

## Task 1: Async Comprehension
This task import the `Async_generator` from the previous task and then writes a coroutine called `async_comprehension` that takes no arguments. The coroutine collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 random numbers.

## Task 2: Measure Runtime
This task imports `async_comprehension` from the previous task and writes a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` measures the total runtime and returns it.

## Usage
Each task is contained in its own Python script. To run a task, use the following command:
```bash
./<script_name>.py
Replace <script_name> with the name of the script you want to run.

Requirements
- Python 3.7+
- asyncio library

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Author
- Yours Truly
Congo J Migue 