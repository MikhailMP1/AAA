class CountVectorizer(object):
    @staticmethod
    def fit_transform(raw_document):
        col = 0
        text = {}
        n_rows = 0
        for row in raw_document:
            n_rows += 1
            for word in row.split():
                if word.lower() not in text.keys():
                    text[word.lower()] = col
                    col += 1
        text_words = list(text.keys())
        vector = [0 for i in range((max(text.values())) + 1)]
        matrix = [vector.copy() for i in range(n_rows)]

        num_row = 0
        for row in raw_document:
            for word in row.split():
                matrix[num_row][text_words.index(word.lower())] += 1
            num_row += 1
        return matrix

    @staticmethod
    def get_feature_name(raw_document):
        words_li = []
        for row in raw_document:
            for word in row.split():
                if word.lower() not in words_li:
                    words_li.append(word.lower())
        return words_li


corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste',
    'say no to racism'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_name(corpus))
print(count_matrix)
