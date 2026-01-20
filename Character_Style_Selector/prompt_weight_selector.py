class Prompt_Weight_5_Selector:

    @classmethod
    def INPUT_TYPES(cls):
        # none + 0.1 ～ 2.0（0.1刻み）
        weights = ["none"] + [f"{i/10:.1f}" for i in range(1, 21)]

        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": ""}),
                "weight1": (weights,),
                "weight2": (weights,),
                "weight3": (weights,),
                "weight4": (weights,),
                "weight5": (weights,),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weighted_prompt",)
    FUNCTION = "run"
    CATEGORY = "Text/Utility"

    def run(self, prompt, weight1, weight2, weight3, weight4, weight5):
        if not prompt.strip():
            return ("",)

        # Style Selectorの出力は ", "（カンマ＋スペース）で結合されているので、それで分割
        parts = [p.strip() for p in prompt.split(", ") if p.strip()]

        weights = [weight1, weight2, weight3, weight4, weight5]

        result = []

        for i, part in enumerate(parts):
            if i >= 5:
                # 6個目以降はそのまま追加
                result.append(part)
                continue

            w = weights[i]

            # none または 1.0 の場合は素通し（重み付けなし）
            if w == "none" or w == "1.0":
                result.append(part)
            else:
                try:
                    w_float = float(w)
                    # 1項目全体を括弧で囲って重み付け → これが肝！
                    result.append(f"({part}:{w_float:.1f})")
                except ValueError:
                    result.append(part)

        return (", ".join(result),)


# --------------------------------------------------------------
# 登録（表示名はシンプルに）
# --------------------------------------------------------------
NODE_CLASS_MAPPINGS = {
    "Prompt Weight Selector": Prompt_Weight_5_Selector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Prompt Weight Selector": "Prompt Weight Selector"
}