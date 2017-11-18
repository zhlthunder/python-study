#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

import pytesseract
from PIL import Image

image = Image.open('./jpg/code.png')
code = pytesseract.image_to_string(image)
print(code)


#下面的代码还有问题，待继续排查
image = Image.open('./jpg/code2.png')
code = pytesseract.image_to_string(image)
print(code)
