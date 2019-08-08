from PIL import Image
from fastai.core import *
from fastai.vision import *

from .filters import IFilter, MasterFilter, ColorizerFilter
from .generators import gen_inference_deep, gen_inference_wide


class ModelImageVisualizer():
    def __init__(self, filter:IFilter, results_dir:str=None):
        self.filter = filter

    def _clean_mem(self):
        torch.cuda.empty_cache()
        #gc.collect()


    def get_transformed_image(self, image:Image, render_factor:int=None)->Image:
        self._clean_mem()
        filtered_image = self.filter.filter(image, image, render_factor=render_factor)
        return filtered_image


def get_image_colorizer(render_factor:int=35, artistic:bool=True)->ModelImageVisualizer:
    if artistic:
        return get_artistic_image_colorizer(render_factor=render_factor)
    else:
        return get_stable_image_colorizer(render_factor=render_factor)

def get_stable_image_colorizer(root_folder:Path=Path('./'), weights_name:str='ColorizeStable_gen', 
        results_dir='result_images', render_factor:int=35)->ModelImageVisualizer:
    learn = gen_inference_wide(root_folder=root_folder, weights_name=weights_name)
    filtr = MasterFilter([ColorizerFilter(learn=learn)], render_factor=render_factor)
    vis = ModelImageVisualizer(filtr, results_dir=results_dir)
    return vis

def get_artistic_image_colorizer(root_folder:Path=Path('./'), weights_name:str='ColorizeArtistic_gen', 
        results_dir='result_images', render_factor:int=35)->ModelImageVisualizer:
    learn = gen_inference_deep(root_folder=root_folder, weights_name=weights_name)
    filtr = MasterFilter([ColorizerFilter(learn=learn)], render_factor=render_factor)
    vis = ModelImageVisualizer(filtr, results_dir=results_dir)
    return vis

