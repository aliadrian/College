document.addEventListener("DOMContentLoaded", function () {
  const body = document.querySelector("body");
  const pageType = window.location.pathname.includes('account') ? 'account' : 'members';
  console.log(pageType)

  const toggleWrapper = document.createElement("div");
  toggleWrapper.className = "toggle-wrapper";
  toggleWrapper.style.position = "fixed";
  toggleWrapper.style.right = "10px";
  toggleWrapper.style.top = "50%";
  toggleWrapper.style.zIndex = "50";
  toggleWrapper.style.transform = "translateY(-50%)";

  const toggleSwitch = document.createElement("input");
  toggleSwitch.type = "checkbox";
  toggleSwitch.id = "toggleReference";
  toggleSwitch.className = "toggle-switch";
  toggleSwitch.style.display = "none";

  const toggleLabel = document.createElement("label");
  toggleLabel.className = "switch";
  toggleLabel.htmlFor = "toggleReference";
  toggleLabel.style.display = "block";
  toggleLabel.style.width = "20px";
  toggleLabel.style.height = "40px";
  toggleLabel.style.background = "#ccc";
  toggleLabel.style.position = "relative";
  toggleLabel.style.borderRadius = "12px";

  const knob = document.createElement("span");
  knob.className = "slider";
  knob.style.position = "absolute";
  knob.style.top = "0";
  knob.style.left = "0";
  knob.style.width = "20px";
  knob.style.height = "20px";
  knob.style.borderRadius = "50%";
  knob.style.background = "#fff";
  knob.style.transition = "0.4s";

  toggleLabel.appendChild(knob);
  toggleWrapper.appendChild(toggleSwitch);
  toggleWrapper.appendChild(toggleLabel);

  body.appendChild(toggleWrapper);

  toggleSwitch.addEventListener("change", function() {
    if (this.checked) {
      toggleLabel.style.background = "#2196F3";
      knob.style.top = "20px";
    } else {
      toggleLabel.style.background = "#ccc";
      knob.style.top = "0";
    }
  });

  const fetchWidthHeightMap = async () => {
    const response = await fetch(`./control/${pageType}_w_h.json`);
    if (response.ok) {
      return await response.json();
    } else {
      throw new Error(`Failed to load ${pageType} width-height map`);
    }
  };

  const updateBackgroundImage = (widthHeightMap) => {
    const w = window.innerWidth;
    if (w >= 392 && w <= 1600) {
      const h = widthHeightMap[w.toString()];
      if (h) {
        const imagePath = `./control/control_images/${pageType}/${pageType}_ref_${h}_${w}.webp`;
        
        const referenceImage = document.createElement("div");
        referenceImage.className = "reference_image";
        
        referenceImage.style.position = "absolute";
        referenceImage.style.top = "0px";
        referenceImage.style.left = "0px";
        referenceImage.style.zIndex = "20";
        referenceImage.style.width = "100%";
        referenceImage.style.height = `${h}px`;
        referenceImage.style.backgroundImage = `url('${imagePath}')`;
        referenceImage.style.backgroundSize = "cover";
        referenceImage.style.backgroundPosition = "left";
        referenceImage.style.backgroundRepeat = "no-repeat";
        referenceImage.style.opacity = "1";
        
        body.appendChild(referenceImage);
      }
    }
  };

  const applyBackground = (widthHeightMap) => {
    const existingReference = document.querySelector(".reference_image");
    if (existingReference) {
      existingReference.remove();
    }
    if (toggleSwitch.checked) {
      updateBackgroundImage(widthHeightMap);
    }
  };

  const debounce = (func, wait) => {
    let timeout;
    return (...args) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => func.apply(this, args), wait);
    };
  };

  fetchWidthHeightMap()
  .then((widthHeightMap) => {
    const debouncedUpdate = debounce(() => applyBackground(widthHeightMap), 150);
    debouncedUpdate();
    window.addEventListener("resize", debouncedUpdate);
    toggleSwitch.addEventListener("change", debouncedUpdate);
  })
  .catch((error) => {
    console.error(`Failed to load ${pageType} width-height map:`, error);
  });
});
