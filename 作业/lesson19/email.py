class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.

    >>> s = Server()
    >>> # Dummy client class implementation for testing only
    >>> class Client:
    ...     def __init__(self, server, name):
    ...         self.inbox = []
    ...         self.server = server
    ...         self.name = name
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> s.register_client(a) 
    >>> s.register_client(b)
    >>> len(s.clients)  # we have registered 2 clients
    2
    >>> all([type(c) == str for c in s.clients.keys()])  # The keys in self.clients should be strings
    True
    >>> all([type(c) == Client for c in s.clients.values()])  # The values in self.clients should be Client instances
    True
    >>> new_a = Client(s, 'Alice')  # a new client with the same name as an existing client
    >>> s.register_client(new_a)
    >>> len(s.clients)  # the key of a dictionary must be unique
    2
    >>> s.clients['Alice'] is new_a  # the value for key 'Alice' should now be updated to the new client new_a
    True
    >>> e = Email("I love 61A", b, 'Alice')
    >>> s.send(e)
    >>> len(new_a.inbox)  # one email has been sent to new Alice
    1
    >>> type(new_a.inbox[0]) == Email  # a Client's inbox is a list of Email instances
    True
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to.
            email is an instance of the Email class.
        """
        self.clients[email.recipient_name].inbox.append(email)

    def register_client(self, client):
        """Add a client to the clients mapping (which is a 
        dictionary from client names to client instances).
            client is an instance of the Client class.
        """
        self.clients[client.name]=client
class Client:
    """A client has a server, a name (str), and an inbox (list).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient."""
        email = Email(message, self, recipient_name)
        self.server.send(email)