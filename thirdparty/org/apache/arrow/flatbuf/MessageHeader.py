# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

# /// ----------------------------------------------------------------------
# /// The root Message type
# /// This union enables us to easily send different message types without
# /// redundant storage, and in the future we can easily add new message types.
# ///
# /// Arrow implementations do not need to implement all of the message types,
# /// which may include experimental metadata types. For maximum compatibility,
# /// it is best to send data using RecordBatch
class MessageHeader(object):
    NONE = 0
    Schema = 1
    DictionaryBatch = 2
    RecordBatch = 3
    Tensor = 4
