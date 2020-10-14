# # import unittest
# #
# # l = [["foo", "a", "a",], ["bar", "a", "a"], ["lee", "b", "b"]]
# #
# # class TestSequenceMeta(type):
# #     def __new__(mcs, name, bases, dict):
# #
# #         def gen_test(a, b):
# #             def test(self):
# #                 self.assertEqual(a, b)
# #             return test
# #
# #         for tname, a, b in l:
# #             test_name = "test_%s" % tname
# #             print(tname, a, b)
# #             dict[test_name] = gen_test(a,b)
# #         return type.__new__(mcs, name, bases, dict)
# #
# # class TestSequence(unittest.TestCase):
# #     __metaclass__ = TestSequenceMeta
# #
# # if __name__ == '__main__':
# #     unittest.main()
#
# import unittest
# class ParametrizedTestCase(unittest.TestCase):
#     """ TestCase classes that want to be parametrized should
#         inherit from this class.
#     """
#     def __init__(self, methodName='runTest', param=None):
#         super(ParametrizedTestCase, self).__init__(methodName)
#         self.param = param
#     @staticmethod
#     def parametrize(testcase_klass, param=None):
#         """ Create a suite containing all tests taken from the given
#             subclass, passing them the parameter 'param'.
#         """
#         testloader = unittest.TestLoader()
#         testnames = testloader.getTestCaseNames(testcase_klass)
#         suite = unittest.TestSuite()
#         for name in testnames:
#             suite.addTest(testcase_klass(name, param=param))
#         return suite
#
#
# #####################################################
# ##用法-testcase
# class TestOne(ParametrizedTestCase):
#     def test_something(self):
#         print ('param =', self.param)
#         self.assertEqual(1, 1)
#
#     def test_something_else(self):
#         self.assertEqual(2, 2)
#
# ##用法-测试
# suite = unittest.TestSuite()
# suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=42))
# suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=13))


# def foo(arg):
#
#     arg = 2
#
#     print(arg)
#
#
#
# a = 1
#
# foo(a)  # 输出：2
#
# print(a) # 输出：1
def bad_append(new_item, a_list=None):
    if a_list is None:
        a_list = []
    a_list.append(new_item)

    return a_list
print(bad_append('two'))
def good_append(new_item, a_list=None):

    if a_list is None:

        a_list = []

    a_list.append(new_item)

    return a_list

print(good_append('one'))
