# https://morvanzhou.github.io/tutorials/python-basic/threading/2-add-thread/
import threading

def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    
if __name__ == '__main__':
    main()