# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/JointSample.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class JointSample(genpy.Message):
  _md5sum = "fe238686c8b329629bd0aa9499404e2e"
  _type = "ff_msgs/JointSample"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Copyright (c) 2017, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# 
# All rights reserved.
# 
# The Astrobee platform is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# JointSample message, based off of rapid::JointSample

# Flag values for joint status. 
# Joint is enabled
uint8 JOINT_ENABLED    = 0      # Joint enabled
uint8 JOINT_DISABLED   = 1      # Joint disabled


# Angle position (in radians) of the joint
float32 angle_pos

# Angle velocity (in radians/sec) of the joint
float32 angle_vel

# Angle acceleration (in radians/sec^2) of the joint (not being used)
float32 angle_acc

# Current draw of joint motor
float32 current

# Torque sensed at the joint (not being used)
float32 torque

# Temperature of the joint (in Celsius)
float32 temperature

# Bit field representing the state of the joint
uint16 status

# Human-readable name
string name
"""
  # Pseudo-constants
  JOINT_ENABLED = 0
  JOINT_DISABLED = 1

  __slots__ = ['angle_pos','angle_vel','angle_acc','current','torque','temperature','status','name']
  _slot_types = ['float32','float32','float32','float32','float32','float32','uint16','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       angle_pos,angle_vel,angle_acc,current,torque,temperature,status,name

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(JointSample, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.angle_pos is None:
        self.angle_pos = 0.
      if self.angle_vel is None:
        self.angle_vel = 0.
      if self.angle_acc is None:
        self.angle_acc = 0.
      if self.current is None:
        self.current = 0.
      if self.torque is None:
        self.torque = 0.
      if self.temperature is None:
        self.temperature = 0.
      if self.status is None:
        self.status = 0
      if self.name is None:
        self.name = ''
    else:
      self.angle_pos = 0.
      self.angle_vel = 0.
      self.angle_acc = 0.
      self.current = 0.
      self.torque = 0.
      self.temperature = 0.
      self.status = 0
      self.name = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6fH().pack(_x.angle_pos, _x.angle_vel, _x.angle_acc, _x.current, _x.torque, _x.temperature, _x.status))
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 26
      (_x.angle_pos, _x.angle_vel, _x.angle_acc, _x.current, _x.torque, _x.temperature, _x.status,) = _get_struct_6fH().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6fH().pack(_x.angle_pos, _x.angle_vel, _x.angle_acc, _x.current, _x.torque, _x.temperature, _x.status))
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 26
      (_x.angle_pos, _x.angle_vel, _x.angle_acc, _x.current, _x.torque, _x.temperature, _x.status,) = _get_struct_6fH().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6fH = None
def _get_struct_6fH():
    global _struct_6fH
    if _struct_6fH is None:
        _struct_6fH = struct.Struct("<6fH")
    return _struct_6fH
