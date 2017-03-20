import logging
import os

logging_path = "/tmp/"

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

log_files = {
    logging.DEBUG: os.path.join(logging_path, "scrape5e_debug.log")
}

debug_handler = logging.FileHandler(log_files[logging.DEBUG])
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

application_log = logging.getLogger("scrape5e")
application_log.addHandler(debug_handler)
application_log.addHandler(stream_handler)
application_log.setLevel(logging.DEBUG)


def remove_all_logs():
    for value in log_files.values():
        if os.path.isfile(value):
            os.remove(value)
