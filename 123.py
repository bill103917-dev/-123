export default {
  async fetch(request, env) {
    // 你的原始伺服器（Railway/Render/其他）
    let url = new URL(request.url);
    url.hostname = "https://disecord-bot2-u3z3.onrender.com";  // 換成你的服務域名
    return fetch(url, request);
  }
};