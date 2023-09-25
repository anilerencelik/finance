import schedule
import time
import yaml
from importlib import import_module
from utils.time import isWorkingHours

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

def scheduleWorkingHours():
    schedule.every(5).minutes.do(task1)
    schedule.every(5).minutes.do(task2)
    schedule.every().day.at("18:15").do(task3)

print("Starting Finance App")
scheduleWorkingHours()
while True:
    if isWorkingHours():
        schedule.run_pending()
    else: 
        schedule.clear()
        scheduleWorkingHours()
    time.sleep(1)