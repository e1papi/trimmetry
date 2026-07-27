(() => {
  const script = Array.from(document.scripts).find((item) =>
    new URL(item.src).pathname.endsWith("/_static/language-switcher.js")
  );
  if (!script) return;

  const currentLanguage =
    document.documentElement.lang.toLowerCase().startsWith("ru") ? "ru" : "en";
  const currentBuildRoot = new URL("../", script.src);
  const siteRoot =
    currentLanguage === "ru" ? new URL("../", currentBuildRoot) : currentBuildRoot;
  const currentUrl = new URL(window.location.href);
  const relativePage = currentUrl.pathname.slice(currentBuildRoot.pathname.length);

  const targetFor = (language) => {
    const targetRoot =
      language === "ru" ? new URL("ru/", siteRoot) : new URL("./", siteRoot);
    const target = new URL(relativePage || "index.html", targetRoot);
    target.search = currentUrl.search;
    target.hash = currentUrl.hash;
    return target.href;
  };

  const wrapper = document.createElement("div");
  wrapper.className = "trimmetry-language-switcher";

  const select = document.createElement("select");
  select.className = "form-select form-select-sm";
  select.setAttribute(
    "aria-label",
    currentLanguage === "ru" ? "Выбор языка" : "Select language"
  );

  [
    ["en", "English"],
    ["ru", "Русский"],
  ].forEach(([value, label]) => {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    option.selected = value === currentLanguage;
    select.appendChild(option);
  });

  select.addEventListener("change", () => {
    window.location.assign(targetFor(select.value));
  });

  wrapper.appendChild(select);

  const navbarEnd = document.querySelector(".navbar-header-items__end");
  if (!navbarEnd) return;
  const themeSwitcher = navbarEnd.querySelector(".theme-switch-container");
  navbarEnd.insertBefore(wrapper, themeSwitcher);
})();
