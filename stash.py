import grpc

from protos import cloudkeeper_pb2, cloudkeeper_pb2_grpc

stub = None

def setup_module():
	global stub
	channel = grpc.insecure_channel('localhost:50051')
	stub = cloudkeeper_pb2_grpc.CommunicatorStub(channel)

def test_list():
	images = stub.ImageLists(cloudkeeper_pb2.Empty())
	print(type(images))
	for image in images:
		print(image.image_list_identifier)

#def run():
#	with grpc.insecure_channel('localhost:50051') as channel:
#		stub = cloudkeeper_pb2_grpc.CommunicatorStub(channel)
#
#		image = cloudkeeper_pb2.Image(
#				mode = cloudkeeper_pb2.Image.LOCAL,
#				location = "a",
#				format = cloudkeeper_pb2.Image.RAW,
#				uri = "test",
#				checksum = "blabla",
#				size = 510000,
#				username = "test",
#				password = "test",
#				digest = "blabla")
#
#		appliance = cloudkeeper_pb2.Appliance(
#				identifier = "test",
#				title = "test",
#				description = "test",
#				mpuri = "test",
#				group = "test",
#				ram = 512000,
#				core = 4,
#				version = "1",
#				architecture = "amd64",
#				operating_system = "linux",
#				vo = "bla",
#				expiration_date = 1234567891231,
#				image_list_identifier = "bla",
#				base_mpuri = "testX",
#				appid = "yyy",
#				digest = "blable",
#				image = image)
#
#		f = open("test", "wb")
#		f.write(appliance.SerializeToString())
#		f.close()
#
#		stub.AddAppliance(appliance)
#
#		for image in stub.ImageLists(cloudkeeper_pb2.Empty()):
#			print(image.image_list_identifier)

if __name__ == '__main__':
	setup_module()
	test_list()
