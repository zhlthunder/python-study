#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:zhl

from flask import Flask
app = Flask(__name__)
from . import account
from . import order
from . import user