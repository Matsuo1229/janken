Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> export default {
  async fetch(request) {

    if (request.headers.get("Upgrade") !== "websocket") {
      return new Response("WebSocket Server");
    }

    const pair = new WebSocketPair();
    const client = pair[0];
    const server = pair[1];

    server.accept();

    server.addEventListener("message", event => {
        server.send(event.data);
    });

    return new Response(null, {
      status:101,
      webSocket:client
    });
  }
}