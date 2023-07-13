import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import cv2
from ultralytics import YOLO
import addjpg
import singup
class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)

        self.master = master

        self.pack()
        self.model = YOLO('yolov8s-pose.pt')

        self.create_widgets()
    

    def create_widgets(self):
        self.addjpgbtn = tk.Button(self,text = "注册员工",width = 10,height = 5,command = self.addjpg,padx=5,bg = "red")
        self.addjpgbtn.grid(row = 0,column = 0)

        self.indoorbtn = tk.Button(self,text = "门禁系统",width = 10,height = 5,command = self.goin,padx=5,bg = "yellow")
        self.indoorbtn.grid(row = 1,column = 0)

        self.picturebtn = tk.Button(self,text = "打开图片",width = 10,height = 5,command = self.picturepre,padx=5,bg = "red")
        self.picturebtn.grid(row = 0,column = 1)   

        self.videobtn = tk.Button(self,text = "打开视频",width = 10,height = 5,command = self.videopre,padx=5,bg = "red")
        self.videobtn.grid(row = 1,column = 1)

        self.camerabtn = tk.Button(self,text = "打开摄像头",width = 10,height = 5,command = self.camerapre,padx=5,bg = "red")
        self.camerabtn.grid(row = 2,column = 1)

        self.quitbtn = tk.Button(self,text = "退出",width = 5,height = 3,command = self.master.destroy,padx=5,bg = "blue")
        self.quitbtn.grid(row = 3,column = 3)

    def goin(self):

        singup.goin()
        pass

    def addjpg(self):
        addjpg.select_file()
        messagebox.showinfo(title = "提示",message = "员工注册成功！")
        pass


    def picturepre(self):
        # 选择图像文件
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        frame = cv2.imread(file_path)

        cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)  # 创建可调整大小的窗口
        cv2.resizeWindow("YOLOv8 Inference", 500, 300)  # 设置初始窗口大小
        
        print("选择的图像文件路径：", file_path)
        results = self.model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

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
        
    
    def videopre(self):
        # 选择视频文件
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])

        # 打印视频文件路径
        print("选择的视频文件路径：", file_path)
        cap = cv2.VideoCapture(file_path)
        cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)  # 创建可调整大小的窗口
        cv2.resizeWindow("YOLOv8 Inference", 500, 300)  # 设置初始窗口大小
        
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()

            if success:
        # Run YOLOv8 inference on the frame
                results = self.model(frame)

        # Visualize the results on the frame
                annotated_frame = results[0].plot()

        # Display the annotated frame
                cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
        # Break the loop if the end of the video is reached
                break

# Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()
        

    def camerapre(self):
        cap = cv2.VideoCapture(0)
        cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)  # 创建可调整大小的窗口
        cv2.resizeWindow("YOLOv8 Inference", 500, 300)  # 设置初始窗口大小
         

        # Loop through the video frames
        while cap.isOpened():
    # Read a frame from the video
            success, frame = cap.read()

            if success:
        # Run YOLOv8 inference on the frame
                results = self.model(frame)

        # Visualize the results on the frame
                annotated_frame = results[0].plot()

        # Display the annotated frame
                cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
        # Break the loop if the end of the video is reached
                break

# Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()
        

if __name__ == "__main__":
    
    root  = tk.Tk()
    root.geometry("600x600+200+200")
    root.title('食品行业工作人员卫生监测系统')

    app = Application(master = root)
    root.mainloop()