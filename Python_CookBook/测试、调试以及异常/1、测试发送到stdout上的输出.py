"""
测试输出
"""
import mymodule
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domin = 'example.com'
        excepted_url = '{}://{}.{}\n'.format(protocol, host, domin)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            mymodule.urlprint(protocol, host, domin)
            self.assertEqual(fake_out.getvalue(), excepted_url)


a = TestURLPrint()
a.test_url_gets_to_stdout()
