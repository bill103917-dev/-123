export default {
  async fetch(request, env) {
    let url = new URL(request.url);
    url.hostname = "disecord-bot2-u3z3.onrender.com"; // 只填域名

    return fetch(url.toString(), {
      method: request.method,
      headers: request.headers,
      body: request.body,
      redirect: 'manual'
    });
  }
};