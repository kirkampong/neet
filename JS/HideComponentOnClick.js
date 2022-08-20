import {useState} from 'react';

export default function App() {
  const [isShown, setIsShown] = useState(false);

  const handleClick = event => {
    // 👇️ toggle shown state
    setIsShown(current => !current);

    // 👇️ or simply set it to true
    // setIsShown(true);
  };

  // Do not render component at all
  if (!props.warn) {
    return null;
  }

  return (
    <div>
      <button onClick={handleClick}>Click</button>

      {/* 👇️ Note: ternary is better since the left side could be falsy(eg empty array)
       and render nothing or zero*/}
      {isShown && (
        <div>
          <h2>Some content here</h2>
        </div>
      )}

      {/* 👇️ show component on click */}
      {(message.length > 0) && <Box />}

      <div>
        The user is <b>{isShown ? 'currently' : 'not'}</b> logged in.
      </div>
    </div>
  );
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

// map list to components:
posts.map(post => <li key={post.id}>{post.title}</li>)

// Root setup:
const root = ReactDOM.createRoot(document.getElementById('root')); 
// Try changing to isLoggedIn={true}:
root.render(<Greeting isLoggedIn={false} />);