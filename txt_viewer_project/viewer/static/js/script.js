function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
  const txtSelect = document.getElementById("txtSelect");
  const viewBtn = document.getElementById("viewBtn");

  txtSelect.addEventListener("change", function () {
    viewBtn.disabled = this.value === "";
  });

  viewBtn.addEventListener("click", function () {
    const selectedFile = txtSelect.value;
    fetch("/check_file/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken")
      },
      body: JSON.stringify({ filename: selectedFile })
    })
      .then(response => response.json())
      .then(data => {
        if (!data.exists) {
          const modal = new bootstrap.Modal(document.getElementById("fileNotFoundModal"));
          document.getElementById("downloadLink").href = data.download_url;
          modal.show();
        }
      });
  });
});
