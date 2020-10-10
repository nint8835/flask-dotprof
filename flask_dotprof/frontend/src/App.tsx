import React from 'react';
import './App.css';
import { Graphviz } from 'graphviz-react';

function App() {
  return (
    <div className="App">
      <Graphviz dot={`
        digraph G {
          hello
          world
          this
          is
          a
          test

          hello -> world
          this -> is
          is -> a
          a -> test
          a -> world
          hello ->  test
        }
      `}/>
    </div>
  );
}

export default App;
