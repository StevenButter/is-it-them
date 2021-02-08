import unittest
import whatsapp_reader

filename = 'dummy_whatsapp_log.txt'

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
    ('Lorem superposés valise pourparlers', 'person2')
]


class whatsapp_reader_test(unittest.TestCase):
    def test_shouldReadChat(self):
        data = whatsapp_reader.read(filename)

        self.assertListEqual(expectedData, data)


if __name__ == "__main__":
    unittest.main()
