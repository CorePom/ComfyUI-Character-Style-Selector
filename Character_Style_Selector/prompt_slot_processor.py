class Prompt_Slot_Processor:

    # ここで除外するトークンを設定してください
    EXCLUDE_KEYWORDS = [
        # 髪
        "hair",
        "bangs",
        "sidelock",
        "twintails",
        "ponytail",
        "ahoge",

        # 目
        "eye",
        "eyes",

        # 耳
        "ear",
        "ears",

        # 胸
        "breast",
        "breasts",
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": ""}),

                "slot1_cosplay": ("BOOLEAN", {"default": False}),
                "slot1_exclude": ("BOOLEAN", {"default": False}),

                "slot2_cosplay": ("BOOLEAN", {"default": False}),
                "slot2_exclude": ("BOOLEAN", {"default": False}),

                "slot3_cosplay": ("BOOLEAN", {"default": False}),
                "slot3_exclude": ("BOOLEAN", {"default": False}),

                "slot4_cosplay": ("BOOLEAN", {"default": False}),
                "slot4_exclude": ("BOOLEAN", {"default": False}),

                "slot5_cosplay": ("BOOLEAN", {"default": False}),
                "slot5_exclude": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("processed_prompt",)
    FUNCTION = "run"
    CATEGORY = "Text/Utility"

    def run(
        self,
        prompt,
        slot1_cosplay, slot1_exclude,
        slot2_cosplay, slot2_exclude,
        slot3_cosplay, slot3_exclude,
        slot4_cosplay, slot4_exclude,
        slot5_cosplay, slot5_exclude,
    ):

        if not prompt.strip():
            return ("",)

        slots = [p for p in prompt.split(", ") if p.strip()]
        settings = [
            (slot1_cosplay, slot1_exclude),
            (slot2_cosplay, slot2_exclude),
            (slot3_cosplay, slot3_exclude),
            (slot4_cosplay, slot4_exclude),
            (slot5_cosplay, slot5_exclude),
        ]

        result = []

        for i, part in enumerate(slots):
            tokens = part.split(",")
            cosplay, exclude = settings[i] if i < len(settings) else (False, False)

            kept = []
            for t in tokens:
                token = t.strip()
                if exclude and any(k in token for k in self.EXCLUDE_KEYWORDS):
                    continue
                kept.append(token)

            if not kept:
                continue

            if cosplay:
                kept[0] = kept[0] + " cosplay"

            result.append(",".join(kept))

        return (", ".join(result),)


NODE_CLASS_MAPPINGS = {
    "Prompt Slot Processor": Prompt_Slot_Processor
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Prompt Slot Processor": "Prompt Slot Processor"
}
