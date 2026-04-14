import fire

from chatbot.bootstrap.console import CliCommand


class Command:
    def __init__(self):
        self.chatbotapi = CliCommand()


def main():
    """Trigger function for fire command line interface"""
    fire.Fire(Command)


if __name__ == "__main__":
    main()
