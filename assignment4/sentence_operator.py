# sentence_operator.py

class sentence_operator:
    def __init__(self):
        pass

    def my_split(self, sentence, separator):
        result = []
        current_item = ""

        for char in sentence:
            if char == separator:
                if current_item:
                    result.append(current_item)
                    current_item = ""
            else:
                current_item += char

        # Append the last item if there's any remaining part after the loop
        if current_item:
            result.append(current_item)

        return result

    def my_join(self, items, separator):
        result = ""

        for i, item in enumerate(items):
            if i > 0:
                result += separator
            result += item

        return result
