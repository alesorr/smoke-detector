import unittest
import unittest.runner
import itertools
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/alex/Desktop/smoke-detector/source')
import detector    

''' 
    UTILS --> This Classes need to show progress bar while testing
'''
class CustomTextTestResult(unittest.runner.TextTestResult):
    """Extension of TextTestResult to support numbering test cases"""

    def __init__(self, stream, descriptions, verbosity):
        """Initializes the test number generator, then calls super impl"""

        self.test_numbers = itertools.count(1)

        return super(CustomTextTestResult, self).__init__(stream, descriptions, verbosity)

    def startTest(self, test):
        """Writes the test number to the stream if showAll is set, then calls super impl"""

        if self.showAll:
            progress = '[{0}/{1}] '.format(next(self.test_numbers), self.test_case_count)
            self.stream.write(progress)

            # Also store the progress in the test itself, so that if it errors,
            # it can be written to the exception information by our overridden
            # _exec_info_to_string method:
            test.progress_index = progress

        return super(CustomTextTestResult, self).startTest(test)

    def _exc_info_to_string(self, err, test):
        """Gets an exception info string from super, and prepends 'Test Number' line"""

        info = super(CustomTextTestResult, self)._exc_info_to_string(err, test)

        if self.showAll:
            info = 'Test number: {index}\n{info}'.format(
                index=test.progress_index,
                info=info
            )

        return info
class CustomTextTestRunner(unittest.runner.TextTestRunner):
    """Extension of TextTestRunner to support numbering test cases"""

    resultclass = CustomTextTestResult

    def run(self, test):
        """Stores the total count of test cases, then calls super impl"""

        self.test_case_count = test.countTestCases()
        return super(CustomTextTestRunner, self).run(test)

    def _makeResult(self):
        """Creates and returns a result instance that knows the count of test cases"""

        result = super(CustomTextTestRunner, self)._makeResult()
        result.test_case_count = self.test_case_count
        return result


class Testing(unittest.TestCase):

    def setUp(self):
        """
        Here will be initialized all the values to be tested.
        """
        self.text = "INFO >> Start..."
        self.a = "some"
        self.b = "some"

    def test_string(self):
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        try:
            self.assertEqual(self.a, self.b)
        except:
            raise Exception()

    def test_default_text(self):
        """
        Any method which starts with ``test_`` will considered as a test case.
        """
        try:
            self.assertEqual(self.text, detector.main())
        except:  
            raise Exception()
                        



'''
===================================================================================================
MAIN CODE
===================================================================================================
'''

def get_tests():
    """
    This function return a list of all the use case method's names 
    """
    test_funcs = ['test_string', 'test_default_text']
    return [Testing(func) for func in test_funcs]

if __name__ == '__main__':
    test_suite = unittest.TestSuite()

    repetitions = 3                                         # ogni test lo eseguo 3 volte
    tests = get_tests()
    for __ in range(0, repetitions):
        test_suite.addTests(tests)

    CustomTextTestRunner(verbosity=2).run(test_suite)