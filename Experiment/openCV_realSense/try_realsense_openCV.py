import pyrealsense2 as rs
import cv2
import numpy as np
from time import sleep

# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
config = rs.config()
config.disable_all_streams()
config.enable_stream(stream_type=rs.stream.color, width=640, height=480, format=rs.format.bgr8, framerate=30)
pipeline.start(config)
while(True):
    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    color_image = np.asanyarray(color_frame.get_data())
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('RealSense', color_image)
    cv2.waitKey(1)
# sleep(3)
pipeline.stop()