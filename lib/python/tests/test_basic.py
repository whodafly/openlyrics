# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=80 tabstop=4 softtabstop=4
#
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


'''Unit test example using unittest module.'''

import unittest
import openlyrics

from tests import paths


class WeirdTestCase(unittest.TestCase):

    def test_notexist_file(self):
        fname = 'not existing file.xml'
        self.assertRaises(IOError, openlyrics.Song, fname)

    def test_invalid_xml(self):
        fname = paths.invalid_song
        print fname
        self.assertRaises(SyntaxError, openlyrics.Song, fname)
     

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(WeirdTestCase, 'test'))

    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')

