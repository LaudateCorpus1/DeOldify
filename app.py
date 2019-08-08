import io
import os

import ai_integration
import torch
from PIL import Image

from fasterai.visualize import get_image_colorizer

torch.backends.cudnn.benchmark = True

image_colorizer = get_image_colorizer(artistic=True)

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

while True:
    with ai_integration.get_next_input(inputs_schema={
        "image": {
            "type": "image"
        },
        "render_factor": {
            "type": "text"
        }
    }) as inputs_dict:
        image = Image.open(io.BytesIO(inputs_dict['image']))

        image = image.convert('RGB')

        render_factor = 35
        if inputs_dict.get('render_factor') and inputs_dict['render_factor'] != '':
            render_factor = int(inputs_dict['render_factor'])

        result_image = image_colorizer.get_transformed_image(image, render_factor=render_factor)

        imgByteArr = io.BytesIO()
        result_image.save(imgByteArr, format='JPEG', subsampling=0, quality=98)
        imgByteArr = imgByteArr.getvalue()

        result = {
            'content-type': 'image/jpeg',
            'data': imgByteArr,
            'success': True,
            'error': None
        }
        ai_integration.send_result(result)
