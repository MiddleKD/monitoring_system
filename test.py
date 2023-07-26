import threading
import time

from monitoring import ComputerResourceMonitor, print_and_get_flops_parameter

monitor = ComputerResourceMonitor()
monitor_thread = threading.Thread(target=monitor.monitor)
monitor_thread.start()

for x in range(10):
    monitor.restart()
    time.sleep(3)
    # print_and_get_flops_parameter(model=model, input_x=input_data)
    monitor.stop()

    result = monitor.print_and_get_results()
    monitor.reset()
    result = monitor.print_and_get_results()

monitor.kill()
    