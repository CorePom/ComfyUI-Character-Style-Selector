# --------------------------------------------------------------
#  Pose Style Selector (5 Select Version)
#  CSV: name,prompt,negative_prompt
#  ポーズスタイルを 5 個同時選択して合成出力
# --------------------------------------------------------------

import os
import csv

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}


class Pose_Style_Selector:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CSV_PATH = os.path.join(BASE_DIR, "pose.csv")

    # CSV 絶対パスを使用時（ここのbackground.csvのパスを変更して各自のパスを指定し、上二行をコメントアウト）
    #CSV_PATH = r"C:\ComfyUI\custom_nodes\Character_Style_Selector\pose.csv"

    cached_csv = {}
    cached_mtime = 0

    # ----------------------------------------------------------
    # CSV 読み込み
    # ----------------------------------------------------------
    @classmethod
    def load_csv(cls):
        path = cls.CSV_PATH
        if not os.path.exists(path):
            print("[Pose] CSV not found:", path)
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
            print("[Pose] CSV load error:", e)
            data = {}

        cls.cached_csv = data
        cls.cached_mtime = mtime
        return data

    # ----------------------------------------------------------
    # UI：5つのポーズ選択プルダウン
    # ----------------------------------------------------------
    @classmethod
    def INPUT_TYPES(cls):
        data = cls.load_csv()
        names = list(data.keys()) if data else ["(no data)"]

        return {
            "required": {
                "pose1": (names,),
                "pose2": (names,),
                "pose3": (names,),
                "pose4": (names,),
                "pose5": (names,),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "run"
    CATEGORY = "Text/Pose"

    # ----------------------------------------------------------
    # 実行：選択されたポーズの prompt / negative を結合
    # ----------------------------------------------------------
    def run(self, pose1, pose2, pose3, pose4, pose5):

        data = self.load_csv()
        selected = [pose1, pose2, pose3, pose4, pose5]

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

NODE_CLASS_MAPPINGS["Pose Style Selector"] = Pose_Style_Selector
NODE_DISPLAY_NAME_MAPPINGS["Pose Style Selector"] = "Pose Style Selector"
