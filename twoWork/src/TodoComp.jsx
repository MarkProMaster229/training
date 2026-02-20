import { useState } from 'react'

function ToDoList(){

<h>this Todo app for you!</h>
const [text, settext] = useState("")
const [todoList, SetTodoFun] = useState([]);

return(
    <div>
        <input type='text' value={text} onChange={(e) =>
        settext(e.target.value)}placeholder='пиши задачу'
        />
    

   <button onClick={() => SetTodoFun([...todoList, text])}>
      Добавить
    </button>

    <ul>
        {todoList.map((todo, index) => (
            <li key={index}>{todo}</li>   // каждый элемент массива — своя строка
        ))}
    </ul>

</div>

)
}

export default ToDoList