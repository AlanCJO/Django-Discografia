function alerta(event) {
    event.preventDefault();

    const link = event.target.href
    const linkLength = link.length
    const idMusica = link[linkLength - 2]

    alertaDoce(link); // kkkkkkkkkk (estava dando conflito colocando o nome da biblioteca na função, então vai em br mesmo)
}

function alertaDoce(link) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-danger',
            cancelButton: 'btn btn-success'
        },
        buttonsStyling: false
    })

    swalWithBootstrapButtons.fire({
        title: 'Você tem certeza??',
        text: "Você não poderá reverter isso!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, deletar música!',
        cancelButtonText: 'Não, cancelar!',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            swalWithBootstrapButtons.fire(
                'Deletado!',
                'Sua música foi removida da playlist!',
                'success'
            );

            // Se confirmar direcionar para a rota que chama a view de exclusão
            setTimeout(() => {
                window.location.href = link
            }, 1000);

        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire(
                'Cancelado',
                'Sua música está segura :)',
                'error'
            );
        }
    })
}