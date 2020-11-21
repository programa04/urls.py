var quill = new Quill('#editor', {
    modules: {
        toolbar: [
            [{ size: ['small', false, 'large', 'huge'] }],  // custom dropdown
            [{ 'font': [] }],
            ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
            [{ 'align': [] }],
            [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
            [{ 'list': 'ordered'}, { 'list': 'bullet' }],
            ['blockquote','image','video', 'code-block'],
            [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
            [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
            ['link'],
            ['clean']           
        ]
    },
    theme: 'snow'
});
function PegaTexto(){
    let text = quill.getText();
    let TextoHtml = document.getElementsByClassName('ql-editor')
    let Input = document.getElementById("id_ConteudoClausula")
    Input.value = TextoHtml[0].innerHTML

    if (TextoHtml[0].innerHTML=='<p><br></p>') {
        alert("Escreva algo.");
    }else {
        $( "#Form_2" ).submit();
        alert("Salvo");
    }
    
};