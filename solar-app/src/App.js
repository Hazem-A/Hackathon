import './App.css';

import Splash from './components/Splash/Splash';
import ProblemStatement from './components/ProblemStatement/ProblemStatement';

import plot from './assets/figure/myplot.png';
import photo_pot from './assets/figure/Photovoltaic Potential.png';

function App() {

  return (
    <div className="App">
      <Splash />
      <ProblemStatement />
      <h1>Historical Cloud_Covering in Alberta</h1>
      <img src={plot} alt='figure' className='figure' />
      <h1>PhotoVoltaic Potential throughout the year</h1>
      <img src={photo_pot} alt='photovoltaic potential' className='figure' />
    </div>
  );
}

export default App;
