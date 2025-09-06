from kivy.core.text import LabelBase
from kivy.metrics import sp

def register_fonts(theme_cls):
    LabelBase.register(name="OutfitSemiBold", fn_regular="font/Outfit-SemiBold.ttf")
    LabelBase.register(name="OutfitBlack", fn_regular="font/Outfit-Black.ttf")
    LabelBase.register(name="OutfitMedium", fn_regular="font/Outfit-Medium.ttf")
    LabelBase.register(name="OutfitRegular", fn_regular="font/Outfit-Regular.ttf")
    LabelBase.register(name="RobotoLight", fn_regular="font/roboto/Roboto-Light.ttf")
    LabelBase.register(name="RobotoRegular", fn_regular="font/roboto/Roboto-Regular.ttf")
    LabelBase.register(name="RobotoMedium", fn_regular="font/roboto/Roboto-Medium.ttf")
    LabelBase.register(name="RobotoSemiBold", fn_regular="font/roboto/Roboto-SemiBold.ttf")
    LabelBase.register(name="RobotoBold", fn_regular="font/roboto/Roboto-Bold.ttf")
    LabelBase.register(name="RobotoExtraBold", fn_regular="font/roboto/Roboto-ExtraBold.ttf")
    LabelBase.register(name="RobotoBlack", fn_regular="font/roboto/Roboto-Black.ttf")




    theme_cls.font_styles["RobotoLight"] = {
        "small": {
            "font-name": "RobotoLight",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "RobotoLight",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "RobotoLight",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }

    theme_cls.font_styles["RobotoMedium"] = {
        "small": {
            "font-name": "RobotoMedium",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "RobotoMedium",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "RobotoMedium",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }

    theme_cls.font_styles["RobotoBold"] = {
        "small": {
            "font-name": "RobotoBold",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "RobotoBold",
            "font-size": sp(20),
            "line-height": 1.5,
        },
        "large": {
            "font-name": "RobotoBold",
            "font-size": sp(28),
            "line-height": 1.75,
        },
    }

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
    """ theme_cls.font_styles["Display"] = {
        "large": {
            "font-size": 112,
            "line-height": 112,
            "font-name": "RobotoLight",
            "letter-spacing": -1,
        },
        "small": {
            "font-name": "RobotoLight",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-name": "RobotoLight",
            "font-size": sp(20),
            "line-height": 1.5,
        }
    }

    theme_cls.font_styles["Headline"] = {
        "large": {
            "font-size": 112,
            "line-height": 112,
            "font-name": "RobotoLight",
            "letter-spacing": -1,
        },
        "small": {
            "font-name": "RobotoLight",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-size": 56,
            "line-height": 56,
            "font-name": "RobotoLight",
            "letter-spacing": -0.5,
        }
    }

    theme_cls.font_styles["Title"] = {
        "large": {
            "font-size": 112,
            "line-height": 112,
            "font-name": "RobotoLight",
            "letter-spacing": -1,
        },
        "small": {
            "font-name": "RobotoLight",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-size": 24,
            "line-height": 24,
            "font-name": "RobotoLight",
            "letter-spacing": -0.1,
        }
    }

    theme_cls.font_styles["Body"] = {
        "large": {
            "font-size": 112,
            "line-height": 112,
            "font-name": "RobotoLight",
            "letter-spacing": -1,
        },
        "small": {
            "font-name": "RobotoLight",
            "font-size": sp(14),
            "line-height": 1.25,
        },
        "medium": {
            "font-size": 14,
            "line-height": 14,
            "font-name": "RobotoLight",
            "letter-spacing": -0.1,
        }
    }

    theme_cls.font_styles["Label"] = {
        "large": {
            "font-size": 56,
            "line-height": 56,
            "font-name": "RobotoLight",
            "letter-spacing": -1,
        },
        "medium": {
            "font-size": 14,
            "line-height": 14,
            "font-name": "RobotoLight",
            "letter-spacing": -0.1,
        },
        "small": {
            "font-size": 12,
            "line-height": 12,
            "font-name": "RobotoLight",
            "letter-spacing": -0.1,
        },
    }
    """
    theme_cls.font_styles["Body1"] = theme_cls.font_styles["RobotoMedium"]
    theme_cls.font_styles["Button"] = theme_cls.font_styles["RobotoMedium"]
    theme_cls.font_styles["Subtitle1"] = theme_cls.font_styles["RobotoMedium"]
    theme_cls.font_styles["H6"] = theme_cls.font_styles["RobotoMedium"]
