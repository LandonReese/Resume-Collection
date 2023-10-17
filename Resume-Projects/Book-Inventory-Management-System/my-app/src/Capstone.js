import React from 'react';
import ReactDOM from 'react-dom';
import './Capstone.css';

import Component1 from './Components/Component1.js';
import Component2 from './Components/Component2.js';
import Component3 from './Components/Component3.js';
import Component4 from './Components/Component4.js';

function Capstone(){
	return (
	  <React.StrictMode>
		<div className="container">
		  <div className="header"><Component1 /></div>
		  
		  <div className="upperMiddle"><Component2 /></div>
		  <div className="lowerMiddle"><Component3 /></div>
		  
		  
		  <div className="footer"><Component4 /></div>
		</div>
	  </React.StrictMode>
	);
}

export default Capstone;