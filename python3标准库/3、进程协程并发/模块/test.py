import subprocess
import time
from threading import Timer, Thread
from time import sleep
from typing import List


def execute(cmd):
    """
    执行命令行
    :param cmd:
    :return:
    """
    clock = 10  # 设置超时时间
    now_time = time.time()  # 命令执行前当前时间
    while True:  # 循环创建执行命令子进程，在特定时间后退出
        ret = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)  # 创建子进程
        Timer(clock, kill_cammand, [ret]).start()  # 启动计时器,clock秒后kill掉该子进程
        stdout = ret.communicate()[0]  # 获取命令执行结果
        if stdout:  # 判断结果是否存在
            endtime = time.time()  # 获取结果后当前时间
            clock = 10 - (endtime - now_time)  # 更新超时时间
            print(stdout)
            sleep(1)
            continue  # 结果存在,继续循环创建子进程
        else:
            break  # 结果不存在，退出当前循环，等超时时间到，kill掉子进程，程序退出


def kill_cammand(ret):
    """
    kill掉创建的子进程
    :param ret:
    :return:
    """
    ret.kill()


if __name__ == '__main__':
    # execute()
    thread_list = []  # 子线程列表
    cmd_list = [['date'], ['ls', '-l']]  # 要执行的命令列表
    for cmd in cmd_list:
        thread_01 = Thread(target=execute, args=(cmd,))  # 创建子线程
        thread_01.start()  # 开始子线程
        thread_list.append(thread_01)
    [j.join() for j in thread_list]  # 主线程阻塞等待,统一回收子线程
