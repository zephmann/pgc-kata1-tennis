import React, { useState } from 'react';

import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  // const [server, setServer] = useState(0);
  // const [opponent, setOpponent] = useState(0);
  // const [score, setScore] = useState("");

  constructor(props) {
    super(props);
    
    this.state = {
      server: 1,
      opponent: 0,
      score: ""
    };
  }

  componentDidMount() {
    const url = "/score?server=0&opponent=0";
    fetch(url).then(res => res.json()).then(data => {
      this.setState({ score: data.score })
      // setScore(data.score);
    });
  }

  render() {
    return (
      <div className="App">
        <h1>Tennis Score</h1>
        <h1 id="score">"{this.state.score}"</h1>
        <div id="server" className="btn"><h2>Point Server</h2></div>
        <div id="opponent" className="btn"><h2>Point Opponent</h2></div>
      </div>
    );
  }
}

export default App;
