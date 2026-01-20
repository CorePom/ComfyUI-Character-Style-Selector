import torch
import torch.nn.functional as F

class ScaleBySelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "scale_mode": (
                    ["1.25x (5/16)", "1.5x (3/8)"],
                    {"default": "1.25x (5/16)"}
                ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "scale"
    CATEGORY = "image/resize"

    def scale(self, image, scale_mode):
        b, h, w, c = image.shape

        if scale_mode == "1.25x (5/16)":
            num, den = 5, 16
        elif scale_mode == "1.5x (3/8)":
            num, den = 3, 8
        else:
            num, den = 5, 16  # 保険

        new_w = (w * num) // den
        new_h = (h * num) // den

        img = image.permute(0, 3, 1, 2)
        img = F.interpolate(
            img,
            size=(new_h, new_w),
            mode="bicubic",
            align_corners=False
        )
        img = img.permute(0, 2, 3, 1)

        return (img,)


NODE_CLASS_MAPPINGS = {
    "ScaleBySelector": ScaleBySelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ScaleBySelector": "Scale By Selector (1.25x / 1.5x)",
}
