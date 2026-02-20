import { useState } from 'react' // Импортируем "состояние"
import Hello from './Hello'
import Test from './TestComponent'
import ToDoList from './TodoComp'
import ColorForYou from './StillColor'
function App() {
  // Создаем переменную 'count' и функцию 'setCount', чтобы её менять
  const [count, setCount] = useState(0)

  return (
    
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Мой первый React проект!</h1>
      <p>Ты нажал на кнопку {count} раз</p>
      <Hello name="Бро" />
      <Hello name="React-мастер" />
      <Test />
      <ToDoList />
      <ColorForYou />
      {/* При клике вызываем setCount, React сам перерисует текст выше */}
      <button onClick={() => setCount(count + 1)}>
        Нажми меня
      </button>
    </div>
  
)
}

export default App
