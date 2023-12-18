function deleteSong(songId) {
  fetch("/delete-song", {
    method: "POST",
    body: JSON.stringify({ songId: songId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
