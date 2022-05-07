import React from 'react';

import './ProblemStatement.styles.css';

const ProblemStatement = () => {
    return (
        <div className='ps_body'>
            <h1 className='ps_title'>Problem Statement</h1>
            <p className='ps_text'>
                Build a model to predict the solar energy generation of a particular region using weather and solar irradiance data
            </p>
        </div>
    );
}
export default ProblemStatement;