import unittest
import tempfile
import os

import nav

class Demo(unittest.TestCase):

    def setUp(self):
        pass

    # silly test
    def test_directoryExists(self):
        with tempfile.TemporaryDirectory() as tempdir:
            self.assertTrue(nav.dirExists(tempdir))
            self.assertFalse(nav.dirExists(os.path.join(tempdir, "foo")))

    def test_createDirectoryReturnTrueIfSuccess(self):
        with tempfile.TemporaryDirectory() as tempdir:
            self.assertTrue(nav.createDirectory(os.path.join(tempdir, 'foo')))

    def test_ItemsListHasNotEmpty(self):
        tempdir = tempfile.TemporaryDirectory()

        d2 = os.path.join(tempdir.name, "foo)")
        os.mkdir(d2)


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

        print (tempdir.name)



if __name__ == '__main__':
    unittest.main()
