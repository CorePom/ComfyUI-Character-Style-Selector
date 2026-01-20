from .character_style_selector import NODE_CLASS_MAPPINGS as CHAR_MAP, NODE_DISPLAY_NAME_MAPPINGS as CHAR_NAME
from .background_style_selector import NODE_CLASS_MAPPINGS as BG_MAP, NODE_DISPLAY_NAME_MAPPINGS as BG_NAME
from .expression_style_selector import NODE_CLASS_MAPPINGS as EXP_MAP, NODE_DISPLAY_NAME_MAPPINGS as EXP_NAME
from .pose_style_selector import NODE_CLASS_MAPPINGS as POSE_MAP, NODE_DISPLAY_NAME_MAPPINGS as POSE_NAME
from .outfit_style_selector import NODE_CLASS_MAPPINGS as OUTFIT_MAP, NODE_DISPLAY_NAME_MAPPINGS as OUTFIT_NAME
from .angle_style_selector import NODE_CLASS_MAPPINGS as ANGLE_MAP, NODE_DISPLAY_NAME_MAPPINGS as ANGLE_NAME

# ★ 触手セレクター（これが抜けてた）
from .tentacle_style_selector import NODE_CLASS_MAPPINGS as TENTACLE_MAP, NODE_DISPLAY_NAME_MAPPINGS as TENTACLE_NAME

# ★ 重みセレクター
from .prompt_weight_selector import NODE_CLASS_MAPPINGS as WEIGHT_MAP, NODE_DISPLAY_NAME_MAPPINGS as WEIGHT_NAME
from .style_style_selector import NODE_CLASS_MAPPINGS as STYLE_MAP, NODE_DISPLAY_NAME_MAPPINGS as STYLE_NAME

from .scale_selector import NODE_CLASS_MAPPINGS as SCALESEL_MAP, NODE_DISPLAY_NAME_MAPPINGS as SCALESEL_NAME
from .auto_snap import NODE_CLASS_MAPPINGS as SNAP_MAP, NODE_DISPLAY_NAME_MAPPINGS as SNAP_NAME
from .empty_latent_auto_snap import NODE_CLASS_MAPPINGS as EL_SNAP_MAP, NODE_DISPLAY_NAME_MAPPINGS as EL_SNAP_NAME
# ★ スロット単位プロンプト処理
from .prompt_slot_processor import NODE_CLASS_MAPPINGS as SLOT_MAP, NODE_DISPLAY_NAME_MAPPINGS as SLOT_NAME



NODE_CLASS_MAPPINGS = {
    **CHAR_MAP,
    **BG_MAP,
    **EXP_MAP,
    **POSE_MAP,
    **OUTFIT_MAP,
    **ANGLE_MAP,
    **TENTACLE_MAP,  # ← 重要
    **WEIGHT_MAP,
    **SLOT_MAP,
    **STYLE_MAP,
    **SCALESEL_MAP,
    **SNAP_MAP,
    **EL_SNAP_MAP,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **CHAR_NAME,
    **BG_NAME,
    **EXP_NAME,
    **POSE_NAME,
    **OUTFIT_NAME,
    **ANGLE_NAME,
    **TENTACLE_NAME,  # ← 重要
    **WEIGHT_NAME,
    **SLOT_NAME,
    **STYLE_NAME,
    **SCALESEL_NAME,
    **SNAP_NAME,
    **EL_SNAP_NAME,
}
