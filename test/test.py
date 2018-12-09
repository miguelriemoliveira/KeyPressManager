#!/usr/bin/env python
"""
This is a long, multiline description
"""

# -------------------------------------------------------------------------------
# --- IMPORTS (standard, then third party, then my own modules)
# -------------------------------------------------------------------------------
import cv2
import numpy as np
import KeyPressManager.KeyPressManager
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# -------------------------------------------------------------------------------
# --- FUNCTIONS
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# --- MAIN
# -------------------------------------------------------------------------------
if __name__ == "__main__":

    # ---------------------------------------
    # --- INITIALIZATION
    # ---------------------------------------

    #Opencv window
    image = np.random.rand(300,200)
    cv2.namedWindow('TestWindow', cv2.WINDOW_NORMAL)
    cv2.imshow('TestWindow', image)
    key = cv2.waitKey(15)

    #Matplot lib window
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    KeyPressManager.KeyPressManager.drawAxis3D(ax, np.identity(4), "world", axis_scale=0.7, line_width=3)
    # KeyPressManager.drawAxis3D()

    wm = KeyPressManager.KeyPressManager.WindowManager(fig)

    if wm.waitForKey():
        exit(0)


