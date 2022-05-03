import base64
import os

from PIL import Image


VALID_IMAGE_PATH = ''

OUTPUT_DIR = './output'
OUTPUT_CREATED_IMAGE = './output/created_image.png'
OUTPUT_CREATED_IMAGE_FROM_TUPLE = './output/created_image_from_tuple.png'
OUTPUT_CREATED_IMAGE_FROM_DEFAULT_PARAMS = './output/created_image_from_default_params.png'

OUTPUT_HTML = os.path.abspath('./output/handler_test.csv')
OUTPUT_HTML = os.path.abspath('./output/handler_test.html')
OUTPUT_XML = os.path.abspath('./output/handler_test.xml')
OUTPUT_JSON = os.path.abspath('./output/handler_test.json')

TEST_IMAGE = Image.open(VALID_IMAGE_PATH)

TEST_BASE64_IMAGE = base64.b64encode(TEST_IMAGE.tobytes()).decode('ascii')

HANDLER_TEST_IMAGE = [TEST_IMAGE, TEST_IMAGE]
HANDLER_TEST_BASE64_IMAGE = [TEST_BASE64_IMAGE, TEST_BASE64_IMAGE]