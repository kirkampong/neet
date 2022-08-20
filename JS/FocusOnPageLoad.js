import React, {useEffect, useRef} from 'react';

const App = () => {
  const inputElRef = useRef(null)
  
  useEffect(()=>{
    inputElRef.current.focus()
  }, [])
  
  return(
    <div>
      <input
        defaultValue={'Won\'t focus'}
      />
      <input
        ref={inputElRef}
        defaultValue={'Will focus'}
      />
    </div>
  )
}

ReactDOM.render(<App />, document.getElementById('app'))