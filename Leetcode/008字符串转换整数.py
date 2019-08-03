#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if re.match('^[\+\-]?\d+', str.lstrip()):
            value = int(re.match('^[\+\-]?\d+', str.lstrip()).group())
        else:
            return 0
        if value > (1<<31)-1:
            return (1<<31)-1
        elif value < -1<<31:
            return -1<<31
        else:
            return value