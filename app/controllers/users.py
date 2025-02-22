* {
    font-family: 'Poppins', sans-serif;
    color: white;
}

body {
    display: flex;
    flex-direction: column;
    background-color: #121212;
    padding: 0px;
    margin: 0px;
    height: 100vh;
    width: 100vw;
}

.purple {
    color: #4361ee;
}

.navbar {
    background-color: #121212;
    padding: 0px;
    margin: 0px;
    position: sticky;
    top: 0px;
    z-index: 1;
    padding: 0px 0px;
}

.flex {
    display: flex;
}

.row {
    flex-direction: row;
}

.column {
    flex-direction: column;
}

.jsplit {
    justify-content: space-between;
}

.gap {
    gap: 10px;
}

.container {
    width: calc(100% - 40px);
    max-width: 1200px;
    margin: auto;
    padding: 20px 20px;
}

.products {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-start;
    gap: 10px;
}

.product {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background-color: #222222;
    padding: 20px;
    border-radius: 5px;
    /* flex-grow: 1; */
    flex-shrink: 0;
    width: 300px;
}

.light {
    opacity: 0.5;
}

.center {
    display: flex;
    justify-content: center;
    align-items: center;
}

.align-center {
    align-items: center;
}

.justify-center {
    justify-content: center;
}

.justify-split {
    justify-content: space-between;
}


.fill-height {
    flex-grow: 1;
}

.fill-width {
    width: 100%;
}

.box {
    background-color: #222222;
    border-radius: 5px;
    padding: 20px;
}

.gap-10 {
    gap: 10px;
}

input {
    background-color: #161616a6;
    border: none;
    border-radius: 5px;
    padding: 10px;
    color: white;
    outline: none;
    min-width: 300px;
}

button {
    background-color: #4361ee;
    border: none;
    border-radius: 5px;
    padding: 10px;
    color: white;
    outline: none;
    cursor: pointer;
}

textarea {
    background-color: #161616a6;
    border: none;
    border-radius: 5px;
    padding: 10px;
    color: white;
    outline: none;
    min-width: 300px;
    min-height: 100px;
}

.aButton {
    background-color: #4361ee;
    border: none;
    border-radius: 5px;
    padding: 10px;
    color: white;
    outline: none;
    cursor: pointer;
    text-decoration: none;
    width: fit-content;
}

.warning {
    background-color: #ee4361;
}
