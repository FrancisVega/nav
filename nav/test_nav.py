import unittest
import nav

class Demo(unittest.TestCase):

    def setUp(self):
        pass

    # silly test
    def test_directoryExists(self):
        dir = "/Users/hisco"
        self.assertTrue(nav.dirExists(dir))

    def test_ItemsListHasNotEmpty(self):
        items = {
                "dir": [
                    "file",
                    "file", {
                        "dir": [
                            "file",
                            "file"
                        ]
                    }
                ]
        }
        pass



if __name__ == '__main__':
    unittest.main()
