class FPTreeNode:
    def __init__(self, item, count=1):
        """Node class for FP-tree"""
        self.item = item  # Item stored in this node
        self.count = count  # Count of how many times the item occurs
        self.parent = None  # Parent node in the tree
        self.children = {}  # Children of this node
        self.link = None  # Link to another node with the same item for header table navigation


class FPGrowth:
    def __init__(self, min_support):
        """FP-Growth class to handle FP-tree construction and mining"""
        self.min_support = min_support  # Minimum support threshold
        self.header_table = {}  # Header table to store links to item nodes in the tree

    def build_fp_tree(self, transactions):
        """Builds the FP-tree from the list of transactions"""
        # Step 1: Calculate item frequency and filter by min_support
        item_count = {}
        for transaction in transactions:
            for item in transaction:
                item_count[item] = item_count.get(item, 0) + 1

        # Step 2: Filter items that don't meet the min_support threshold
        frequent_items = {item: count for item, count in item_count.items() if count >= self.min_support}

        # Step 3: Initialize Header Table
        self.header_table = {item: [count, None] for item, count in frequent_items.items()}

        # Step 4: Create the root of the FP-tree
        root = FPTreeNode(None)  # Root node does not store any item

        # Step 5: Insert transactions into the tree
        for transaction in transactions:
            # Filter and sort items in the transaction by frequency
            sorted_items = [item for item in transaction if item in frequent_items]
            sorted_items.sort(key=lambda i: frequent_items[i], reverse=True)
            if sorted_items:
                self._insert_tree(sorted_items, root)

        return root, self.header_table

    def _insert_tree(self, items, node):
        """Inserts sorted items into the FP-tree recursively"""
        if not items:
            return

        first_item = items[0]
        if first_item in node.children:
            # If the item already exists as a child, increment its count
            node.children[first_item].count += 1
        else:
            # Create a new node for the first item
            new_node = FPTreeNode(first_item)
            new_node.parent = node
            node.children[first_item] = new_node

            # Update header table links for this item
            if self.header_table[first_item][1] is None:
                self.header_table[first_item][1] = new_node
            else:
                current_node = self.header_table[first_item][1]
                while current_node.link is not None:
                    current_node = current_node.link
                current_node.link = new_node

        # Recursively insert the remaining items into the tree
        self._insert_tree(items[1:], node.children[first_item])

    def mine_patterns(self, tree):
        """Mine frequent patterns from the FP-tree"""
        patterns = {}
        # Iterate over items in the header table, sorted by their frequency
        for item, node_info in sorted(self.header_table.items(), key=lambda x: x[1][0]):
            patterns[item] = node_info[0]  # Add single-item patterns

            # Build the conditional FP-tree for this item
            suffix_tree = self._build_conditional_tree(item)
            if suffix_tree:
                # Recursively mine patterns from the conditional FP-tree
                suffix_patterns = self.mine_patterns(suffix_tree)
                for suffix, count in suffix_patterns.items():
                    patterns[item + ' ' + suffix] = count

        return patterns

    def _build_conditional_tree(self, item):
        """Builds a conditional FP-tree for a given item"""
        # Placeholder for the method to create conditional trees
        # This would gather suffix paths and build an FP-tree
        pass
