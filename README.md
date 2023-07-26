# monitoring_system
컴퓨터 리소스를 모니터링하는 코드입니다.


## CPU, GPU, RAM, time 모니터링

### Usage
```python
import threading
from monitoring import ComputerResourceMonitor

monitor = ComputerResourceMonitor()
monitor_thread = threading.Thread(target=monitor.monitor)
monitor_thread.start()

# your test code

monitor.kill()
```

* `ComputerResourceMonitor`: 모니터링 시스템을 불러옵니다. object는 stop state로 생성되기 때문에, `restart`가 필요합니다.
* `monitor.restart()`: 시스템을 다시 시작합니다. CPU, GPU, RAM, consumed time을 측정합니다.
* `monitor.stop()`: 시스템을 정지합니다. 기록된 리소스는 리스트의 형태로 메모리에 남아있습니다. `restart`하면 다시 이어서 기록을 시작합니다.
* `monitor.reset()`: 기록된 리소스 리스트를 초기화합니다.
* `monitor.kill()`: 시스템을 완전히 정지해야합니다. object가 삭제됩니다.

### Return
```python
{"avg_cpu":avg_cpu, "max_cpu":max_cpu,\
"avg_ram":avg_ram, "max_ram":max_ram,\
"avg_gpu":avg_gpu, "max_gpu":max_gpu,\
"avg_time":avg_time, "max_time":max_time}
```

---

## AI모델 flops, parameters 모니터링

### Usage
```python
from monitoring import print_and_get_flops_parameter

model = my_model # it is your own model
input_data = my_data # it is your own data like tensor

print_and_get_flops_parameter(model=model, input_x=input_data)
```

### Return 
```python
{"flops":flops, "params":params}
```
