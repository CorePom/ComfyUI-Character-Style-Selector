# --------------------------------------------------------------
#  Outfit Style Selector (5 Select Version)
#  CSV: name,prompt,negative_prompt
#  衣装スタイルを 5 個同時選択して合成出力
# --------------------------------------------------------------

import os
import csv

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}


class Outfit_Style_Selector:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH = os.path.join(BASE_DIR, "outfits.csv")

    # CSV 絶対パスを使用時（ここのbackground.csvのパスを変更して各自のパスを指定し、上二行をコメントアウト）
    #CSV_PATH = r"C:\ComfyUI\custom_nodes\Character_Style_Selector\outfits.csv"

    cached_csv = {}
    cached_mtime = 0

    # ----------------------------------------------------------
    # CSV 読み込み
    # ----------------------------------------------------------
    @classmethod
    def load_csv(cls):
        path = cls.CSV_PATH
        if not os.path.exists(path):
            print("[Outfit] CSV not found:", path)
            cls.cached_csv = {}
            return {}

        mtime = os.path.getmtime(path)

        if cls.cached_mtime == mtime and cls.cached_csv:
            return cls.cached_csv

        data = {}

        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    name = row.get("name", "").strip()
                    prompt = row.get("prompt", "").strip()
                    negative = row.get("negative_prompt", "").strip()
                    if name:
                        data[name] = {"prompt": prompt, "negative": negative}
        except Exception as e:
            print("[Outfit] CSV load error:", e)
            data = {}

        cls.cached_csv = data
        cls.cached_mtime = mtime
        return data

    # ----------------------------------------------------------
    # UI：5つの衣装選択プルダウン
    # ----------------------------------------------------------
    @classmethod
    def INPUT_TYPES(cls):
        data = cls.load_csv()
        names = list(data.keys()) if data else ["(no data)"]

        return {
            "required": {
                "outfit1": (names,),
                "outfit2": (names,),
                "outfit3": (names,),
                "outfit4": (names,),
                "outfit5": (names,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "run"
    CATEGORY = "Text/Outfit"

    # ----------------------------------------------------------
    # 実行：選択された衣装の prompt / negative を結合
    # ----------------------------------------------------------
    def run(self, outfit1, outfit2, outfit3, outfit4, outfit5):

        data = self.load_csv()
        selected = [outfit1, outfit2, outfit3, outfit4, outfit5]

        pos_list = []
        neg_list = []

        for name in selected:
            if name in data:
                pos_list.append(data[name]["prompt"])
                neg_list.append(data[name]["negative"])

        positive = ", ".join([p for p in pos_list if p])
        negative = ", ".join([n for n in neg_list if n])

        return (positive, negative)


# --------------------------------------------------------------
# 登録
# --------------------------------------------------------------

NODE_CLASS_MAPPINGS["Outfit Style Selector"] = Outfit_Style_Selector
NODE_DISPLAY_NAME_MAPPINGS["Outfit Style Selector"] = "Outfit Style Selector"
