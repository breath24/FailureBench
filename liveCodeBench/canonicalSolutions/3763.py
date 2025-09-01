def separateSquares(squares):
    """
    Find the minimum y-coordinate of a horizontal line such that 
    the total area above equals the total area below the line.
    
    Args:
        squares: List of [x, y, l] where (x,y) is bottom-left corner and l is side length
    
    Returns:
        Float representing the y-coordinate of the dividing line
    """
    def area_below(y_line):
        """Calculate total area of squares below the horizontal line at y_line"""
        total = 0
        for x, y, l in squares:
            if y_line <= y:
                # Entire square is above the line
                area = 0
            elif y_line >= y + l:
                # Entire square is below the line
                area = l * l
            else:
                # Square is partially cut by the line
                # Area below = (height below line) * width
                area = (y_line - y) * l
            total += area
        return total
    
    # Calculate total area of all squares
    total_area = sum(l * l for x, y, l in squares)
    target = total_area / 2.0
    
    # Determine search range
    min_y = min(y for x, y, l in squares)
    max_y = max(y + l for x, y, l in squares)
    
    # Binary search for the exact y-coordinate
    left, right = min_y, max_y
    
    # Use enough iterations for required precision (10^-5)
    for _ in range(100):
        mid = (left + right) / 2.0
        area = area_below(mid)
        
        if area < target:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2.0


# Test with provided examples
if __name__ == "__main__":
    # Example 1
    squares1 = [[0,0,1],[2,2,1]]
    result1 = separateSquares(squares1)
    print(f"Example 1: squares = {squares1}")
    print(f"Result: {result1:.5f}")
    print(f"Expected: 1.0")
    print()
    
    # Example 2
    squares2 = [[0,0,2],[1,1,1]]
    result2 = separateSquares(squares2)
    print(f"Example 2: squares = {squares2}")
    print(f"Result: {result2:.5f}")
    print(f"Expected: 1.16667")
