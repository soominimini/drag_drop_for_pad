from flask import Flask, render_template, redirect, url_for, session
from flask_socketio import SocketIO, emit, join_room
import time
import threading

# import rospy
# from std_msgs.msg import String
# from qt_robot_interface.srv import *
# from qt_gesture_controller.srv import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('first_talk')
def first_talk_robot(msg):
    print(str(msg))
    # talktext_pub.publish("I want "+msg)

@socketio.on('giveme_talk')
def giveme_talk_robot(msg):
    print(str(msg))
    # rospy.sleep(1.0)
    # talktext_pub.publish("Can you give me "+msg+"?")


@socketio.on('object_list')
def correct_answer(obj):
    # rospy.sleep(1.0)
    print(str(obj))

@socketio.on('correct')
def correct_answer(obj):
    # rospy.sleep(1.0)
    # talktext_pub.publish("Good job")
    print(str(obj))


@socketio.on('wrong')
def score_handle_from_html(data):
    # talktext_pub.publish("Try again!")
    print(str(data))


@socketio.on('block_page')
def block_page_redirect(msg):
    # rospy.sleep(1.0)
    # talktext_pub.publish(msg)
    print(str(msg))


@socketio.on('connect event')
def test_connect(message):
    print(message)


@socketio.on('disconnect')
def test_connect(message):
    print("disconnected")


@app.route('/')
def taking_instruction():
    return render_template('home.html')


@app.route('/first_page')
def taking_instruction1():
    # rospy.sleep(1.0)
    # talktext_pub.publish("I want fruits!")
    return render_template('index_taking_instruction.html')


@app.route('/second_page')
def taking_instruction2():
    return render_template('index_taking_instruction_page2.html')


@app.route('/third_page')
def taking_instruction3():
    return render_template('index_taking_instruction_page3.html')


if __name__ == '__main__':
    # rospy.init_node('taking_instruction_node')
    # rospy.loginfo("taking_instruction started!")

    global t1
    t1 = time.time()
    # creating a ros publisher
    # speechSay_pub = rospy.Publisher('/qt_robot/speech/say', String, queue_size=10)
    # talktext_pub = rospy.Publisher('/qt_robot/behavior/talkText', String, queue_size=10)
    socketio.run(app, host='0.0.0.0', debug=True)
