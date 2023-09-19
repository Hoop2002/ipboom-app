
$(document).on('click', '.button_form', function(event){
    const keyApi = document.getElementById('keyApi');
    const csvFile = document.getElementById('csvFile');
    if(keyApi.value == '' || typeof keyApi.value == "undefined") {
        alert("API KEY Пуст!")
        window.stop()
    }
     if(typeof csvFile.files[0] == "undefined"){
        alert("Не выбран файл!");
        window.stop()
    }

    const file = csvFile.files[0];
    const fileName = file.name
    console.log(keyApi)
   
    if (file.type != "text/csv"){
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