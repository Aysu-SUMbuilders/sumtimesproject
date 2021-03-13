#coding: utf8
import math
import rospy
from pyzbar import pyzbar
from clover import srv
from std_srvs.srv import Trigger
#from sensor_msgs.msg import Range
from clover.srv import SetLEDEffect
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()

rospy.init_node('barcode_test')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=1, yaw=0, speed=2, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

dist = 0   
def range_callback(msg):
    global dist
    dist = msg.range 
    
def check_height():
    global height
    telem = get_telemetry("aruco_map")
    height = telem.z - dist
    print(height)


# Image subscriber callback function
qr = ""
def image_callback(data):
    global qr
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    barcodes = pyzbar.decode(cv_image)
    for barcode in barcodes:
        qr = barcode.data.encode("utf-8")

image_sub = rospy.Subscriber('main_camera/image_raw_throttled', Image, image_callback, queue_size=1)
navigate_wait(frame_id="body", auto_arm = True)

navigate_wait(7, 0, 1)
while qr == "":
    rospy.sleep(0.2)
       
qr_data = qr.split(' ')
print(qr_data)

class Ickiler:
  def __init__(self, kalori):
    self.kalori = kalori

ayran = Ickiler(40)
adi_cay = Ickiler(50)
sirin_cay = Ickiler(60)
alma_siresi = Ickiler(45)
qazli_ickiler = Ickiler(50)
yerkoku_siresi = Ickiler(28)
bir_fincan_qehve = Ickiler(44)
kola_33_cc = Ickiler(42)
nescafe = Ickiler(32)
portagal_siresi = Ickiler(24)
portagal_siresi_konsent = Ickiler(24)
soda = Ickiler(45)
uzum_siresi = Ickiler(74)
albali_suyu_konsent = Ickiler(21)

t = 0

for e in qr_data:
    if e == 'ayran':
        t += ayran.kalori 
      
    if e == 'adi_cay':
      
        t += ayran.kalori 
    if e == 'sirin_cay':
  
        t += ayran.kalori 
 
    if e == 'alma_siresi':
       
        t += ayran.kalori 
    if e == 'qazli_ickiler':
       
        t = ayran.kalori 
    if e == 'yerkoku_siresi':
       
        t += ayran.kalori 
    if e == 'bir_fincan_qehve':
        
        t += ayran.kalori 
    if e == 'kola_33_cc':
        
        t += ayran.kalori 
    if e == 'nescafe':
        
        t += ayran.kalori 
    if e == 'portagal_siresi':
       
        t += ayran.kalori 
    if e == 'portagal_siresi_konsent':
        
        t += ayran.kalori
    if e == 'soda':
       
        t += ayran.kalori 
    if e == 'uzum_siresi':
    
        t += ayran.kalori
    if e == 'albali_suyu_konsent':
        
        t += ayran.kalori 
print(t)  
navigate_wait(0, 0, 0)  