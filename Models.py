# coding: utf-8
import json

class RspJson:
     def __init__(self, message, result, error, debug, createTime):
        self.message = message
        self.result = result
        self.error = error
        self.debug = debug
        self.createTime = createTime