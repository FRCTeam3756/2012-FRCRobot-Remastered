import numpy as np
from cscore import CameraServer

#############################################################

class Camera():
    def __init__(self) -> None:
        self.camera = CameraServer.startAutomaticCapture()
        self.camera.setResolution(640, 480)
        self.cvSink = CameraServer.getVideo()
        self.cvSource = CameraServer.putVideo("Camera Feed", 640, 480)

    def update_feed(self) -> None:
        img = np.zeros(shape=(480, 640, 3), dtype=np.uint8)
        time, img = self.cvSink.grabFrame(img)
        if time == 0:
            self.cvSource.notifyError(self.cvSink.getError())
            return
        
        self.cvSource.putFrame(img)