import qsort
# unit testfor rich lambda
import unittest

class  QsortTest(unittest.TestCase):
    def test_sort(self):
        data = [3,2,0,1,27,10]
        result = qsort.qsort(data)
        expected = [0,1,2,3,10,27]
        self.assertEqual(expected,result)