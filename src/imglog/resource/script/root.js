const records = {recorddata};

const logIdInputFormElement = document.getElementById("logidinput");
const logTimeElement = document.getElementById("logtime");
const logLevelElement = document.getElementById("loglevel");
const traceElement = document.getElementById("tracecontent");
const imageElement = document.getElementById("images");
const imagesDataElement = document.getElementById("databody");
const logContentElement = document.getElementById("logcontent");
let preyElement = document.createElement('li');


function loadTitles(logtime, loglevel) {
    logTimeElement.textContent = '';
    logTimeElement.textContent = logtime;

    logLevelElement.className = '';
    logLevelElement.className =  'badge '+ loglevel;
    logLevelElement.textContent = '';
    logLevelElement.textContent = loglevel;
}

function loadTraceContent(trace){
    traceElement.textContent = '';
    traceElement.textContent = trace;
}

function loadImages(images){
    while (imageElement.firstChild){
        imageElement.removeChild(imageElement.firstChild);
    }

    for (let [index, image] of images.entries()){
        const h4Element = document.createElement("h4");
        h4Element.textContent = "#" + index;

        const imgElement = document.createElement("img");
        imgElement.setAttribute("src", 'data:image/png;base64,' + image);
        imgElement.setAttribute("class", "img-fluid");

        const columnElement = document.createElement("div");
        columnElement.setAttribute("class", "col-md-12");
        columnElement.appendChild(h4Element);
        columnElement.appendChild(imgElement);

        imageElement.appendChild(columnElement);
    }
}

function loadImagesData(imagesProperty){
    while (imagesDataElement.firstChild){
        imagesDataElement.removeChild(imagesDataElement.firstChild);
    }

    for (let [index, imageProperty] of imagesProperty.entries()){
        const trElement = document.createElement("tr");

        const tableHead = document.createElement("th");
        tableHead.setAttribute("scope", "row");
        tableHead.textContent = index;

        trElement.appendChild(tableHead);

        const widthElement = document.createElement("td");
        widthElement.textContent = imageProperty.width;

        const heightElement = document.createElement("td");
        heightElement.textContent = imageProperty.height;

        const channelElement = document.createElement("td");
        channelElement.textContent = imageProperty.channel;

        const modeElement = document.createElement("td")
        modeElement.textContent = imageProperty.mode

        const elements = [widthElement, heightElement, channelElement, modeElement];
        for (const element of elements) {
            trElement.appendChild(element);
        }

        imagesDataElement.appendChild(trElement)
    }
}

function loadLog(id, source) {
    logContentElement.classList.remove('d-none')
    preyElement.classList.remove('shadow');
    source.classList.add('shadow');
    preyElement = source;

    for (record of records) {
        if(id == record.id) {
            loadTitles(record.time, record.level);
            loadImages(record.images);
            loadImagesData(record.imagesProperty);
            // loadTraceContent(record.stacktrace);
        }
    }
}

function loadLogInput() {
    const inputId = logIdInputFormElement.value;
    const searchResult = document.getElementById(inputId)

    if (searchResult != null) {
        loadLog(inputId, searchResult)
    }
}