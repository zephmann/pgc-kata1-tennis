import React, { useState } from 'react';

import './App.css';

class App extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      server: 0,
      opponent: 0,
      score: ""
    };
  }

  componentDidMount() {
    const url = "/api/score?server=0&opponent=0";
    fetch(url).then(res => res.json()).then(data => {
      this.setState({ score: data.score })
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
