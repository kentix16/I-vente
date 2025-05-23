from kivy.core.text import LabelBase
from kivy.metrics import sp

def register_fonts(theme_cls):
    LabelBase.register(name="OutfitSemiBold", fn_regular="font/Outfit-SemiBold.ttf")
    LabelBase.register(name="OutfitBlack", fn_regular="font/Outfit-Black.ttf")
    LabelBase.register(name="OutfitMedium", fn_regular="font/Outfit-Medium.ttf")
    LabelBase.register(name="OutfitRegular", fn_regular="font/Outfit-Regular.ttf")

    theme_cls.font_styles["OutfitSemiBold"] = {
        "small": {
            "font-name": "OutfitSemiBold",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "OutfitSemiBold",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "OutfitSemiBold",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }

    theme_cls.font_styles["OutfitBlack"] = {
        "small": {
            "font-name": "OutfitBlack",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "OutfitBlack",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "OutfitBlack",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }
    theme_cls.font_styles["OutfitMedium"] = {
        "small": {
            "font-name": "OutfitMedium",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "OutfitMedium",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "OutfitMedium",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }
    theme_cls.font_styles["OutfitRegular"] = {
        "small": {
            "font-name": "OutfitRegular",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "OutfitRegular",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "OutfitRegular",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }
