function deleteSong(songId) {
  fetch("/delete-song", {
    method: "POST",
    body: JSON.stringify({ songId: songId }),
  }).then((_res) => {
    window.location.href = "/my_library";
  });
};

function redirectToPage(path) {
    window.location.href = path;
}
