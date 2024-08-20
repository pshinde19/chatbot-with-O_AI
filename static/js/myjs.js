var sendbtn=document.getElementById('sendbtn')
var chatbox=document.getElementById('chatbox-main-ul')
var textareainp=document.getElementById('textareainp')
var div_counter=0

function getanswer(){
    var userinput=textareainp.value.trim()
    // console.log( $('#selct-table').val());
    var table_selected=$('#selct-table').val().trim()
    if(userinput != ''){
        getque(userinput)
        var formdata = new FormData();
        formdata.append('que', userinput);
        formdata.append('tablename',table_selected)
        if(table_selected != ''){
            $.ajax({
                type: 'POST',
                url: '/getanswer',
                data: formdata,
                processData: false, // Important for FormData
                contentType: false,
                success: function(response) {
                    console.log(response);
                    document.getElementById('myloader').remove()
                    if(response.msg =='success'){
                        getresponse(response.result)
                    }else if(response.msg =='error'){
                        var lastresp="#bot-response"+ div_counter
                        if(response.error != ''){
                            $(lastresp).append(`<div class="response" style="display:block;">${response.error}</div>` )
                        }
                        div_counter+=1
                    }
                },
                error: function(error) {
                    // Handle error error.statusText
                    console.log(error);
                    document.getElementById('myloader').remove()
                    var lastresp="#bot-response"+ div_counter
                    $(lastresp).append(`<div class="response" style="display:block;color:red;width: 100%;">${error.statusText}</div>` )
                    div_counter+=1
                }
            });
        }else{
            document.getElementById('myloader').remove()
            var lastresp="#bot-response"+ div_counter
            $(lastresp).append(`<div class="response" style="display:block;color:red;width: 100%;">No table selected....</div>` )
            div_counter+=1
        }
       
    }else{
        console.log('empty msg');
        
    }
}

function getque(userinput){
    var htmlstr=`<li class="bot-question Pli">
                    <div class="botlogodiv">
                        <img src="../static/images/user.png" alt="" srcset="">
                    </div>
                    <div class="u-question">
                       ${userinput}
                    </div>
                </li>
                <li class="bot-response Pli" >
                    <div class="botlogodiv">
                        <img src="../static/images/wizard.png" alt="" srcset="">
                    </div>
                    <div id="myloader" style="display: flex;align-items: center;gap: 2px;margin: auto 0px;"><span class="xloader"></span><span>Loading...</span></div>
                    <div id="bot-response${div_counter}" style="flex: 1 1 90%;width:90%"></div>
                </li>`
    chatbox.insertAdjacentHTML('beforeend', htmlstr);
    textareainp.value=''
    var detailsElements = document.querySelectorAll('details');
    // Loop through each <details> element and remove the "open" attribute
    detailsElements.forEach(function(details) {
        details.removeAttribute('open');
    });
}

function getresponse(data){ 
    console.log(data);
    var lastresp="#bot-response"+ div_counter
    if(data['response'] != ''){
        $(lastresp).append(`<div class="response" style="display:block;width: 90%;">${data['response']}</div>` )
    }
    if(data['new_data'] != ''){
        $(lastresp).append(`
            <details class="details" open>
                <summary class="summary" onclick="togglesvgarrow(this)">
                    <span>Data</span>
                    <svg style="transform: rotatez(180deg);" viewBox="0 0 20 20" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" data-testid="stExpanderToggleIcon" class=""><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M12 8l-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14l-6-6z"></path></svg>
                </summary>
                <div class="mydataframe-parent"  style="width: fit-content;">
                <div class="table-utility-parent">
                        <div class="table-utility">
                            <div>
                                <button kind="elementToolbar" class="" onclick="exportTableToExcel(this)">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-download" viewBox="0 0 16 16">
                                    <title>download</title>
                                    <path d="M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5"></path>
                                    <path d="M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708z"></path>
                                    </svg>
                                </button>
                            </div>
                            <div>
                                <button kind="elementToolbar" onclick="searchonoff(this)">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                                        <title>search</title>
                                        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"></path>
                                    </svg>
                                </button>
                            </div>
                            <div class="modalopener">
                                <button  kind="elementToolbar" onclick="openmodal(this)" style="display:block;">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fullscreen" viewBox="0 0 16 16">
                                        <title>fullscreen</title>
                                        <path d="M1.5 1a.5.5 0 0 0-.5.5v4a.5.5 0 0 1-1 0v-4A1.5 1.5 0 0 1 1.5 0h4a.5.5 0 0 1 0 1zM10 .5a.5.5 0 0 1 .5-.5h4A1.5 1.5 0 0 1 16 1.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 1-.5-.5M.5 10a.5.5 0 0 1 .5.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 1 0 1h-4A1.5 1.5 0 0 1 0 14.5v-4a.5.5 0 0 1 .5-.5m15 0a.5.5 0 0 1 .5.5v4a1.5 1.5 0 0 1-1.5 1.5h-4a.5.5 0 0 1 0-1h4a.5.5 0 0 0 .5-.5v-4a.5.5 0 0 1 .5-.5"></path>
                                    </svg>
                                </button>
                            </div>
                        </div>
                        <div class="mysearchutility" style="display: none;">
                            <div>
                                <input type="search" name="" id="" placeholder="Search here..." style="display: block;" oninput="searchtable(this)">
                                <!-- <span>0 results</span> -->
                            </div>
                            <!-- <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">
                                <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
                              </svg> -->
                        </div>
                </div>
                <div class="mydataframe">
                ${data['new_data']}
                </div>
                </div>
            </details> 
            `)
    }
    if(data['graph_html'] != ''){
       $(lastresp).append(`
        <details class="details" open>
            <summary class="summary" onclick="togglesvgarrow(this)">
                <span>Graph</span>
                <svg style="transform: rotatez(180deg);" viewBox="0 0 20 20" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" data-testid="stExpanderToggleIcon" class=""><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M12 8l-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14l-6-6z"></path></svg>
            </summary>
            <div class="last-graph-1" id='last-graph${div_counter}'>
               ${data['graph_html']}
            </div>
        </details>
        `) 
    }
    // appendCodeToChatbox(data['generated_response'])
   div_counter+=1
}

function appendCodeToChatbox(code) {
    const chatbox = document.getElementById(`last-code${(div_counter-1)}`);
    const codeElement = document.createElement('pre');
    codeElement.classList.add('language-python'); 
    const codeContent = document.createElement('code');
    codeContent.textContent = code;
    codeElement.appendChild(codeContent);
    chatbox.appendChild(codeElement);
    const button = chatbox.querySelector('button');

    if (button) {
      button.setAttribute('data-clipboard-text', code);
    }
    // Essential step: Highlight the newly added code
    Prism.highlightElement(codeElement);
  }




function copytext(ele){
   console.log(ele.getAttribute('data-clipboard-text'));
   const dataSortValue = ele.getAttribute('data-clipboard-text');
   navigator.clipboard.writeText(dataSortValue)
     .then(() => {
       console.log('Copied to clipboard');
     })
     .catch(err => {
       console.error('Failed to copy: ', err);
     });
}




sendbtn.addEventListener('click',getanswer)
textareainp.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' && window.innerWidth > 800 && !event.shiftKey) {
        event.preventDefault(); // Prevent form submission
        getanswer();
    }
});

var selecttable=document.getElementById('select-tbl-svg')

selecttable.addEventListener('click',()=>{
    var tablelist=document.getElementById('select-table-modal')
    if (tablelist.style.display === "none" || tablelist.style.display === "") {
        tablelist.style.display = "flex";
    } else {
        tablelist.style.display = "none";
    }
})

document.addEventListener('DOMContentLoaded',()=>{
    $.ajax({
        url: "/get_tables", // Replace with your actual API endpoint
        type: "GET",
        dataType: "json", // Expected data type
        success: function(data) {
        //   console.log(data); 
          if(data.length==0){
            $("#gettable-error").text('No table found').show()
          }
          for(let i=0;i<data.length;i++){
            $('#selct-table').append(`<option value="${data[i]}">${data[i]}</option>`)
          }
          $('#selct-table').select2({
            dropdownParent: $('.chatbox-footer'),
            // placeholder:"Select table",
           // allowClear: true
           })
        },
        error: function(xhr, status, error) {
          // Handle error
          console.log(error);
          $("#gettable-error").text('Internal server error').show()
        }
      });
    
})



function raw(){
    // <details class="details" open>
    //                         <summary class="summary">
    //                             <span>Code</span>
    //                             <svg style="transform: rotatez(180deg);" viewBox="0 0 20 20" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" data-testid="stExpanderToggleIcon" class=""><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M12 8l-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14l-6-6z"></path></svg>
    //                         </summary>
    //                         <div class="clipboard last-code-1" id='last-code${div_counter}' style='position:relative;'>
    //                                 <button  title="Copy to clipboard" data-clipboard-text="" class="copybtn" style="" onclick="copytext(this)">
    //                                     <svg xmlns="http://www.w3.org/2000/svg"
    //                                         width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
    //                                         stroke-linecap="round" stroke-linejoin="round">
    //                                         <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
    //                                         <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
    //                                     </svg>
    //                                 </button>
    //                         </div>
    //                     </details> 
}

function exportTableToExcel(element) {
  //  var tableId='table1'
    // Get the table element
   var tableId= element.parentElement.parentElement.parentElement.nextElementSibling.querySelector('table').id;
    const table = document.getElementById(tableId);
    
  
    // Initialize CSV content
    var csvContent = "";
            
    // Loop through each row
    for (var i = 0; i < table.rows.length; i++) {
        var row = table.rows[i];
        var rowData = [];

        // Loop through each cell in the row
        for (var j = 0; j < row.cells.length; j++) {
             if( j!=0){
                rowData.push(row.cells[j].innerText);
             }
            
        }

        // Join row data with commas and add a new line
        csvContent += rowData.join(",") + "\n";
    }

    // Create a Blob from the CSV content
    var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    
    // Create a link element
    var link = document.createElement("a");
    if (link.download !== undefined) {
        // Set the file name
        link.setAttribute("href", URL.createObjectURL(blob));
        link.setAttribute("download", "download.csv");

        // Trigger the download by clicking the link
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
  }

function openmodal(element){
  $(".mymodal").show()
  var masterdata= element.parentElement.parentElement.parentElement.parentElement
  var masterdataHTML = masterdata.innerHTML;
 
  var tempElement = document.createElement('div');
  tempElement.classList.add('mydataframe-parent');
  tempElement.style.width = 'fit-content';
  tempElement.innerHTML = masterdataHTML;

   var utilityElements = tempElement.querySelectorAll('.modalopener')[0]
    utilityElements.innerHTML=`<button onclick="closemodal(this)">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-fullscreen-exit" viewBox="0 0 16 16">
                                        <path d="M5.5 0a.5.5 0 0 1 .5.5v4A1.5 1.5 0 0 1 4.5 6h-4a.5.5 0 0 1 0-1h4a.5.5 0 0 0 .5-.5v-4a.5.5 0 0 1 .5-.5m5 0a.5.5 0 0 1 .5.5v4a.5.5 0 0 0 .5.5h4a.5.5 0 0 1 0 1h-4A1.5 1.5 0 0 1 10 4.5v-4a.5.5 0 0 1 .5-.5M0 10.5a.5.5 0 0 1 .5-.5h4A1.5 1.5 0 0 1 6 11.5v4a.5.5 0 0 1-1 0v-4a.5.5 0 0 0-.5-.5h-4a.5.5 0 0 1-.5-.5m10 1a1.5 1.5 0 0 1 1.5-1.5h4a.5.5 0 0 1 0 1h-4a.5.5 0 0 0-.5.5v4a.5.5 0 0 1-1 0z"/>
                                    </svg>
                                </button>`;
  $('.mymodal-content').html(tempElement)
  
}

function closemodal(element){
    $(".mymodal").hide()
}

function searchtable(element){
    console.log('called');
    
    var table= element.parentElement.parentElement.parentElement.nextElementSibling.querySelector('table');
    var searchValue=element.value.toLowerCase();
    var rows = table.querySelectorAll('tr');
    // var  spanresults=element.nextElementSibling
    var count=0
    // Loop through each row
    rows.forEach(function(row, index) {
        if (index === 0) return; // Skip the first row (header)
        // Assume initially that the row does not match the search
        var rowMatches = false;
        // Loop through each cell in the row
        var cells = row.querySelectorAll('td');
        cells.forEach(function(cell) {
            // Check if the cell value matches the search value
            var cellValue = cell.textContent.toLowerCase() || cell.innerText.toLowerCase();
            if (cellValue.includes(searchValue)) {
                rowMatches = true; 
            }
        });
        // Show or hide the row based on whether it matches the search value
        if (rowMatches) {
            row.style.display = ''; // Show the row
            count++;
        } else {
            row.style.display = 'none'; // Hide the row
            count--
        }

    })
    console.log(searchValue,count);

    // spanresults.innerHTML=count + "results"
}

function debounce(func, wait) {
    let timeout;
    return function(...args) {
        const context = this;
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(context, args), wait);
    };
}



function searchonoff(element){
    var searchtab= element.parentElement.parentElement.nextElementSibling;
    if (searchtab.style.display === 'none' || searchtab.style.display === '') {
        searchtab.style.display = 'block'; // Show the element
    } else {
        searchtab.style.display = 'none'; // Hide the element
    }
}

function togglesvgarrow(element) { 
    const svg = element.querySelector('svg');
   // console.log(svg);
    
    const currentRotation = svg.style.transform;
    if (currentRotation === 'rotateZ(180deg)') {
        svg.style.transform = 'rotateZ(360deg)';
    } else {
        svg.style.transform = 'rotateZ(180deg)';
    }
}