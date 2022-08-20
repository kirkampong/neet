import logo from './logo.svg';
import './App.css';
import {useEffect, useState} from 'react'
import axios from "axios"

function App() {
  const [posts, setPosts] = useState([]);
  const [userInfo, setUserInfo] = useState([]);

  useEffect(() => {
    let userIds = new Set()
    const p = axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(function(response){
        setPosts(response.data)
        for (let i=0; i<posts.length; i++) {
          userIds.add(posts[i].userId)
        }
      }).then(function(){        
        let userInfoTemp = []
        userIds.forEach(userId => {
          const u = axios.get(`https://jsonplaceholder.typicode.com/users/${userId}`)
          userInfoTemp.push(u)
        })
        Promise.all(userInfoTemp).then((values) => {
          const res = values.map(val => {
            return val.data;
          })
          setUserInfo(res)
        });
       }
      )
    
  }, [])
  return (
    <div className="App">
      {posts.map((post) => 
        <li key={post.id}>
        
          {post.title}
          {
          (userInfo.find(info => {
            return(info.id === post.userId)
          }))?.name}
        </li>)
        
        }
        
    </div>
  );
}

export default App;
