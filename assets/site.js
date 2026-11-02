// Language toggle (FR default; ?lang=en in the URL forces English) and mobile menu.
(function () {
  var root = document.documentElement;
  var param = new URLSearchParams(window.location.search).get("lang");
  var saved = null;
  try { saved = localStorage.getItem("lang"); } catch (e) {}
  var lang = param === "en" || param === "fr" ? param : (saved || "fr");
  function apply(l) {
    root.setAttribute("data-lang", l);
    root.setAttribute("lang", l);
    var b = document.getElementById("lang");
    if (b) b.textContent = l === "fr" ? "EN" : "FR";
    try { localStorage.setItem("lang", l); } catch (e) {}
  }
  apply(lang);
  document.addEventListener("DOMContentLoaded", function () {
    apply(root.getAttribute("data-lang"));
    var b = document.getElementById("lang");
    if (b) b.addEventListener("click", function () { apply(root.getAttribute("data-lang") === "fr" ? "en" : "fr"); });
    var m = document.getElementById("burger"), n = document.getElementById("nav");
    if (m && n) m.addEventListener("click", function () { n.classList.toggle("open"); });
  });
})();
