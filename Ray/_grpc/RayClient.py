import grpc
from ray_pb2_grpc import UserDefinedServiceStub
from ray_pb2 import UserDefinedMessage


channel = grpc.insecure_channel("127.0.0.1:9000")
stub = UserDefinedServiceStub(channel)
request = UserDefinedMessage(name="foo", num=30, origin="bar")

response, call = stub.__call__.with_call(request=request)
print(f"status code: {call.code()}")  # grpc.StatusCode.OK
print(f"greeting: {response.greeting}")  # "Hello foo from bar"
print(f"num: {response.num}")  # 60