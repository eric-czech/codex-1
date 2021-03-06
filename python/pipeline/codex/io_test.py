import unittest
import codex
from codex import io as codex_io


class TestIo(unittest.TestCase):

    def test_raw_img_paths(self):
        codex.set_file_format_version(codex.FF_V01)

        # Test raw image path generation with default settings
        path = codex_io.get_raw_img_path(ireg=0, itile=0, icyc=0, ich=0, iz=0)
        self.assertEqual('Cyc1_reg1/1_00001_Z001_CH1.tif', path)

        # Test raw image path generation with explicit overrides on index mappings
        codex.set_raw_index_symlinks(dict(region={1: 2}, cycle={1: 5}, z={1: 3}, channel={1: 9}))
        path = codex_io.get_raw_img_path(ireg=0, itile=0, icyc=0, ich=0, iz=0)
        self.assertEqual('Cyc5_reg2/1_00001_Z003_CH9.tif', path)
        codex.set_raw_index_symlinks({})

        # Test file formats v0.2
        codex.set_file_format_version(codex.FF_V02)
        path = codex_io.get_raw_img_path(ireg=0, itile=0, icyc=0, ich=0, iz=0)
        self.assertEqual('Cyc1_reg1/C001_Z001_T001.tif', path)
