import cv2

# 打开视频文件
video_path = 'ac.mp4'
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 读取第一帧
ret, frame = cap.read()

# 检查是否成功读取第一帧
if ret:
    # 保存为JPG文件
    output_path = 'first_frame.jpg'
    cv2.imwrite(output_path, frame)
    print(f"第一帧已保存为 {output_path}")
else:
    print("无法读取第一帧")

# 释放视频文件
cap.release()