class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    

class LinkedList:
    """
    Singly Linked List implementation
    """
    
    def __init__(self):
        """
        Initialize empty linked list
        """
        self.head = None
        self.size = 0
    
    # ============= INSERTION METHODS =============
    
    def insert_head(self, val):
        """
        Insert at the beginning of the list
        Time: O(1), Space: O(1)
        """
        # TODO: Create new node, set its next to current head, update head
        node = Node(val, self.head)
        self.head = node
        self.size+=1
    
    def insert_tail(self, val):
        """
        Insert at the end of the list
        Time: O(n), Space: O(1)
        """
        # TODO: If empty, same as insert_head
        # Otherwise, traverse to end and add new node
        if self.head:
            curr = self.head
            while curr.next:  # Stop at last node, not None
                curr = curr.next
            curr.next = Node(val)
        else:
            self.head = Node(val)
        
        self.size+=1
    
    def insert_at_index(self, index, val):
        """
        Insert at specific index (0-based)
        Time: O(n), Space: O(1)
        """
        # TODO: Handle edge cases (index 0, out of bounds)
        # Traverse to position index-1, insert new node
        if index == 0:
            self.insert_head(val)
        elif index == self.size:
            self.insert_tail(val)
        elif index > self.size:
            return -1
        else:
            curr = self.head
            i = 0
            while curr:
                if i == index-1:
                    temp = curr.next
                    curr.next = Node(val, temp)
                    break
        
            self.size+=1

    
    # ============= DELETION METHODS =============
    
    def delete_head(self):
        """
        Delete the first node
        Time: O(1), Space: O(1)
        Returns: deleted value or None if empty
        """
        # TODO: Handle empty list, update head to head.next
        if self.head:
            temp = self.head
            self.head = self.head.next
            self.size-=1
            return temp
        else:
            return None
    
    def delete_tail(self):
        """
        Delete the last node
        Time: O(n), Space: O(1)
        Returns: deleted value or None if empty
        """
        # TODO: Handle empty/single node, find second-to-last node
        if not self.head:
            return None
        elif self.size == 1:
            temp = self.head
            self.head = None
            self.size-=1
            return temp
        else:
            curr = self.head
            idx = 0
            while curr:
                if idx == self.size - 2:
                    temp = curr.next
                    curr.next = None
                    return temp
                idx += 1
                curr = curr.next
    
    def delete_value(self, val):
        """
        Delete first occurrence of value
        Time: O(n), Space: O(1)
        Returns: True if deleted, False if not found
        """
        # TODO: Handle head deletion, track previous node
        if self.head and self.head.val == val:
            self.delete_head()
            return True
        else:
            curr = self.head
            prev = None
            while curr:
                if curr.val == val:
                    prev.next = curr.next
                    return True
                prev = curr
                curr = curr.next
            
            return False
    
    def delete_at_index(self, index):
        """
        Delete node at specific index
        Time: O(n), Space: O(1)
        Returns: deleted value or None if invalid index
        """
        # TODO: Handle edge cases, traverse to index-1
        if index == 0:
            self.delete_head()
        elif index == self.size - 1:
            self.delete_tail()
        elif index < 0 or index > self.size:
            return None
        else:
            curr = self.head
            prev = None
            i = 0
            while curr:
                if i == index - 1:
                    prev.next = curr.next
                    self.size-=1
                    return curr.val
                prev = curr
                curr = curr.next
    
    # ============= SEARCH METHODS =============
    
    def search(self, val):
        """
        Find if value exists in list
        Time: O(n), Space: O(1)
        Returns: True if found, False otherwise
        """
        # TODO: Traverse and compare values

        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next

        return False
    
    def find_index(self, val):
        """
        Find index of first occurrence of value
        Time: O(n), Space: O(1)
        Returns: index if found, -1 otherwise
        """
        # TODO: Traverse with counter
        curr = self.head
        idx = 0
        while curr:
            if curr.val == val:
                return idx
            curr = curr.next
            idx+=1
        
        return -1
    
    def get_at_index(self, index):
        """
        Get value at specific index
        Time: O(n), Space: O(1)
        Returns: value at index or None if invalid
        """
        # TODO: Traverse to index, return value
        curr = self.head
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx+=1
        
        return None
    
    # ============= UTILITY METHODS =============
    
    def is_empty(self):
        """
        Check if list is empty
        Time: O(1), Space: O(1)
        """
        # TODO: Check if head is None
        return self.head is None
    
    def get_size(self):
        """
        Get number of nodes in list
        Time: O(1), Space: O(1) if tracking size
        Time: O(n), Space: O(1) if counting
        """
        # TODO: Return self.size or count nodes
        return self.size
    
    def clear(self):
        """
        Remove all nodes from list
        Time: O(1), Space: O(1)
        """
        # TODO: Set head to None, size to 0
        pass
    
    # ============= ADVANCED OPERATIONS =============
    
    def reverse(self):
        """
        Reverse the linked list in-place
        Time: O(n), Space: O(1)
        """
        # TODO: Three-pointer technique
        dummy = self.head
        curr = dummy
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        self.head = prev
    
    def find_middle(self):
        """
        Find the middle node using slow/fast pointers
        Time: O(n), Space: O(1)
        Returns: middle node or None if empty
        """
        # TODO: Slow/fast pointer technique
        if self.head:
            slow = fast = self.head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        else:
            return None
        
    def has_cycle(self):
        """
        Detect if there's a cycle in the list
        Time: O(n), Space: O(1)
        Returns: True if cycle exists, False otherwise
        """
        # TODO: Floyd's cycle detection (slow/fast pointers)
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
            
    
    def remove_duplicates(self):
        """
        Remove duplicate values (assuming sorted list)
        Time: O(n), Space: O(1)
        """
        # TODO: Compare current with next, skip duplicates
        if self.size < 2:
            return
        else:
            curr = self.head.next
            prev = self.head
            while curr:
                if curr.val == prev.val:
                    prev.next = curr.next

    
    def merge_sorted(self, other_list):
        """
        Merge with another sorted linked list
        Time: O(n + m), Space: O(1)
        Returns: new LinkedList with merged result
        """
        # TODO: Two-pointer merge technique
        p1 = self.head
        p2 = other_list
        dummy  = Node()
        current = dummy
        

        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            
            current = current.next
        
        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        return dummy.next
    
    # ============= DISPLAY METHODS =============
    
    def to_list(self):
        """
        Convert to Python list for easy viewing
        Time: O(n), Space: O(n)
        Returns: list of values
        """
        # TODO: Traverse and collect values
        curr = self.head
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        return nodes

    
    def __str__(self):
        """
        String representation of the list
        """
        # TODO: Return "val1 -> val2 -> val3 -> None"
        curr = self.head
        out = ""
        while curr:
            out += f"{curr.val} -> "
            curr = curr.next
        out += "None"
        print(out)
            
    
    def __len__(self):
        """
        Allow len(linked_list) to work
        """
        return self.get_size()
    
    def __contains__(self, val):
        """
        Allow 'val in linked_list' to work
        """
        return self.search(val)