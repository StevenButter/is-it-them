import unittest
import whatsapp_reader


class whatsapp_reader_test(unittest.TestCase):
    def test_shouldReadChat(self):
        data = whatsapp_reader.read('dummy_whatsapp_log.txt')

        expectedData = [
            ('Lorem ipsum', 'person1'),
            ('Lorem ipsum', 'person1'),
            ('Lorem superposés valise pourparlers', 'person2'),
            ('Lorem superposés valise pourparlers', 'person2'),
            ('Lorem ipsum', 'person1'),
            ('Lorem ipsum', 'person1'),
            ('Lorem superposés valise pourparlers', 'person2'),
            ('Lorem ipsum', 'person1'),
            ('Lorem superposés valise pourparlers', 'person2'),
            ('Lorem superposés valise pourparlers', 'person2')]
        self.assertListEqual(expectedData, data)

    def test_shouldCombineMultiLineMessages(self):
        data = whatsapp_reader.read('whatsapp_log_multiline.txt')

        expectedData = [
            ('Lorem superposés valise pourparlers', 'person2'),
            ('Lorem ipsum', 'person1'),
            ('Lorem ipsum \n Lorem ipsum \n Lorem ipsum \n Lorem ipsum \n Lorem ipsum', 'person1'),
            ('Lorem ipsum', 'person1')]
        self.assertListEqual(expectedData, data)


if __name__ == "__main__":
    unittest.main()
