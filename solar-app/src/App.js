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
      <img src={plot} alt='figure' className='figure' />
      <img src={photo_pot} alt='photovoltaic potential' className='figure' />
    </div>
  );
}

export default App;
