

class FPTreeNode:
    def __init__(self, item, count=1):
        self.item = item
        self.count = count
        self.parent = None
        self.children = {}
        self.link = None

class FPGrowth:
    def __init__(self, min_support):
        self.min_support = min_support
        self.header_table = {}

    def build_fp_tree(self, transactions):
       
        item_count = {}
        for transaction in transactions:
            for item in transaction:
                item_count[item] = item_count.get(item, 0) + 1

        
        items = {k: v for k, v in item_count.items() if v >= self.min_support}

       
        self.header_table = {k: [v, None] for k, v in items.items()}

        
        root = FPTreeNode(None)

        for transaction in transactions:
            
            sorted_items = sorted([item for item in transaction if item in items],
                                  key=lambda i: items[i], reverse=True)
            self._insert_tree(sorted_items, root)

        return root, self.header_table

    def _insert_tree(self, items, node):
        if not items:
            return

        first_item = items[0]
        if first_item in node.children:
            node.children[first_item].count += 1
        else:
            new_node = FPTreeNode(first_item)
            new_node.parent = node
            node.children[first_item] = new_node

           
            if self.header_table[first_item][1] is None:
                self.header_table[first_item][1] = new_node
            else:
                current_node = self.header_table[first_item][1]
                while current_node.link is not None:
                    current_node = current_node.link
                current_node.link = new_node

       
        self._insert_tree(items[1:], node.children[first_item])

    def mine_patterns(self, tree):
        
        patterns = {}
        for item, node_info in sorted(self.header_table.items(), key=lambda x: x[1][0]):
            patterns[item] = node_info[0]
            suffix_tree = self._build_conditional_tree(item)
            if suffix_tree:
                suffix_patterns = self.mine_patterns(suffix_tree)
                for suffix, count in suffix_patterns.items():
                    patterns[item + ' ' + suffix] = count

        return patterns

    def _build_conditional_tree(self, item):
       
        pass
