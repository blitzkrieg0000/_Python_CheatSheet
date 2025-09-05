import asyncio
import time
from concurrent import futures
from typing import Generator

import grpc
from ray import serve
from ray.serve.config import gRPCOptions

import ray_pb2 as rc

grpc_port = 9000
grpc_servicer_functions = [
    "ray_pb2_grpc.add_UserDefinedServiceServicer_to_server",
    "ray_pb2_grpc.add_ImageClassificationServiceServicer_to_server",
]
serve.start(
    grpc_options=gRPCOptions(
        port=grpc_port,
        grpc_servicer_functions=grpc_servicer_functions
    )
)


@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.4, "num_gpus": 1})
class GrpcDeployment():
	def __call__(self, user_message: rc.UserDefinedMessage) -> rc.UserDefinedResponse:
		greeting = f"Hello {user_message.name} from {user_message.origin}"
		num = user_message.num * 2
		user_response = rc.UserDefinedResponse(
			greeting=greeting,
			num=num,
		)
		return user_response


	@serve.multiplexed(max_num_models_per_replica=1)
	async def get_model(self, model_id: str) -> str:
		return f"loading model: {model_id}"


	async def Multiplexing(self, user_message: rc.UserDefinedMessage2) -> rc.UserDefinedResponse2:
		model_id = serve.get_multiplexed_model_id()
		model = await self.get_model(model_id)
		user_response = rc.UserDefinedResponse2(
			greeting=f"Method2 called model, {model}",
		)
		return user_response


	def Streaming(self, user_message: rc.UserDefinedMessage) -> Generator[rc.UserDefinedResponse, None, None]:
		for i in range(10):
			greeting = f"{i}: Hello {user_message.name} from {user_message.origin}"
			num = user_message.num * 2 + i
			user_response = rc.UserDefinedResponse(
				greeting=greeting,
				num=num,
			)
			yield user_response

			time.sleep(0.1)


app = GrpcDeployment.bind()

app1 = "app1"
serve.run(target=app, name=app1, route_prefix=f"/{app1}")

asyncio.get_event_loop().run_forever()


#? Diğer başlatma yöntemleri:
# =================================================================================================================== #
#! 1-) Config File                                                                                                    #
# =================================================================================================================== #
"""
    # config.yml
    grpc_options:
    port: 9000
    grpc_servicer_functions:
        - ray_pb2_grpc.add_UserDefinedServiceServicer_to_server
        - ray_pb2_grpc.add_ImageClassificationServiceServicer_to_server

    applications:
    - name: app1
        route_prefix: /app1
        import_path: RayDeployment:app
        runtime_env: {}
"""
"""
    $ serve run config.yml
"""


# =================================================================================================================== #
#! 2-) CLI                                                                                                            #
# =================================================================================================================== #
"""
    $ ray start --head
        serve start \
            --grpc-port 9000 \
            --grpc-servicer-functions ray_pb2_grpc.add_UserDefinedServiceServicer_to_server \
            --grpc-servicer-functions ray_pb2_grpc.add_ImageClassificationServiceServicer_to_server
"""