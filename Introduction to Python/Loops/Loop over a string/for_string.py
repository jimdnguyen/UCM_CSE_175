hello_world = "Hello, World!"

for ch in hello_world:    # Print each character from hello_world
    print(ch)

length = 0      # Initialize length variable

for ch in hello_world:
    length += 1


print(len(hello_world) == length)
