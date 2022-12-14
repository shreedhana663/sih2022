import cv2
#import cv2
import numpy as np
import argparse
import time
#from playsound import playsound
img_path="clear images/clear3.jpeg"
img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
laplacian_var = cv2.Laplacian(img, cv2.CV_64F).var()
if laplacian_var < 30:
    print("Image blurry , Please upload clear image!")
else:
    print("Not blurry")

print(laplacian_var)

# cv2.imshow("Img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

if(laplacian_var>30):




    def load_yolo():
        net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
        classes = []
        with open("coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]
        layers_names = net.getLayerNames()
        print(layers_names)
        print(net.getUnconnectedOutLayers())
        output_layers = [layers_names[i - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        return net, classes, colors, output_layers


    def load_image(img_path):
        # image loading
        img = cv2.imread(img_path)
        img = cv2.resize(img, None, fx=0.4, fy=0.4)
        height, width, channels = img.shape
        return img, height, width, channels


    def detect_objects(img, net, outputLayers):
        blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        outputs = net.forward(outputLayers)
        # print("Output : {} ".format(outputs))
        return blob, outputs


    def get_box_dimensions(outputs, height, width):
        boxes = []
        confs = []
        class_ids = []
        for output in outputs:
            for detect in output:
                scores = detect[5:]
                # print(scores)
                class_id = np.argmax(scores)
                conf = scores[class_id]
                if conf > 0.3:
                    center_x = int(detect[0] * width)
                    center_y = int(detect[1] * height)
                    w = int(detect[2] * width)
                    h = int(detect[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confs.append(float(conf))
                    class_ids.append(class_id)
        return boxes, confs, class_ids


    # def dummy():
    #     print('playing sound using playsound')
    #     playsound(r'C:\\Users\P.Dhanashreenydhi\Downloads\buzz.mp3')
    #
    #     print('running..')


    def draw_labels(boxes, confs, colors, class_ids, classes, img):
        indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y - 5), font, 1, color, 1)
        cv2.imshow("Image", img)
        #dummy()


    def webcam_detect():
        model, classes, colors, output_layers = load_yolo()
        cap = cv2.VideoCapture(0)
        while True:
            _, frame = cap.read()
            height, width, channels = frame.shape
            blob, outputs = detect_objects(frame, model, output_layers)
            boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
            draw_labels(boxes, confs, colors, class_ids, classes, frame)
            key = cv2.waitKey(1)
            if key == 27:
                break
        cap.release()


    def start_video(video_path):
        model, classes, colors, output_layers = load_yolo()
        cap = cv2.VideoCapture(video_path)
        while True:
            _, frame = cap.read()
            height, width, channels = frame.shape
            blob, outputs = detect_objects(frame, model, output_layers)
            boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
            draw_labels(boxes, confs, colors, class_ids, classes, frame)
            key = cv2.waitKey(1)
            # print("frame : {}".format(frame))
            if key == 27:
                cv2.destroyAllWindows()
                break
        cap.release()


    def predict_this_image(src):
        model, classes, colors, output_layers = load_yolo()
        frame = cv2.imread(src)
        height, width, channels = frame.shape
        blob, outputs = detect_objects(frame, model, output_layers)
        boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
        draw_labels(boxes, confs, colors, class_ids, classes, frame)
        key = cv2.waitKey(0)


    if __name__ == "__main__":
        # start_video(r"E:\learning Python\vehicelmovement.mp4")
        #  start_video(r"E:\learning Python\video1.mp4")
        # predict_this_image(r"E:\learning Python\1.jpg")
        predict_this_image(img_path)