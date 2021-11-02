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

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',
        'say no to racism'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_name())
    print(count_matrix)
