class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def __str__(self):
        attrs = vars(self)
        return 'Question({})'.format(', '.join('{}={}'.format(k, v) for k, v in attrs.items()))

