import schedule
import time
import yaml
from importlib import import_module

def task1():
    with open("configs/config1.yaml", 'r') as file:
        config = yaml.safe_load(file)
        task_module = import_module(f'tasks.{config["task"]}')
        task_module.run(config)

def task2():
    with open("configs/config2.yaml", 'r') as file:
        config = yaml.safe_load(file)
        task_module = import_module(f'tasks.{config["task"]}')
        task_module.run(config)

def task3():
    with open("configs/config3.yaml", 'r') as file:
        config = yaml.safe_load(file)
        task_module = import_module(f'tasks.{config["task"]}')
        task_module.run(config)

schedule.every(2).minutes.do(task1)
schedule.every(2).minutes.do(task2)
# schedule.every(3).minutes.do(task3)

while True:
    schedule.run_pending()
    time.sleep(1)