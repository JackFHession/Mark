from nl_processing.process_input import *

import socket
import threading
import json

from utils.servertk import *

def server_main():
    # Start server for port 2040
    server_thread_2040 = threading.Thread(target=start_server, args=(2040,))
    server_thread_2040.start()

    # Start server for port 2060
    server_thread_2060 = threading.Thread(target=start_server, args=(2060,))
    server_thread_2060.start()

    # Wait for both threads to finish
    server_thread_2040.join()
    server_thread_2060.join()

if __name__ == "__main__":
    server_main()
