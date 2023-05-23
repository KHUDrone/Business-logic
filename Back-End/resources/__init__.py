def create_socketio(sock):
    from .ws_ns import ChatNamespace
    sock.on_namespace(ChatNamespace('/realtime'))


