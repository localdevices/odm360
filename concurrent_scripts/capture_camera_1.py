from datetime import datetime
import subprocess, sys

camera_id = "camera_1/"
save_dir = "/home/pi/cm360/images/" + camera_id

port = str(sys.argv[2])
image_name = "image_" + str(sys.argv[1]) + ".jpg"
save_location = save_dir + image_name

before_time = datetime.now()

subprocess.call(["gphoto2", "--capture-image-and-download", "--port", port, "--filename", save_location])

after_time = datetime.now()
print("Camera {}: {}".format(1, (after_time - before_time).total_seconds()))
