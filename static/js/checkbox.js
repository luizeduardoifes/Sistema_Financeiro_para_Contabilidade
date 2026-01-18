//Função para checkbox
document.addEventListener("keydown", function (event) {
    if (event.code === "Space") {
        const overlay = document.getElementById("erroOverlay");
        const sucesso = document.getElementById("sucessoOverlay");
        if (overlay) overlay.remove();
        if (sucesso) sucesso.remove();
    }
});