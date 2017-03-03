#!/usr/bin/env python

# Copyright (C) 2017
# Ben Bellekens, ben.bellekens@uantwerpen.be

import rospy
import time
from std_msgs.msg import String
from rospyd7a.msg import dash7
import d7a
from modem.modem import Modem

class modem_listener:
    def __init__(self, port, rate, verbose):
        self.port = port
        self.rate = rate
        self.verbose = verbose
        self.modem = None

    def received_command_callback(self, cmd):
        print cmd
        if cmd.interface_status != None:
            if cmd.interface_status.operand.interface_id == 215:  # 215 is the interface_id that corresponds to DASH7
                rospy.loginfo("interface-id")
                message = dash7()
                message.header.stamp = rospy.Time.now()
                message.rx_address = cmd.interface_status.operand.interface_id.addressee.id
                message.tx_address = self.modem.uid

    def listen(self):
        rospy.loginfo("port %s with baudrate %s", self.port, self.rate)
        self.modem = Modem(self.port, self.rate, receive_callback=self.received_command_callback, show_logging=verbose)
        self.modem.start_reading()
        while not rospy.is_shutdown():
            pass


if __name__ == '__main__':
    rospy.init_node('modem_publisher', log_level=rospy.INFO)
    # port = rospy.get_param("~dash7_port")
    # baudrate = rospy.get_param("~dash7_baudrate")
    port = "/dev/ttyUSB0"
    baudrate = 115200
    verbose = True
    try:
        dash7_listener = modem_listener(port, baudrate, verbose)
        dash7_listener.listen()
    except rospy.ROSInterruptException:
        pass
