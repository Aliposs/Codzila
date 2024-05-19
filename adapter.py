class OldPrinter:
    def print(self, text):
        print(f"Old Printer: {text}")

class NewPrinterInterface:
    def print_text(self, text):
        pass

class OldPrinterAdapter(NewPrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print_text(self, text):
        self.old_printer.print(text)

old_printer = OldPrinter()
adapter = OldPrinterAdapter(old_printer)
adapter.print_text("Hello, World!")  # Old Printer: Hello, World!
