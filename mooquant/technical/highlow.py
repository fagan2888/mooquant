# -*- coding: utf-8 -*-
# MooQuant
#
# Copyright 2017 bopo.wang<ibopo@126.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: bopo.wang <ibopo@126.com>
"""

from mooquant import technical


# 高低价指标
class HighLowEventWindow(technical.EventWindow):
    def __init__(self, windowSize, useMin):
        super().__init__(windowSize)
        self.__useMin = useMin

    def getValue(self):
        ret = None

        if self.windowFull():
            values = self.getValues()

            if self.__useMin:
                ret = values.min()
            else:
                ret = values.max()

        return ret


class High(technical.EventBasedFilter):
    """This filter calculates the highest value.

    :param dataSeries: The DataSeries instance being filtered.
    :type dataSeries: :class:`mooquant.dataseries.DataSeries`.
    :param period: The number of values to use to calculate the highest value.
    :type period: int.
    :param maxLen: The maximum number of values to hold.
        Once a bounded length is full, when new items are added, a corresponding number of items are discarded from the
        opposite end. If None then dataseries.DEFAULT_MAX_LEN is used.
    :type maxLen: int.
    """

    def __init__(self, dataSeries, period, maxLen=None):
        super().__init__(dataSeries, HighLowEventWindow(period, False), maxLen)


class Low(technical.EventBasedFilter):
    """This filter calculates the lowest value.

    :param dataSeries: The DataSeries instance being filtered.
    :type dataSeries: :class:`mooquant.dataseries.DataSeries`.
    :param period: The number of values to use to calculate the lowest value.
    :type period: int.
    :param maxLen: The maximum number of values to hold.
        Once a bounded length is full, when new items are added, a corresponding number of items are discarded from the
        opposite end. If None then dataseries.DEFAULT_MAX_LEN is used.
    :type maxLen: int.
    """

    def __init__(self, dataSeries, period, maxLen=None):
        super().__init__(dataSeries, HighLowEventWindow(period, True), maxLen)
