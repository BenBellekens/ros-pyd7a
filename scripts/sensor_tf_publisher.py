#!/usr/bin/env python  


# Copyright (C) 2017
# Ben Bellekens, ben.bellekens@uantwerpen.be

import roslib
import rospy
import tf
from rospyd7a.msg import dash7

node_1 = []
node_2 = []
node_3 = []
node_4 = []
node_5 = []
node_6 = []

def tf_broadcast_cb(data):
    br = tf.TransformBroadcaster()
    rospy.loginfo(data.tx_address)    
    rospy.loginfo(node_1[0])
    #receiving_frame = rospy.get_param('~receiving_frame')
    receiving_frame = "base_link"
    if len(node_1) > 0:
        if str(data.tx_address) == str(node_1[0]):
            rospy.loginfo('sendTF node_1')
            br.sendTransform((node_1[1], node_1[2], node_1[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_2) > 0:
        if str(data.tx_address) == str(node_2[0]):
            rospy.loginfo('sendTF node_2')
            br.sendTransform((node_2[1], node_2[2], node_2[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_3) > 0:
        if str(data.tx_address) == str(node_3[0]):
            br.sendTransform((node_3[1], node_3[2], node_3[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_4) > 0:
        if str(data.tx_address) == str(node_4[0]):
            br.sendTransform((node_4[1], node_4[2], node_4[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_5) > 0:
        if str(data.tx_address) == str(node_5[0]) and len(node_5) > 0:
            br.sendTransform((node_5[1], node_5[2], node_5[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_6) >0:
        if str(data.tx_address) == str(node_6[0]) and len(node_6) > 0:
            br.sendTransform((node_6[1], node_6[2], node_6[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_7) >0:
        if str(data.tx_address) == str(node_7[0]) and len(node_7) > 0:
            br.sendTransform((node_7[1], node_7[2], node_7[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_8) >0:
        if str(data.tx_address) == str(node_8[0]) and len(node_8) > 0:
            br.sendTransform((node_8[1], node_8[2], node_8[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_9) >0:
        if str(data.tx_address) == str(node_9[0]) and len(node_9) > 0:
            br.sendTransform((node_9[1], node_9[2], node_9[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    elif len(node_10) >0:
        if str(data.tx_address) == str(node_10[0]) and len(node_10) > 0:
            br.sendTransform((node_10[1], node_10[2], node_10[3]),
                                 (0.0, 0.0, 0.0, 1.0),
                                 rospy.Time.now(),
                                 data.header.frame_id,
                                 receiving_frame)
    else:
        rospy.logerr('ERROR frame_id is not known')

if __name__ == '__main__':
    rospy.init_node('rf_tf_broadcaster', log_level=rospy.DEBUG)
    rospy.loginfo('read rosparam')

    if rospy.has_param('~id_1'):
        id_1_name = rospy.get_param('~id_1')
        id_1_x = rospy.get_param('~id_1_x')
        id_1_y = rospy.get_param('~id_1_y')
        id_1_z = rospy.get_param('~id_1_z')
        node_1 = [id_1_name, id_1_x, id_1_y, id_1_z]

    elif rospy.has_param('~id_2'):    
        id_2_name = rospy.get_param('~id_2')
        id_2_x = rospy.get_param('~id_2_x')
        id_2_y = rospy.get_param('~id_2_y')
        id_2_z = rospy.get_param('~id_2_z')
        node_2 = [id_2_name, id_2_x, id_2_y, id_2_z]

    elif rospy.has_param('~id_3'):
        id_3_name = rospy.get_param('~id_3')
        id_3_x = rospy.get_param('~id_3_x')
        id_3_y = rospy.get_param('~id_3_y')
        id_3_z = rospy.get_param('~id_3_z')
        node_3 = [id_3_name, id_3_x, id_3_y, id_3_z]

    elif rospy.has_param('~id_4'):        
        id_4_name = rospy.get_param('~id_4')
        id_4_x = rospy.get_param('~id_4_x')
        id_4_y = rospy.get_param('~id_4_y')
        id_4_z = rospy.get_param('~id_4_z')
        node_4 = [id_4_name, id_4_x, id_4_y, id_4_z]

    elif rospy.has_param('~id_5'):
        id_5_name = rospy.get_param('~id_5')
        id_5_x = rospy.get_param('~id_5_x')
        id_5_y = rospy.get_param('~id_5_y')
        id_5_z = rospy.get_param('~id_5_z')
        node_5 = [id_5_name, id_5_x, id_5_y, id_5_z]

    elif rospy.has_param('~id_6'):
        id_6_name = rospy.get_param('~id_6')
        id_6_x = rospy.get_param('~id_6_x')
        id_6_y = rospy.get_param('~id_6_y')
        id_6_z = rospy.get_param('~id_6_z')
        node_6 = [id_6_name, id_6_x, id_6_y, id_6_z]

    elif rospy.has_param('~id_7'):
        id_7_name = rospy.get_param('~id_7')
        id_7_x = rospy.get_param('~id_7_x')
        id_7_y = rospy.get_param('~id_7_y')
        id_7_z = rospy.get_param('~id_7_z')
        node_7 = [id_7_name, id_7_x, id_7_y, id_7_z]

    elif rospy.has_param('~id_8'):
        id_8_name = rospy.get_param('~id_8')
        id_8_x = rospy.get_param('~id_8_x')
        id_8_y = rospy.get_param('~id_8_y')
        id_8_z = rospy.get_param('~id_8_z')
        node_8 = [id_8_name, id_8_x, id_8_y, id_8_z]

    elif rospy.has_param('~id_9'):
        id_9_name = rospy.get_param('~id_9')
        id_9_x = rospy.get_param('~id_9_x')
        id_9_y = rospy.get_param('~id_9_y')
        id_9_z = rospy.get_param('~id_9_z')
        node_9 = [id_9_name, id_9_x, id_9_y, id_9_z]

    elif rospy.has_param('~id_10'):
        id_10_name = rospy.get_param('~id_10')
        id_10_x = rospy.get_param('~id_10_x')
        id_10_y = rospy.get_param('~id_10_y')
        id_10_z = rospy.get_param('~id_10_z')
        node_10 = [id_10_name, id_10_x, id_10_y, id_10_z]

    rospy.Subscriber('dash7', dash7, tf_broadcast_cb)
    rospy.spin()