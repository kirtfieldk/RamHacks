import React, {useState} from 'react'

function Spaces() {
    const [map, setMap] = useState("")
    const renderButtons = () =>{
        return(
            <div className = "flex flex-wrap">
                <div className = "w-9/12 flex-row rounded-lg mx-auto mt-24 mb-12 h-10 text-2xl align-text-bottom hover:bg-green-400 font-bolder justify-between border text-center"
                onClick = {() => setMap("garage")}>
                    Parking Spotss
                </div>
                <div className = "w-9/12 rounded-lg flex-row mx-auto my-12 hover:bg-green-400 text-2xl h-10 font-bolder justify-between border text-center"
                onClick = {() => setMap("room")}>
                    Meeting Spaces
                </div>
            </div>
        )
    }
    const displayBtnOrMap = () =>{
        if(map === "")
            return renderButtons()
        if(map === "garage")
            return <div>Garage</div>
        if(map === "room")
            return <div>Room</div>
    }
    return (
        <div>
            {displayBtnOrMap()}
        </div>
    )
}


export default Spaces
