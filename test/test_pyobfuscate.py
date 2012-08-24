#!/usr/bin/env python

import unittest
import sys
sys.path = ["/opt/thinlinc/modules"] + sys.path
import subprocess
import re
import os
import tempfile

class ObfuscateTest(unittest.TestCase):
    def mkstemp(self):
        """wrapper for mkstemp, calling mktemp if mkstemp is not available"""
        if hasattr(tempfile, "mkstemp"):
            return tempfile.mkstemp()
        else:
            fname = tempfile.mktemp()
            return os.open(fname, os.O_RDWR|os.O_CREAT), fname

    def run_pyobfuscate(self, testfile, args=[]):
        cmdline = ["../pyobfuscate"] + args + [testfile]
        p = subprocess.Popen(cmdline,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        (stdout, stderr) = p.communicate()
        assert '' == stderr, "pyobfuscate wrote to stderr: %s" % stderr
        return stdout

    def obfuscate_and_write(self, testfile, outfile, args=[]):
        open(outfile, 'w').write(self.run_pyobfuscate(testfile, args))

    def run_src(self, src):
        f, fname = self.mkstemp()
        os.write(f, src)
        os.close(f)
        retcode = subprocess.call([sys.executable, fname])
        os.remove(fname)
        return retcode

    def obfuscate_and_run_file(self, testfile, args=[]):
        output = self.run_pyobfuscate(testfile, args)
        return self.run_src(output)

    def obfuscate_and_run_src(self, src, args=[]):
        f, fname = self.mkstemp()
        os.write(f, src)
        os.close(f)
        retcode = self.obfuscate_and_run_file(fname, args)
        os.remove(fname)
        return retcode
    
    def test_DontKeepblanks(self):
        """Don't keep blanks unless told so"""
        output = self.run_pyobfuscate("testfiles/commblanks.py")
        assert None == re.search(output, "^$"), "Blank lines in output"
        lines = output.split("\n")
        assert "#" == lines[0][0], "First line is not a comment"
        assert 42 == self.run_src(output)        

    def test_Keepblanks(self):
        """Keep blanks when told so"""
        output = self.run_pyobfuscate("testfiles/commblanks.py",
                                      args=["--keepblanks"])
        lines = output.split("\n")
        assert '' == lines[5], "Blank lines removed"
        assert 42 == self.run_src(output)

    def test_lambdaGlobal(self):
        """Support lambda constructs referencing global functions.
        Test inspired by log message for revision 1.15"""
        assert 42 == self.obfuscate_and_run_file("testfiles/lambda_global.py"), "Incorrect value returned after obfuscation"

    def test_power(self):
        """Handle power operator correctly. Bug 1411"""
        assert 4 == self.obfuscate_and_run_file("testfiles/power.py"), "Incorrect value returned after obfuscation"

    def test_keywordfunc(self):
        """Handle keyword functions correctly.
        Test inspired by revision 1.8 and revision 1.9"""
        assert 42 == self.obfuscate_and_run_file("testfiles/keywordfunc.py"), "Incorrect value returned after obfuscation"

    def test_importlist(self):
        """Handle from <x> import <y>"""
        self.obfuscate_and_write("testfiles/tobeimported.py",
                                 "generated/tobeimported.py")
        self.obfuscate_and_write("testfiles/import.py",
                                 "generated/import.py")
        assert 42 == subprocess.call([sys.executable, "generated/import.py"]), "Incorrect value returned after obfuscation"

    def test_import_package(self):
        """Handle from x.y import z"""
        self.obfuscate_and_write("testfiles/package/tobeimported.py",
                                 "generated/package/tobeimported.py")
        self.obfuscate_and_write("testfiles/package/__init__.py",
                                 "generated/package/__init__.py")

        self.obfuscate_and_write("testfiles/importpackage.py",
                                 "generated/importpackage.py")
        assert 42 == subprocess.call([sys.executable,
                                      "generated/importpackage.py"],
                                     env={"PYTHONPATH":"generated"}), "Incorrect value returned after obfuscation"

    def test_import_package_as(self):
        """Handle from x.y import z as a"""
        self.obfuscate_and_write("testfiles/package/tobeimported.py",
                                 "generated/package/tobeimported.py")
        self.obfuscate_and_write("testfiles/package/__init__.py",
                                 "generated/package/__init__.py")

        self.obfuscate_and_write("testfiles/importpackage_as.py",
                                 "generated/importpackage_as.py")
        assert 42 == subprocess.call([sys.executable,
                                      "generated/importpackage_as.py"],
                                     env={"PYTHONPATH":"generated"}), "Incorrect value returned after obfuscation"

    def test_import_everything(self):
        self.obfuscate_and_write("testfiles/tobeimported_everything.py",
                                 "generated/tobeimported_everything.py")
        self.obfuscate_and_write("testfiles/importall_star.py",
                                 "generated/importall_star.py")
        assert 42 == subprocess.call([sys.executable, "generated/importall_star.py"]), "Incorrect value returned after obfuscation"

    def test_import_dyn_all(self):
        """Verify that trying to import from a file with dynamic __all__ fails"""
        cmdline = ["../pyobfuscate", "testfiles/dyn_all.py"]        
        p = subprocess.Popen(cmdline,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        (stdout, stderr) = p.communicate()
        assert -1 != stderr.find("__all__ is not a list of constants"), "pyobufscate didn't bail out with an error on file with dynamic __all__"

    def test_import_with_keywords(self):
        """Verify that an imported class, defined in __all__, does not get obfuscated keyword arguments"""
        self.obfuscate_and_write("testfiles/keywordclass.py",
                                 "generated/keywordclass.py")
        self.obfuscate_and_write("testfiles/keywordclassuser.py",
                                 "generated/keywordclassuser.py")
        assert 42 == subprocess.call([sys.executable, "generated/keywordclassuser.py"]), "Incorrect value returned after obfuscation"

    def test_global_stmt(self):
        """Verify use of 'global' keyword"""
        assert 42 == self.obfuscate_and_run_file("testfiles/global.py"), "Incorrect value returned after obfuscation"

    def test_definition_after_use(self):
        """Verify that a function defined after it's used works as expected"""
        output = self.run_pyobfuscate("testfiles/defafteruse.py")
        assert 42 == self.run_src(output), "Incorrect value returned after obfuscation"

    def test_bug1583(self):
        """Verify that bug 1583 is not present (lambda obfuscation problems)"""
        output = self.run_pyobfuscate("testfiles/bug1583.py")
        assert 42 == self.run_src(output), "Incorrect value returned after obfuscation"

    def test_bug1673(self):
        """Verify that bug 1673 is not present (global variable handling)"""
        output = self.run_pyobfuscate("testfiles/bug1673.py")
        assert 49 == self.run_src(output), "Incorrect value returned after obfuscation"

                                 

    
if "__main__" == __name__:
    unittest.main()
