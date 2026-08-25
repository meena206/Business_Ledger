class TrieNode:
    def __init__(self):
        self.children = {}
        self.customer_ids = set()


class CustomerTrie:
    searchable_fields = ("name", "phone", "city")

    def __init__(self):
        self.root = TrieNode()

    def add(self, customer):
        customer_id = customer.id
        for field in self.searchable_fields:
            value = getattr(customer, field, "") or ""
            normalized_value = value.casefold()
            for start in range(len(normalized_value)):
                node = self.root
                for character in normalized_value[start:]:
                    node = node.children.setdefault(character, TrieNode())
                    node.customer_ids.add(customer_id)

    def search(self, query):
        node = self.root
        for character in query.casefold():
            node = node.children.get(character)
            if node is None:
                return set()
        return node.customer_ids.copy()