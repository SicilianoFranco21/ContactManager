from controller.contactController import ContactController


def main() -> None:
    contact_controller: ContactController = ContactController()
    contact_controller.run()
main()