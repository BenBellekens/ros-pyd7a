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
    rospy.loginfo('test %s', data.tx_address)    
    #receiving_frame = rospy.get_param('~receiving_frame')
    receiving_frame = "base_link"
    rospy.loginfo('hallo')
    rospy.loginfo(node_1[0])

    if data.tx_address == node_1[0]:
        br.sendTransform((node_1[1], node_1[2], node_1[3]),
                             (0.0, 0.0, 0.0, 1.0),
                             rospy.Time.now(),
                             data.header.frame_id,
                             receiving_frame)
    # elif data.tx_address == node_2[0]:
    #     br.sendTransform((node_2[1], node_2[2], node_2[3]),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          data.header.frame_id,
    #                          receiving_frame)
    # elif data.tx_address == node_3[0]:
    #     br.sendTransform((node_3[1], node_3[2], node_3[3]),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          data.header.frame_id,
    #                          receiving_frame)
    # elif data.tx_address == node_4[0]:
    #     br.sendTransform((node_4[1], node_4[2], node_4[3]),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          data.header.frame_id,
    #                          receiving_frame)
    # elif data.tx_address == node_5[0]:
    #     br.sendTransform((node_5[1], node_5[2], node_5[3]),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          data.header.frame_id,
    #                          receiving_frame)
    # elif data.tx_address == node_6[0]:
    #     br.sendTransform((node_6[1], node_6[2], node_6[3]),
    #                          (0.0, 0.0, 0.0, 1.0),
    #                          rospy.Time.now(),
    #                          data.header.frame_id,
    #                          receiving_frame)
    else:
        rospy.logerr('ERROR frame_id is not known')

if __name__ == '__main__':
    rospy.init_node('rf_tf_broadcaster', log_level=rospy.DEBUG)
    rospy.loginfo('read rosparam')

    #id_1_name = rospy.get_param('~id_1')
    id_1_name = 3191882256028378
    # id_1_x = rospy.get_param('~id_1_x')
    # id_1_y = rospy.get_param('~id_1_y')
    # id_1_z = rospy.get_param('~id_1_z')
    node_1 = [id_1_name, 5.0, 0.0, 0.0]

    # id_2_name = rospy.get_param('~id_2')
    # id_2_x = rospy.get_param('~id_2_x')
    # id_2_y = rospy.get_param('~id_2_y')
    # id_2_z = rospy.get_param('~id_2_z')
    # node_2 = [id_2_name, id_2_x, id_2_y, id_2_z]

    # id_3_name = rospy.get_param('~id_3')
    # id_3_x = rospy.get_param('~id_3_x')
    # id_3_y = rospy.get_param('~id_3_y')
    # id_3_z = rospy.get_param('~id_3_z')
    # node_3 = [id_3_name, id_3_x, id_3_y, id_3_z]

    # id_4_name = rospy.get_param('~id_4')
    # id_4_x = rospy.get_param('~id_4_x')
    # id_4_y = rospy.get_param('~id_4_y')
    # id_4_z = rospy.get_param('~id_4_z')
    # node_4 = [id_4_name, id_4_x, id_4_y, id_4_z]

    # id_5_name = rospy.get_param('~id_5')
    # id_5_x = rospy.get_param('~id_5_x')
    # id_5_y = rospy.get_param('~id_5_y')
    # id_5_z = rospy.get_param('~id_5_z')
    # node_5 = [id_5_name, id_5_x, id_5_y, id_5_z]

    # id_6_name = rospy.get_param('~id_6')
    # id_6_x = rospy.get_param('~id_6_x')
    # id_6_y = rospy.get_param('~id_6_y')
    # id_6_z = rospy.get_param('~id_6_z')
    # node_6 = [id_6_name, id_6_x, id_6_y, id_6_z]

    rospy.Subscriber('dash7', dash7, tf_broadcast_cb)
    rospy.spin()