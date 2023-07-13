import cv2
from ultralytics import YOLO


# Load the YOLOv8 model
model = YOLO('yolov8s-pose.pt')

# Open the video file
#video_path = "video.mp4"
#cap = cv2.VideoCapture(video_path)
#打开摄像头
#cap = cv2.VideoCapture(0) 

# Loop through the video frames
frame = cv2.imread('hutao.jpg')
results = model(frame)

        # Visualize the results on the frame
annotated_frame = results[0].plot()


# 定义鼠标事件处理函数
def mouse_callback(event, x, y, flags, param):
    # 如果检测到鼠标右键点击事件，关闭图像窗口
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.destroyAllWindows()


# 创建窗口并显示图像
cv2.imshow("YOLOv8 Inference", annotated_frame)

# 设置鼠标事件回调函数
#cv2.setMouseCallback("YOLOv8 Inference", mouse_callback)

# 持续显示图像直到关闭窗口
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 关闭窗口
cv2.destroyAllWindows()



