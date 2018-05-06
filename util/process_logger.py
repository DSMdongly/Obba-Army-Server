from multiprocessing import current_process

"""
    Logger module for logging
    from multiple process
"""


def log(level, message):
    current_process_name = current_process().name
    print('[{0}: {1}] {2}'.format(current_process_name, level, message))
