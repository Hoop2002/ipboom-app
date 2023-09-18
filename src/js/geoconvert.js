
$(document).on('click', '.button_form', function(event){
    const keyApi = document.getElementById('keyApi').value;
    const csvFile = document.getElementById('csvFile');
    const file = csvFile.files[0];
    const fileName = file.name
    console.log(file)
    if(keyApi == '' || typeof keyApi == "undefined") {
        alert("API KEY Пуст!")
    }
    else if(typeof file == "undefined"){
        alert("Не выбран файл!");
    }
    else if (file.type != "text/csv"){
        alert("Выбранный файл неправильного формата  (необходим .csv)");
    }
    else{
        const xhr = new XMLHttpRequest();
        const formData = new FormData();

        formData.append('file', file);

        console.log(formData)
        xhr.open('POST', '/file/upload-file');
        xhr.send(formData);
    }

})