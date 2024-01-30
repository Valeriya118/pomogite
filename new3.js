document.querySelector('.add-to-cart-button').addEventListener('click', function() {
  const planetName = document.querySelector('.planet-name').textContent;
  const planetImage = document.querySelector('.planet-image').src;

  const urlParams = new URLSearchParams({
    planet: planetName,
    image: planetImage
  });

  window.location.href = `page16.html?${urlParams.toString()}`;
});