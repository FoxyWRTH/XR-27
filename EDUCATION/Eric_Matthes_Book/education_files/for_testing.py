"""
Задачи из книги. --Глава 11. Тестирование. Функции и классы для тестирования.
"""


def normal_name_format(first_name, last_name, middle_name=''):
    """Возвращает отформатированное Имя и Фамилию.
    Если есть промежуточное имя, возвращает отформатированный набор"""
    if middle_name != '':
        result = f'{first_name} {middle_name} {last_name}'
        return result.title()
    result = f'{first_name} {last_name}'
    return result.title()


class AnonymousSurvey():
    """Сбор анонимных данных"""

    def __init__(self, question):
        self.question = question
        self.answer_list = []

    def show_question(self):
        """Вывод вопроса"""
        print(self.question)

    def input_answer(self, new_answer):
        """Ввод ответа и запись в список."""
        self.answer_list.append(new_answer)
        print('Не правильно.')

    def all_answers(self):
        """Вывод всего списка ответов."""
        for _ in self.answer_list:
            print(f'- {_}')
