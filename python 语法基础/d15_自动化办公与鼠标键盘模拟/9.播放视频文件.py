#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import numpy as np
import cv2

cap = cv2.VideoCapture(r'D:\movies\SILK-014.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()