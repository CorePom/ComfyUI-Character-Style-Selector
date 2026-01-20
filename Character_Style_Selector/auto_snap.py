import torch
import numpy as np

class AutoSnapToMultiple:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "multiple": ([8, 16, 32], {"default": 16}),
                "mode": (["nearest", "down", "up"], {"default": "down"}),
                "method": (["crop", "pad"], {"default": "crop"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process"
    CATEGORY = "image/resize"

    def snap(self, value, base, mode):
        if mode == "down":
            return (value // base) * base
        elif mode == "up":
            return ((value + base - 1) // base) * base
        else:  # nearest
            down = (value // base) * base
            up = ((value + base - 1) // base) * base
            return down if abs(value - down) <= abs(value - up) else up

    def process(self, image, multiple, mode, method):
        b, h, w, c = image.shape

        target_w = self.snap(w, multiple, mode)
        target_h = self.snap(h, multiple, mode)

        dw = target_w - w
        dh = target_h - h

        # Crop
        if method == "crop":
            x0 = max(0, -dw // 2)
            y0 = max(0, -dh // 2)
            x1 = x0 + target_w
            y1 = y0 + target_h
            image = image[:, y0:y1, x0:x1, :]

        # Pad
        else:
            pad_left   = max(0, dw // 2)
            pad_right  = max(0, dw - pad_left)
            pad_top    = max(0, dh // 2)
            pad_bottom = max(0, dh - pad_top)

            image = torch.nn.functional.pad(
                image,
                (0, 0, pad_left, pad_right, pad_top, pad_bottom),
                mode="constant",
                value=0
            )

        return (image,)


NODE_CLASS_MAPPINGS = {
    "AutoSnapToMultiple": AutoSnapToMultiple
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AutoSnapToMultiple": "Auto Snap to Multiple"
}
