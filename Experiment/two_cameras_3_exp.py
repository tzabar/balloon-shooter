import cvpubsubs.webcam_pub as w
from cvpubsubs.window_sub import SubscriberWindows

t1 = w.VideoHandlerThread(0)
t2 = w.VideoHandlerThread(1)

t1.start()
t2.start()

SubscriberWindows(window_names=['cammy', 'cammy2'], video_sources=[0, 1]).loop()

t1.join()
t1.join()
