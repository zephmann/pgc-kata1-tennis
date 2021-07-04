import React from 'react';

import './App.css';

const TENNIS_API_URL = "/api/score?";


class App extends React.Component {

  constructor(props) {
    super(props);
    
    this.state = {
      server: 0,
      opponent: 0,
      score: "...",
      active: true
    };

    this.updateScore = this.updateScore.bind(this);
    this.handleServerClick = this.handleServerClick.bind(this);
    this.handleOpponentClick = this.handleOpponentClick.bind(this);
    this.parseScore = this.parseScore.bind(this);
    this.resetGame = this.resetGame.bind(this);
  }

  componentDidMount() {
    const url = TENNIS_API_URL + "server=0&opponent=0";
    fetch(url).then(res => res.json()).then(data => {
      this.setState({ score: data.score })
    });
  }

  handleServerClick() {
    const new_server = this.state.server + 1;

    this.setState({
      server: new_server
    });
    
    this.updateScore(new_server, this.state.opponent);
  }

  handleOpponentClick() {
    const new_opponent = this.state.opponent + 1;

    this.setState({
      opponent: new_opponent
    });
    
    this.updateScore(this.state.server, new_opponent);
  }

  updateScore(server, opponent) {
    this.setState({
      score: "..."
    });

    console.log(server + " " + opponent);

    const url = (
      TENNIS_API_URL + 
      "server=" + server + 
      "&opponent=" + opponent
    );
    fetch(url).then(res => res.json()).then(this.parseScore);
  }

  parseScore(data) {
    const active = !data.score.includes("Game");
    this.setState({
      score: data.score,
      active: active
    });
  }

  resetGame() {
    this.setState({
      server: 0,
      opponent: 0,
      score: "...",
      active: true
    });

    this.updateScore(0, 0);
  }

  render() {
    const debug_text = this.state.server + " " + this.state.opponent;
    const active_text = this.state.active ? "Game is active" : "Game is over"

    let button_grp;
    if (this.state.active) {
      button_grp = <div>
        <div id="server" className="btn" onClick={this.handleServerClick}><h2>Point Server</h2></div>
        <div id="opponent" className="btn" onClick={this.handleOpponentClick}><h2>Point Opponent</h2></div>
      </div>;
    }

    return (
      <div className="App">
        <h1>Tennis Score</h1>
        <h1 id="score">"{this.state.score}"</h1>
        {button_grp}
        <div id="reset" className="btn" onClick={this.resetGame}><h2>Reset Game</h2></div>
        <h1>{debug_text}</h1>
        <h1>{active_text}</h1>
      </div>
    );
  }
}

export default App;
