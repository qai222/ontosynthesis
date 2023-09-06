from ord_schema.message_helpers import load_message, json_format
from ord_schema.proto import dataset_pb2

dataset = load_message("ord_dataset-0a66204fc43e49c2922e6f9107e6b62f.pb.gz", message_type=dataset_pb2.Dataset)
reaction = dataset.reactions[42]
js = json_format.MessageToJson(reaction, preserving_proto_field_name=True)
with open("test_reaction.json", "w") as f:
    f.write(js)
