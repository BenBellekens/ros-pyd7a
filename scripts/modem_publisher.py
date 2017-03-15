#!/usr/bin/env python

# Copyright (C) 2017
# Ben Bellekens, ben.bellekens@uantwerpen.be

import rospy
import tf
import time
from rospyd7a.msg import dash7
import d7a
from modem.modem import Modem

class modem_listener:
    def __init__(self, name, port, rate, verbose):
        self.name = name
        self.port = port
        self.baudrate = rate
        self.verbose = verbose
        self.modem = None
        self.counter = 1
        self.pub = rospy.Publisher('dash7', dash7, queue_size=1)
        self.pubrate = rospy.Rate(10)
        self.location = []

    def set_location(self, x, y, z):
        self.location = [x, y, z]

    def location_broadcast(self, msg):
        br = tf.TransformBroadcaster()
        br.sendTransform((self.location[0], self.location[1], self.location[2]),
                         tf.transformations.quaternion_from_euler(0.0, 0.0, 0.0, ),
                         msg.header.stamp,
                         self.name,
                         "base_link")

    def received_command_callback(self, cmd):
        print cmd
        if cmd.interface_status != None:
            if cmd.interface_status.operand.interface_id == 215:  # 215 is the interface_id that corresponds to DASH7
                rospy.loginfo("Received Dash7 message")
                message = dash7()
                message = self.parse(message, cmd)
                self.pub.publish(message)
                self.location_broadcast(message)


    def parse(self, message, cmd):
        rospy.loginfo("Parse Dash7 message")
        message.header.stamp    = rospy.Time.now()
        message.header.frame_id = str(cmd.interface_status.operand.interface_status.addressee.id)
        message.rx_address      = str(self.modem.uid)
        message.tx_address      = str(cmd.interface_status.operand.interface_status.addressee.id)
        message.rx_level        = cmd.interface_status.operand.interface_status.rx_level
        message.link_budget     = cmd.interface_status.operand.interface_status.link_budget
        message.channel_band    = cmd.interface_status.operand.interface_status.channel_header.channel_band.name
        message.channel_class   = cmd.interface_status.operand.interface_status.channel_header.channel_class.name
        message.channel_index   = cmd.interface_status.operand.interface_status.channel_index
        message.counter         = self.counter
        self.counter += 1
        return message

    def listen(self):
        rospy.loginfo("Port %s with Baudrate %s", self.port, self.baudrate)
        while True:
            try:
                self.modem = Modem(self.port, self.baudrate, receive_callback=self.received_command_callback, show_logging=self.verbose)
                self.modem.start_reading()
                while not rospy.is_shutdown():
                    pass
            except Exception, e:
                raise e            

if __name__ == '__main__':
    rospy.init_node('d7_rx_node', log_level=rospy.INFO)
    name = rospy.get_name()
    port = rospy.get_param("~dash7_port")
    baudrate = rospy.get_param("~dash7_baudrate")
    x_coor = rospy.get_param("~x_coor")
    y_coor = rospy.get_param("~y_coor")
    z_coor = rospy.get_param("~z_coor")
    #port = "/dev/ttyUSB1"
    #baudrate = 115200
    verbose = True
    try:
        dash7_listener = modem_listener(name, port, baudrate, verbose)
        dash7_listener.set_location(x_coor, y_coor, z_coor)
        dash7_listener.listen()
    except rospy.ROSInterruptException:
        pass
