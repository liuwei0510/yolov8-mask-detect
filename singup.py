import cv2
import dlib
import numpy as np
from sklearn.neighbors import NearestNeighbors
import time
from sklearn.metrics.pairwise import cosine_distances

import os
import glob


def goin():
        # 加载人脸检测器和人脸特征提取器（这里使用dlib的预训练模型）
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


    # 加载已知人脸数据库
    # 指定文件夹路径
    folder_path = 'images'

    # 获取文件夹中的所有图片文件
    image_files = glob.glob(os.path.join(folder_path, '*.jpg')) + glob.glob(os.path.join(folder_path, '*.png'))

    # 生成字典
    database = {}
    for file_path in image_files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        database[file_name] = file_path

    # 打印生成的字典
    print(database)


    face_descriptors = []
    names = []

    # 提取数据库中已知人脸的特征
    for name, image_path in database.items():
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # 检测人脸
        faces = detector(gray)

        # 提取人脸特征
        for face in faces:
            landmarks = predictor(gray, face)
            face_descriptor = np.array([landmarks.part(i).x for i in range(68)] +
                                    [landmarks.part(i).y for i in range(68)])
            face_descriptors.append(face_descriptor)
            names.append(name)

    # 初始化最近邻算法
    knn = NearestNeighbors(n_neighbors=1)
    knn.fit(face_descriptors)

    '''-----------------------------人脸识别-----------------------------'''
    #打开摄像头
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)  # 创建可调整大小的窗口
    cv2.resizeWindow("YOLOv8 Inference", 300, 300)  # 设置初始窗口大小

    while cap.isOpened():

        success, frame = cap.read()
        if success:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 检测人脸
            faces = detector(gray)
            # 标记是否找到匹配的人脸
            match_found = False
            distance = 0
            # 匹配待识别人脸
            for face in faces:
                landmarks = predictor(gray, face)
                face_descriptor = np.array([landmarks.part(i).x for i in range(68)] +
                                        [landmarks.part(i).y for i in range(68)])

                # 使用最近邻算法进行匹配
                turble = knn.kneighbors(face_descriptor.reshape(1, -1),n_neighbors=1,return_distance=True)
                print(turble)
                pred_name = names[turble[1][0][0]]
                #获取distance
                distance = turble[0][0][0]
                print(distance)
                print(pred_name)
                
                # 判断匹配是否成功
                if distance < 1000:
                    match_found = True
                    print("配到人脸")
                    
                    cv2.putText(frame, pred_name+" come in", (face.left(), face.top() - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    
                    opendoor()

                # 如果没有找到匹配的人脸，给予提示信息
                if not match_found:
                    print("未配到人脸")
                    
                    cv2.putText(frame, "Permission denied !", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                    
                    # 显示结果

                cv2.imshow("result", frame)    
                continue
            
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    #关闭摄像头
    cap.release()
    cv2.destroyAllWindows()

def opendoor():
    #模拟真实门禁
    print("开门")
