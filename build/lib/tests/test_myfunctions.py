
# import yaml
# import config.yaml
#
#
# file_name = 'config.yaml'
#
# with open('config.yaml') as infile:
#     data = yaml.load(infile)
#
# person = data['Person']
# person['name'] = input('What is your name? ')
# person['age'] = int(input('What is your age? '))
# person['nationality'] = input('What is your nationality? ')
# person['footed'] = input('What foot? ')
# person['position'] = input('What is your position? ')
#
# with open('config.yaml', 'w') as outfile:
#     yaml.dump(data, stream=outfile, default_flow_style=False, indent=3)


import unittest
import os
from assign_lib.MYPYTHONLIBRARY.sacumen_lib import convert_to_json, get_dict

class TestMyfun(unittest.TestCase):

    def test_convert_to_json(self):
        convert_to_json(r'D:\assign_lab\lanenv\Akshay_Hiwarkar\assign_lib\MYPYTHONLIBRARY\tests\config.ini',
                              r'D:\assign_lab\lanenv\Akshay_Hiwarkar\assign_lib\MYPYTHONLIBRARY\sample1.json')

        is_file_present = os.path.exists(r'D:\assign_lab\lanenv\Akshay_Hiwarkar\assign_lib\MYPYTHONLIBRARY\sample1.json')
        self.assertEqual(is_file_present, True)

    def test_get_dict(self):
        d = get_dict(r'D:\assign_lab\lanenv\Akshay_Hiwarkar\assign_lib\MYPYTHONLIBRARY\tests\fig.ini')
        is_dict = isinstance(d, dict)
        self.assertEqual(is_dict, True)


if __name__ == '__main__':
    unittest.main()