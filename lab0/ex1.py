from learntools.core import *
from learntools.core.problem import injected

class ExerciseFormatTutorial(CodingProblem):
    _var = 'color'
    _hint = "Your favorite color rhymes with *people*."
    _solution = CS('color = "purple"')
    def check(self, color):
        assert color.lower() == "purple"

    @property
    def _correct_message(self):
        history = self._view.interactions
        if history['hint'] == 0 and history['solution'] == 0:
            return ("What?! You got it right without needing a hint or anything?"
                    " Drats. Well hey, you should still continue to the next step"
                    " to get some practice asking for a hint and checking solutions."
                    " (Even though you obviously don't need any help here.)"
                    )
        return ''

    # def _failure_message(self, var, actual, expected):
    #     if (
    #             any(actual.endswith(suff) for suff in ['oo', 'ue', 'ew'])
    #             and actual.strip().lower() != 'blue'
    #         ):
    #         return "Ha ha, very funny."
    #     elif actual.strip(' .!').lower() == 'ni':
    #         return "Please! Please! No more! We will find you a shrubbery."
        return ("{} is not your favorite color!"
                " Well, maybe it is, but we're writing the rules. The point"
                " of this question is to force you to get some practice asking"
                " for a hint. Go ahead and uncomment the call to `q1.hint()`"
                " in the code cell below, for a hint at what your favorite color"
                " *really* is.").format(actual)


qvars = bind_exercises(globals(), [
    ExerciseFormatTutorial,
    # CircleArea,
    # VariableSwap,
    # ArithmeticParens,
    # CandySplitting,
    # MysteryExpression,
    # QuickdrawGridProblem,
    # SameValueInitializationRiddle,
    ],
    start=1,
    var_format='ex{n}',
    )
__all__ = list(qvars)
