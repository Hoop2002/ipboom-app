
$(document).on('click', '.button_form', function(event){
    const keyApi = document.getElementById('keyApi');
    const csvFile = document.getElementById('csvFile');
    const file = csvFile.files[0];
    const fileName = file.name

    if(keyApi == '' || typeof keyApi == "undefined") {
        alert("API KEY Пуст!")
    }
     if(typeof file == "undefined"){
        alert("Не выбран файл!");
    }
    else if (file.type != "text/csv"){
        alert("Выбранный файл неправильного формата  (необходим .csv)");
    }
    else{
         
        const formData = new FormData();

        formData.append('file', file)
        
        
        fetch(`/geoconvert?key=${keyApi.value}`, {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(
          data => {
            var link = document.createElement("a");
            link.setAttribute('href', `../file/geoconvert/${data.file_path}`)
            link.setAttribute('download','download');
            onload=link.click();
        }
        ).catch(error => {
            console.log(error)
        });
    }

})