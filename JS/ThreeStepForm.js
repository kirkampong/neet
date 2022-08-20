// BoardBase:

// <input> tutorial: https://upmostly.com/tutorials/react-onchange-events-with-examples


import "./styles.css";
import { useState } from "react";



const connectChatServer = () => {
  
}

export default function App() {
  useEffect( ()=>{
    console.log("hello");
    setTimeout( ()=>{ alert("hello"); }, 2000);

    return ()=> {/*socket.disconnect*/} //useEffect cleanup
  }, [] ); //empty => componentDidMount


  const saveHuman = (event) => {
    if (event.target.value === "No") {
      setHuman(false);
    } else {
      setHuman(true);
    }
  };

  const saveName = (input) => {
    setName(input);
  };

  const saveComment = (input) => {
    setComment(input);
  };

  const [name, setName] = useState("");
  const [human, setHuman] = useState(false);
  const [comment, setComment] = useState("");
  const [step, setStep] = useState("Human");

  return (
    <div className="App">
      <div>
        <h1>Are you Human?</h1>
        <select onChange={(e) => saveHuman(e)}>
          <option>Yes</option>
          <option>No</option>
        </select>
        <br></br>
        <button onClick={setStep("Name")}>Next</button>
      </div>

      <div>
        <h1>Enter Your Name:</h1>
        <input onChange={(e)=> saveName(e)}></input>
        <br></br>
        <button onClick={setStep("Comment")}>Next</button>
      </div>

      <div>
        <h1>Enter Your Comment:</h1>
        <textarea onChange={saveComment}></textarea>
        <br></br>
        <button onclick={setStep("showAnswers")}>Submit</button>
      </div>

      <h1>ans:</h1>
      <div>
        {name}
        {human}
        {comment}
      </div>
    </div>
  );
}
