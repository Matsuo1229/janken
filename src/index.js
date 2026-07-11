export { GameRoom }

export default {
  async fetch(request, env) {

    const id = env.GAME_ROOM.idFromName("main");
    const stub = env.GAME_ROOM.get(id);

    return stub.fetch(request);
  }
}
