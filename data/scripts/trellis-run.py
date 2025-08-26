import os
import sys
os.environ['ATTN_BACKEND'] = 'xformers'   # Can be 'flash-attn' or 'xformers', default is 'flash-attn'
os.environ['SPCONV_ALGO'] = 'native'        # Can be 'native' or 'auto', default is 'auto'.
                                            # 'auto' is faster but will do benchmarking at the beginning.
                                            # Recommended to set to 'native' if run only once.

import numpy as np
import imageio
from PIL import Image
from trellis.pipelines import TrellisImageTo3DPipeline
from trellis.utils import render_utils, postprocessing_utils

# Load a pipeline from a model folder or a Hugging Face model hub.
pipeline = TrellisImageTo3DPipeline.from_pretrained("microsoft/TRELLIS-image-large")
pipeline.cuda()

# get folder from argument

if len(sys.argv) < 2:
    print("Usage: python trellis-run.py <image_folder>")
    sys.exit(1)

image_folder = sys.argv[1]
if not os.path.exists(image_folder):
    print(f"Image folder {image_folder} does not exist.")
    sys.exit(1)

# list and load all images in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
if len(image_files) == 0:
    print(f"No images found in folder {image_folder}.")
    sys.exit(1)

# sort files to ensure consistent order
image_files.sort()
images = [Image.open(os.path.join(image_folder, f)) for f in image_files]


# Run the pipeline
outputs = pipeline.run_multi_image(
    images,
    seed=1,
    # Optional parameters
    sparse_structure_sampler_params={
        "steps": 12,
        "cfg_strength": 7.5,
    },
    slat_sampler_params={
        "steps": 12,
        "cfg_strength": 3,
    },
)
# outputs is a dictionary containing generated 3D assets in different formats:
# - outputs['gaussian']: a list of 3D Gaussians
# - outputs['radiance_field']: a list of radiance fields
# - outputs['mesh']: a list of meshes

#outputs['gaussian'][0].save_ply("sample.ply")

# make glb
glb = postprocessing_utils.to_glb(
    outputs['gaussian'][0],
    outputs['mesh'][0],
    # Optional parameters
    simplify=0.95,          # Ratio of triangles to remove in the simplification process
    texture_size=1024,      # Size of the texture used for the GLB
)
glb.export("sample1.glb")
exit(0)