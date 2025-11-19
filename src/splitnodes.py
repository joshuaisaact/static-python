from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            result.append(old_node)
        elif delimiter not in old_node.text:
            result.append(old_node)
        else:
            split_words = old_node.text.split(delimiter)
            if len(split_words) % 2 != 1:
                raise Exception(f"This is not valid markdown syntax: {old_node.text}")
            for i, word in enumerate(split_words):
                if word == "":
                    continue
                if i % 2 == 0:
                    result.append(TextNode(split_words[i], TextType.TEXT))
                else:
                    result.append(TextNode(split_words[i], text_type))
    return result
