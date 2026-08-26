// Запрос к своему же адресу: edge раздаёт бандл из S3, а /api/* уводит в контейнер.
const el = document.getElementById("api");
fetch("/api/hello")
  .then((r) => r.json())
  .then((j) => { el.textContent = "API: " + j.message; })
  .catch((e) => { el.textContent = "API недоступен: " + e; });
