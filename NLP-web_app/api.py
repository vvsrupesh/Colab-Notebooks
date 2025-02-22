import nlpcloud




def ner(text):
    client = nlpcloud.Client("finetuned-llama-3-70b", "1400df67c06e6ae5a78388ad45618a6dc5c21440", gpu=True)
    client.entities(
        """John Doe started learning Javascript when he was 15 years old. After a couple of years he switched to Python and starter learning low level programming. He is now a Go expert at Google.""",
        searched_entity="programming languages")
    return ner
