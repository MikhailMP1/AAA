import math
from typing import List


class CountVectorizer(object):
    def fit_transform(self, raw_document):
        self.raw_document = raw_document
        col = 0
        text = {}
        for row in raw_document:
            for word in row.lower().split():
                if word not in text.keys():
                    text[word] = col
                    col += 1
        text_words = list(text.keys())
        vector = [0 for i in range(col)]
        matrix = [vector.copy() for i in range(len(raw_document))]

        num_row = 0
        for row in raw_document:
            for word in row.lower().split():
                matrix[num_row][text_words.index(word)] += 1
            num_row += 1
        return matrix

    def get_feature_name(self):
        words_li = []
        for row in self.raw_document:
            for word in row.lower().split():
                if word not in words_li:
                    words_li.append(word)
        return words_li


class TfIdfTransformer:
    def __init__(self):
        self.tf_matrix = []
        self._idf = []

    def _tf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        self.tf_matrix = []
        for vec in count_matrix:
            number_of_word = sum(vec)
            tf_matrix_row = [round(obj / number_of_word, 3) for obj in vec]
            self.tf_matrix.append(tf_matrix_row)

        return self.tf_matrix

    def _idf_transform(self, count_matrix: List[List[float]]) -> List[float]:
        result = list()
        document_count = len(count_matrix) + 1

        for col in range(len(count_matrix[0])):
            cur_sum = 0
            for row in range(len(count_matrix)):
                cur_sum += bool(count_matrix[row][col])
            result.append(cur_sum + 1)

        for i in range(len(result)):
            result[i] = math.log(result[i] / document_count) + 1

        return result

    def fit_transform(self, matrix):
        self._tf_transform(matrix)
        self._idf_transform(matrix)

        result = []
        for text in self.tf_matrix:
            result.append([round(a * b, 3) for a, b in zip(text, self._idf)])

        return result


class TfIdfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    tf_idf = TfIdfTransformer()
    tf_matrix = tf_idf._tf_transform(count_matrix)
    expected_result = [
        [0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143],
    ]
    for i in range(len(tf_matrix)):
        for j in range(len(tf_matrix[i])):
            assert abs(expected_result[i][j] - tf_matrix[i][j]) < 10e-10
            