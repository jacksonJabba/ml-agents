# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communicator/python_to_unity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from communicator import python_parameters_pb2 as communicator_dot_python__parameters__pb2
from communicator import academy_parameters_pb2 as communicator_dot_academy__parameters__pb2
from communicator import unity_input_pb2 as communicator_dot_unity__input__pb2
from communicator import unity_output_pb2 as communicator_dot_unity__output__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='communicator/python_to_unity.proto',
  package='communicator',
  syntax='proto3',
  serialized_pb=_b('\n\"communicator/python_to_unity.proto\x12\x0c\x63ommunicator\x1a$communicator/python_parameters.proto\x1a%communicator/academy_parameters.proto\x1a\x1e\x63ommunicator/unity_input.proto\x1a\x1f\x63ommunicator/unity_output.proto2\x9f\x01\n\rPythonToUnity\x12O\n\nInitialize\x12\x1e.communicator.PythonParameters\x1a\x1f.communicator.AcademyParameters\"\x00\x12=\n\x04Send\x12\x18.communicator.UnityInput\x1a\x19.communicator.UnityOutput\"\x00\x42\x18\xaa\x02\x15MLAgents.Communicatorb\x06proto3')
  ,
  dependencies=[communicator_dot_python__parameters__pb2.DESCRIPTOR,communicator_dot_academy__parameters__pb2.DESCRIPTOR,communicator_dot_unity__input__pb2.DESCRIPTOR,communicator_dot_unity__output__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\025MLAgents.Communicator'))

_PYTHONTOUNITY = _descriptor.ServiceDescriptor(
  name='PythonToUnity',
  full_name='communicator.PythonToUnity',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=195,
  serialized_end=354,
  methods=[
  _descriptor.MethodDescriptor(
    name='Initialize',
    full_name='communicator.PythonToUnity.Initialize',
    index=0,
    containing_service=None,
    input_type=communicator_dot_python__parameters__pb2._PYTHONPARAMETERS,
    output_type=communicator_dot_academy__parameters__pb2._ACADEMYPARAMETERS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='communicator.PythonToUnity.Send',
    index=1,
    containing_service=None,
    input_type=communicator_dot_unity__input__pb2._UNITYINPUT,
    output_type=communicator_dot_unity__output__pb2._UNITYOUTPUT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PYTHONTOUNITY)

DESCRIPTOR.services_by_name['PythonToUnity'] = _PYTHONTOUNITY

# @@protoc_insertion_point(module_scope)