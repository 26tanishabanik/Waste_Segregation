import torch
import cv2
import numpy as np


def predict(image,
            yolov5_folder = 'yolov5',
            weights_dir = "weights/best.pt",
            img_size = 512,
            conf = 0.25, # NMS confidence threshold
            iou = 0.45, # NMS IoU threshold
            agnostic = False, # NMS class-agnostic
            multi_label = False, # NMS multiple labels per box
            classes = None, # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
            max_det = 50, # maximum number of detections per image
            amp = False): # Automatic Mixed Precision (AMP) inference
    
    # local repo & model
    model = torch.hub.load(yolov5_folder, 'custom', path=weights_dir, source='local')

    #  model.cuda()

    # Inference Setting
    model.conf = conf  
    model.iou = iou  
    model.agnostic = agnostic  
    model.multi_label = multi_label  
    model.classes = classes  
    model.max_det = max_det  
    model.amp = amp  
    
    preds = model(image, img_size)
    
    return preds.pandas().xyxy


def plot_image( image, df, txtbox_h = 50, txtbox_w = 200, txt_size = 1, box_color = (255, 0, 0), box_width = 2):
    # if no object is detected in image        
    if df[0].empty:
        return image
    img = np.copy(image)
    dh, dw, _ = image.shape
    for row in df:
        x1 = int(row['xmin'].tolist()[0])
        y1 = int(row['ymin'].tolist()[0])
        x2 = int(row['xmax'].tolist()[0])
        y2 = int(row['ymax'].tolist()[0])
        conf = round(row['confidence'].tolist()[0], 2)
        class_name = row['name'].tolist()[0]

        if x1 < 0:
            x1 = 0
        if x2 > dw - 1:
            x2 = dw - 1
        if y1 < 0:
            y1 = 0
        if y2 > dh - 1:
            y2 = dh - 1

        # plot bounding box
        cv2.rectangle(img, (x1, y1), (x2, y2), box_color, box_width)

        # plot rectangle for text
        img = cv2.rectangle(img, 
                            (x1, y1-txtbox_h), 
                            (x1 + txtbox_w, y1), 
                            box_color, -1)

        # put text
        img = cv2.putText(img, 
                          class_name,
                          (x1, y1 - 50),
                          cv2.FONT_HERSHEY_SIMPLEX, 
                          txt_size, 
                          (0, 0, 0), 2)
        
    return img


