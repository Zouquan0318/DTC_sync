# get_name_path.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

# 从 obs_browser.py 导入 upload_to_obs 函数
from obs_browser import upload_to_obs

class Watcher:
    def __init__(self, directory_to_watch):
        self.observer = Observer()
        self.directory_to_watch = directory_to_watch

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory_to_watch, recursive=True)
        self.observer.start()
        try:
            while True:
                # 这里可以执行其他任务，或者使用time.sleep()来等待事件
                pass
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None
        else:
            # 获取文件的完整路径
            full_path = event.src_path
            # 获取文件名
            filename = os.path.basename(full_path)
            # 调用上传函数
            upload_to_obs(full_path, filename)

if __name__ == '__main__':
    w = Watcher(directory_to_watch="C:/Users/awosh/Desktop/DTC_SYNC")
    w.run()
