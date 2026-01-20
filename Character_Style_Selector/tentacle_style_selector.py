# --------------------------------------------------------------
#  Tentacle Style Selector (5 Select Version)
#  CSV: name,prompt,negative_prompt
#  触手・拘束・絡み表現を 5 個同時選択して合成出力
# --------------------------------------------------------------

import os
import csv

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}


class Tentacle_Style_Selector:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH = os.path.join(BASE_DIR, "tentacle.csv")

    # CSV 絶対パスを使用時（ここのbackground.csvのパスを変更して各自のパスを指定し、上二行をコメントアウト）
    #CSV_PATH = r"C:\ComfyUI\custom_nodes\Character_Style_Selector\tentacle.csv"

    cached_csv = {}
    cached_mtime = 0

    # ----------------------------------------------------------
    # CSV 読み込み
    # ----------------------------------------------------------
    @classmethod
    def load_csv(cls):
        path = cls.CSV_PATH
        if not os.path.exists(path):
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
                        data[name] = {
                            "prompt": prompt,
                            "negative": negative
                        }
        except Exception as e:
            print(f"[Tentacle Style Selector] CSV load error: {e}")
            data = {}

        cls.cached_csv = data
        cls.cached_mtime = mtime
        return data

    # ----------------------------------------------------------
    # UI：5つの触手スタイル選択
    # ----------------------------------------------------------
    @classmethod
    def INPUT_TYPES(cls):
        data = cls.load_csv()
        names = list(data.keys()) if data else ["(no data)"]

        return {
            "required": {
                "tentacle1": (names,),
                "tentacle2": (names,),
                "tentacle3": (names,),
                "tentacle4": (names,),
                "tentacle5": (names,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "run"
    CATEGORY = "Text/Tentacle"

    # ----------------------------------------------------------
    # 実行：選択された触手表現を結合
    # ----------------------------------------------------------
    def run(self, tentacle1, tentacle2, tentacle3, tentacle4, tentacle5):

        data = self.load_csv()

        selected = [tentacle1, tentacle2, tentacle3, tentacle4, tentacle5]

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

NODE_CLASS_MAPPINGS["Tentacle Style Selector"] = Tentacle_Style_Selector
NODE_DISPLAY_NAME_MAPPINGS["Tentacle Style Selector"] = "Tentacle Style Selector"
