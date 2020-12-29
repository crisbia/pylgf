import glfw
from OpenGL.GL import *

def main():
    # Initialize the library
    if not glfw.init():
        return
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(640, 480, "Hello World", None, None)
    if not window:
        glfw.terminate()
        return

    window2 = glfw.create_window(480, 640, "Hello World 2", None, None)
    if not window2:
        glfw.terminate()
        return

    windows = [window, window2]

    # Loop until the user closes the window
    while len(windows) > 0:
        active_windows = []
        for w in windows:
            if glfw.window_should_close(w):
                glfw.destroy_window(w)
            else:
                active_windows.append(w)

        windows = active_windows                

        for w in windows:
            # Make the window's context current
            glfw.make_context_current(w)
    
            # Render here, e.g. using pyOpenGL
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glClearColor(1, 0, 0, 1)

            # Swap front and back buffers
            glfw.swap_buffers(w)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
