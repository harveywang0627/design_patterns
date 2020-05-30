from abc import ABC, abstractmethod
import copy


class ResumeProtoType(ABC):

    @abstractmethod
    def set_key_point(self):
        pass

    def clone(self):
        return copy.deepcopy(self)


class SoftWareResume(ResumeProtoType):

    def __init__(self, name, birth, score):
        self.resume_type = "SOFTWARE"
        self.name = name
        self.birth = birth
        self.score = score
        self.key_point = ""

    def set_key_point(self):
        self.key_point = self.name + self.score


class ManagerResume(ResumeProtoType):

    def __init__(self, name, birth, score):
        self.resume_type = "MANAGER"
        self.name = name
        self.birth = birth
        self.score = score
        self.key_point = ""

    def set_key_point(self):
        self.key_point = self.birth + self.score


class ResumePrinter(object):

    def __init__(self):

        self.resume_map = {"SOFTWARE": SoftWareResume("Jack", "1991", "100"),
                           "MANAGER": ManagerResume("Leo", "1988", "80")}

    def get_resume(self, rt):

        return self.resume_map[rt]
