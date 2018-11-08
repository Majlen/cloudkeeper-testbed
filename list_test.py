import grpc
import pytest

from protos import cloudkeeper_pb2, cloudkeeper_pb2_grpc

stub = None

def setup_module():
	global stub
	channel = grpc.insecure_channel('127.0.0.1:50051')
	stub = cloudkeeper_pb2_grpc.CommunicatorStub(channel)

def test_list():
	images = stub.ImageLists(cloudkeeper_pb2.Empty())
	count = 0
	for image in images:
		count += 1
	assert count == 0

def test_conn():
	images = stub.ImageLists(cloudkeeper_pb2.Empty())
	count = 0
	with pytest.raises(grpc.RpcError):
		for image in images:
			count += 1

if __name__ == '__main__':
	setup_module()
	test_list()
