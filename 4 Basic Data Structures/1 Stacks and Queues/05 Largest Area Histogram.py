def largestRectangleArea(heights):
    stack = [-1]
    heights.append(0)
    ans = 0
    for i, height in enumerate(heights):
        while heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans


if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    print(largestRectangleArea(arr))
