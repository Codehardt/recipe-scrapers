from ._grouping_utils import group_ingredients
from .einfachkochen import EinfachKochen


class EinfachBacken(EinfachKochen):
    @classmethod
    def host(cls):
        return "einfachbacken.de"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".paragraph--ParagraphIngredientsBlock h4",
            ".paragraph--ParagraphIngredientsBlock section > div > div",
        )
