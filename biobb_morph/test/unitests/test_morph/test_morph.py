# type: ignore
from biobb_common.tools import test_fixtures as fx

from biobb_morph.morph.morph import morph


class TestMorph:
    def setup_class(self):
        fx.test_setup(self, "morph")

    def teardown_class(self):
        # fx.test_teardown(self)
        pass

    def test_morph(self):
        morph(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths["output_morphed_zip_path"])
