class EmptyLatentAutoSnap:
    """
    Empty Latent Image 用
    ・解像度プリセット選択
    ・ワンクリック縦横入れ替え
    ・Auto Snap（8 / 16 / 64倍）
    """

    PRESETS = {
        "Custom (manual)": None,
        "SD 512x512": (512, 512),
        "SD 768x768": (768, 768),
        "SDXL 1024x1024": (1024, 1024),

        #ここで解像度を登録
        "Portrait 720x1280": (720, 1280),
        "Portrait 768x1344": (768, 1344),
        "Portrait 896x1344": (896, 1344),
        "Portrait 1008x1344": (1008, 1344),
        "Portrait 1152x1296": (1152, 1296),
        "Mobile 720x1600": (720, 1600),
    }

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": (list(cls.PRESETS.keys()),),
                "swap_wh": ("BOOLEAN", {"default": False}),
                "snap_base": ([8, 16, 32, 64], {"default": 8}),
                "custom_width": ("INT", {"default": 1024, "min": 64, "step": 8}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "step": 8}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "resolve"
    CATEGORY = "image/resize"

    def resolve(
        self,
        preset,
        swap_wh,
        snap_base,
        custom_width,
        custom_height,
    ):
        # --- 解像度決定 ---
        if self.PRESETS[preset] is None:
            width, height = custom_width, custom_height
        else:
            width, height = self.PRESETS[preset]

        # --- 縦横入れ替え（ワンクリック） ---
        if swap_wh:
            width, height = height, width

        # --- Auto Snap ---
        def snap(v, base):
            return (v // base) * base

        width = snap(width, snap_base)
        height = snap(height, snap_base)

        return (width, height)


NODE_CLASS_MAPPINGS = {
    "EmptyLatentAutoSnap": EmptyLatentAutoSnap,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EmptyLatentAutoSnap": "Empty Latent Auto Snap",
}
