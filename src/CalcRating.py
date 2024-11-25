# -*- coding: utf-8 -*-
from Types import DataType
RatingType = dict[str, float]

class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating

    def so(self) -> str:
        for key in self.data:
            current = 0
            for subject in self.data[key]:
                if subject[1] >= 76:
                    current = current + 1
                if current >= 3:
                    return key
        return "Студентов не найдено"
            