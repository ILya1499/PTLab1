# -*- coding: utf-8 -*-
from Types import DataType
RatingType = dict[str, float]


class CalcRatingOtl:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def so(self) -> str:
        for key in self.data:
            current = 0
            for subject in self.data[key]:
                if subject[1] >= 76:
                    current = current + 1
                if current >= 3:
                    return key
        return "Студентов не найдено"
