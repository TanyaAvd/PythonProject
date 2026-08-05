import unittest
import day_2_coding as ed

test_encrypted = '070411111426152419071413'
test_decrypted = 'hello python'
type_text=170411111426152419071413


class MyTestCase(unittest.TestCase):

     def test_main(self):
         self.assertEqual(ed.decrypt(test_encrypted),test_decrypted)
         self.assertRaises(TypeError,ed.decrypt(test_encrypted),type_text)
         self.assertEqual(len(test_encrypted) % 2, 0)

     def test_decode(self):
         self.assertNotEqual(test_decrypted, '')

     def test_encode_decode(self):
         self.assertNotEqual(test_encrypted, '')

if __name__ == '__main__':
    unittest.main()
