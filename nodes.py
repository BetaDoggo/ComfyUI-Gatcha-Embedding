import random

class GatchaEmbedding:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 1337, "min": 1, "max": 16777215}),
            },
            "optional": {
                "clip1": ("CLIP",),
                "clip2": ("CLIP",),
                "clip3": ("CLIP",),
                "clip4": ("CLIP",),
                "clip5": ("CLIP",),
                "clip6": ("CLIP",),
                "clip7": ("CLIP",),
                "clip8": ("CLIP",),
                "clip9": ("CLIP",),
                "clip10": ("CLIP",),
            },
        }
    
    RETURN_TYPES = ("CLIP",)
    FUNCTION = "roll_gatcha"
    CATEGORY = "ComfyCloudAPIs"

    def roll_gatcha(self, seed, clip1=None, clip2=None, clip3=None, clip4=None, clip5=None, clip6=None, clip7=None, clip8=None, clip9=None, clip10=None,):
        clips = [clip for clip in [clip1, clip2, clip3, clip4, clip5, clip6, clip7, clip8, clip9, clip10] if clip is not None]
        random.seed(seed)
        clip = random.choice(clips)
        return (clip,)

NODE_CLASS_MAPPINGS = {
    "GatchaEmbedding": GatchaEmbedding,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GatchaEmbedding": "GatchaEmbedding",
}