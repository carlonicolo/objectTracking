import cv2
import sys
from random import randint

# Tracking algorithms
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
tracker_type = tracker_types[6]
print(tracker_type)

<<<<<<< HEAD
=======
'''
for i in range(len(tracker_types)):
    print(tracker_types[i])
    if tracker_type == 'BOOSTING':
        tracker = cv2.legacy.TrackerBoosting_create()
    elif tracker_type == 'MIL':
        tracker = cv2.legacy.TrackerMIL_create()
    elif tracker_type == 'KCF':
        tracker = cv2.legacy.TrackerKCF_create()
    elif tracker_type == 'TLD':
        tracker = cv2.legacy.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
        tracker = cv2.legacy.TrackerMedianFlow_create()
    elif tracker_type == 'MOSSE':
        tracker = cv2.legacy.TrackerMOSSE_create()
    elif tracker_type == 'CSRT':
        tracker = cv2.legacy.TrackerCSRT_create()
    print(tracker)
'''

>>>>>>> 8aabc61f9609a25ec02a38f8ee6a6db6cfd3ae96
if tracker_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.legacy.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
elif tracker_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()
elif tracker_type == 'CSRT':
    tracker = cv2.legacy.TrackerCSRT_create()

#print(tracker)

# First step -> load the video
video = cv2.VideoCapture('Videos/race.mp4')
if not video.isOpened():
    print("Error loading the video")
    sys.exit()

# Second step -> analalize a frame for selecting the object to track
# ok -> if we could load the first frame of the video
# frame -> start the first frame of the video
ok, frame = video.read()
if not ok:
    print("Error while loading the frame")
    sys.exit()
#print(ok)

# create the bounding box for tracking the object
bbox = cv2.selectROI(frame) # region of interest
print(bbox)

# initialize the first algorithm on the selected object
ok = tracker.init(frame, bbox)
print(ok)

colors = (randint(0, 255), randint(0, 255), randint(0, 255)) # RGB -> BGR
print(colors)

while True:
    ok, frame = video.read()
    #print(ok)
    if not ok:
        break

    # update the frame and catch the new coordinate of the
    # tracked object while is moving
    ok, bbox = tracker.update(frame)
    print(ok, bbox)
    if ok == True:
        (x, y, w, h) = [int(v) for v in bbox]
        #print(x, y, w, h)
        cv2.rectangle(frame, (x,y), (x+w, y+h), colors, 2, 1)
    else:
        cv2.putText(frame, 'Tracking failure !', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255), 2)

    cv2.putText(frame, tracker_type, (100, 20), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(1) & 0xFF == 27: #esc
        break
