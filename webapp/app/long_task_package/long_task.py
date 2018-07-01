import time
try:
    from concurrent import futures
except ImportError:
    import futures
import sys

N_WORKERS = 5

def long_task(duration):
    time.sleep(duration)
    return {'task': True}

def parallel_long_task(duration):
    # create N parallel subtasks
    reduced_durations = []
    for a in range(1, N_WORKERS + 1):
        reduced_durations.append(float(duration) / N_WORKERS)

    completed = 0
    failed = 0
    with futures.ThreadPoolExecutor(
            max_workers=N_WORKERS) as executor:
        future_list = {
            executor.submit(
                long_task, reduced): reduced for reduced in reduced_durations}
        for future in futures.as_completed(future_list):
            sub_task_num = future_list[future]
            try:
                result = future.result()
            except Exception:
                failed += 1
            else:
                if result == {'task': True}:
                    completed += 1
                else:
                    failed += 1

    return {'completed_subtasks': completed, 'failed_subtasks' : failed}
