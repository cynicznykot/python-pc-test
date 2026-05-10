class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first_comment, second_comment):
        return f"{first_comment} {second_comment}"


my_comment = Comment("My comment")

m_1 = Comment.merge_comments("Hello", "World")
print(m_1)

m_2 = my_comment.merge_comments("Hi", "World")
print(m_2)