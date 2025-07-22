class Stack:
    """
    Stack implementation using Python list (array-based)
    LIFO - Last In, First Out
    """
    
    def __init__(self, max_size=None):
        """
        Initialize empty stack
        :param max_size: maximum capacity (None for unlimited)
        """
        self.stack = []
        self.max_size = max_size
    
    # ============= CORE STACK OPERATIONS =============
    
    def push(self, val):
        """
        Add element to top of stack
        Time: O(1), Space: O(1)
        Raises: StackOverflowError if stack is full
        """
        if self.max_size: 
            if len(self.stack) < self.max_size:
                self.stack.append(val)
            else:
                raise StackOverflowError
        else:
            self.stack.append(val)
    
    def pop(self):
        """
        Remove and return top element
        Time: O(1), Space: O(1)
        Returns: top element
        Raises: StackUnderflowError if stack is empty
        """
        # TODO: Check if stack is empty
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise StackUnderflowError
    
    def peek(self):
        """
        Return top element without removing it
        Time: O(1), Space: O(1)
        Returns: top element
        Raises: StackUnderflowError if stack is empty
        """
        # TODO: Check if empty
        # TODO: Return last element without removing
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise StackUnderflowError
    
    def top(self):
        """
        Alias for peek() - return top element
        """
        return self.peek()
    
    # ============= UTILITY METHODS =============
    
    def is_empty(self):
        """
        Check if stack is empty
        Time: O(1), Space: O(1)
        """
        # TODO: Return True if no elements
        return self.stack==[]
    
    def is_full(self):
        """
        Check if stack is full (only relevant if max_size is set)
        Time: O(1), Space: O(1)
        """
        # TODO: Return True if max_size is set and reached capacity
        if self.max_size:
            return len(self.stack)==self.max_size
        else:
            return False
    
    def size(self):
        """
        Get number of elements in stack
        Time: O(1), Space: O(1)
        """
        # TODO: Return length of internal list
        return len(self.stack)
    
    def clear(self):
        """
        Remove all elements from stack
        Time: O(1), Space: O(1)
        """
        # TODO: Clear the internal list
        self.stack = []
    
    def capacity(self):
        """
        Get maximum capacity of stack
        Time: O(1), Space: O(1)
        """
        # TODO: Return max_size or "Unlimited"
        if self.max_size:
            return self.max_size
        else:
            return "Unlimited"
    
    # ============= SEARCH AND ADVANCED OPERATIONS =============
    
    def search(self, val):
        """
        Search for element and return distance from top (1-indexed)
        Time: O(n), Space: O(1)
        Returns: position from top (1-indexed) or -1 if not found
        """
        # TODO: Search from end of list backwards
        # TODO: Return 1-indexed position from top
        for i in range(len(self.stack)-1, -1, -1):  # Include index 0
            if self.stack[i] == val:
                return len(self.stack) - i 
        
        return -1
    
    def contains(self, val):
        """
        Check if stack contains a value
        Time: O(n), Space: O(1)
        """
        # TODO: Check if val is in the stack
        return val in self.stack
    
    def reverse(self):
        """
        Reverse the stack in-place
        Time: O(n), Space: O(1)
        """
        # TODO: Reverse the internal list
        start = 0
        end = len(self.stack)-1
        while start < end:
            temp = self.stack[start]
            self.stack[start] = self.stack[end]
            self.stack[end] = temp
            start+=1
            end-=1
            
    def copy(self):
        """
        Create a shallow copy of the stack
        Time: O(n), Space: O(n)
        Returns: new Stack with same elements
        """
        # TODO: Create new stack with copy of elements
        new_stack = Stack(self.max_size)
        new_stack.stack = self.stack.copy()
        return new_stack
    
    # ============= DISPLAY METHODS =============
    
    def to_list(self):
        """
        Convert stack to list (top to bottom order)
        Time: O(n), Space: O(n)
        Returns: list of values from top to bottom
        """
        # TODO: Return copy of list in reverse order (top first)
        reverse_stack = []
        for i in range(len(self.stack)-1, -1, -1):  # Go from top to bottom
            reverse_stack.append(self.stack[i])
        return reverse_stack
    
    def __str__(self):
        """
        String representation of stack
        Format: "TOP -> val1 -> val2 -> val3 -> BOTTOM"
        """
        # TODO: Create string representation showing stack structure
        out = "TOP ->"
        for i in range(len(self.stack)):
            out += str(self.stack[i])
            out += "->"
        out += "BOTTOM"
        return out
    
    def __repr__(self):
        """
        Developer representation of stack
        """
        return f"Stack(size={self.size()})"
    
    def __len__(self):
        """
        Allow len(stack) to work
        """
        return self.size()
    
    def __bool__(self):
        """
        Allow if stack: to work (True if not empty)
        """
        return not self.is_empty()
    
    def __contains__(self, val):
        """
        Allow 'val in stack' to work
        """
        return self.contains(val)
    
    def __iter__(self):
        """
        Make stack iterable (top to bottom)
        """
        # TODO: Yield elements from top to bottom
        for i in range(len(self.stack)-1, -1, -1):
            yield self.stack[i]


# ============= CUSTOM EXCEPTIONS =============

class StackOverflowError(Exception):
    """Raised when trying to push to a full stack"""
    pass

class StackUnderflowError(Exception):
    """Raised when trying to pop from an empty stack"""
    pass


# ============= SPECIALIZED STACK IMPLEMENTATIONS =============

class MinStack:
    """
    Stack that supports getting minimum element in O(1) time
    """
    
    def __init__(self):
        """
        Initialize main stack and auxiliary min stack
        """
        # TODO: Create main stack for elements
        # TODO: Create auxiliary stack for tracking minimums
        self.main_stack = []
        self.min_stack = []
    
    def push(self, val):
        """
        Push value and update minimum tracking
        Time: O(1), Space: O(1)
        """
        # TODO: Push to main stack
        # TODO: Push to min stack if val <= current min (or stack empty)
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Pop value and update minimum tracking
        Time: O(1), Space: O(1)
        """
        # TODO: Pop from main stack
        # TODO: Pop from min stack if popped value equals current min
        if not self.main_stack:
            raise StackUnderflowError("Stack is empty")
        val = self.main_stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()
        return val
    
    def top(self):
        """
        Get top element
        Time: O(1), Space: O(1)
        """
        # TODO: Return top of main stack
        return self.main_stack[-1]
    
    def get_min(self):
        """
        Get minimum element in O(1) time
        Time: O(1), Space: O(1)
        """
        # TODO: Return top of min stack
        return self.min_stack[-1]


class MaxStack:
    """
    Stack that supports getting maximum element in O(1) time
    """
    
    def __init__(self):
        # TODO: Initialize main stack and max stack
        self.main_stack = []
        self.max_stack = []
    
    def push(self, val):
        # TODO: Push with max tracking
        self.main_stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        # TODO: Pop with max tracking
        if not self.main_stack:
            raise StackUnderflowError("Stack is empty")
        val = self.main_stack.pop()
        if self.max_stack and val == self.max_stack[-1]:
            self.max_stack.pop()
        return val
    
    def top(self):
        # TODO: Return top element
        return self.main_stack[-1]
    
    def get_max(self):
        # TODO: Return maximum in O(1) time
        return self.max_stack[-1]