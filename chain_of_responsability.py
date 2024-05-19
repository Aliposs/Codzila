class Document:
    def __init__(self, content):
        self.content = content

class Processor:
    def __init__(self, next_processor=None):
        self.next_processor = next_processor

    def process(self, document):
        if self.next_processor:
            self.next_processor.process(document)

class SpellCheckProcessor(Processor):
    def process(self, document):
        print("Spell check complete.")
        super().process(document)

class GrammarCheckProcessor(Processor):
    def process(self, document):
        print("Grammar check complete.")
        super().process(document)

class FormatCheckProcessor(Processor):
    def process(self, document):
        print("Format check complete.")
        super().process(document)

# Setting up the chain
formatter = FormatCheckProcessor()
grammar_checker = GrammarCheckProcessor(formatter)
spell_checker = SpellCheckProcessor(grammar_checker)

# Processing a document
doc = Document("Sample content")
spell_checker.process(doc)