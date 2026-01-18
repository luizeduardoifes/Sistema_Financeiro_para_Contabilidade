document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("meuFormulario");
    const campos = form.querySelectorAll("input, button");

    campos.forEach((campo, index) => {
        campo.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                e.preventDefault(); // impede envio automático

                const proximo = campos[index + 1];
                if (proximo) {
                    proximo.focus();
                }
            }
        });
    });
});