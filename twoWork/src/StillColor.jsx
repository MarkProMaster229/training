import { useState } from "react";


function ColorForYou(){
const[NameColor,ColorNameFun] = useState("")
const[stateList, StateListForControl] = useState([]);

return(
    <div style={{background: stateList[stateList.length - 1]}}>
        
        <h1>протестируй свой цвет тут!</h1>
        <input type="text"value={NameColor} onChange={(e) => 
        ColorNameFun(e.target.value)}placeholder="введи свой цвет" 
        />

        <button onClick={() => StateListForControl([...stateList,NameColor])}>
            Добавить1
        </button>

    <ul>
        {stateList.map((colorm,index) => (
            <li key={index}>{colorm}</li>
        ))}
    </ul>
    
    </div>

)
}
export default ColorForYou