import React from 'react';
import PropTypes from 'prop-types';

import {connect} from 'react-redux';

function Home() {
  return (
    <div>
      <h1>Hello Player!</h1>
    </div>
  );
}

const module = connect(
  null,
  null
)(Home);

export default module;
