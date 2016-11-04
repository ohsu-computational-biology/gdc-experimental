import React, { PropTypes } from 'react';

// TODO - this is not currently used...

const Resource = ({ resource }) => {
  const { login, avatar_url, html_url } = resource;
  const src = `https://ghbtns.com/github-btn.html?resource=${login}&type=follow&count=true&size=large`;

  return (
    <div className="card">
      <div className="card-header">
          <a href={ html_url } target="_blank">
            <h4>{login}</h4>
          </a>
      </div>

      <div className="card-block">
        <img src={ avatar_url } className="card-img-top" width="120" height="120" alt="avatar"/>
      </div>

      <div className="card-footer">
        <iframe
          src={src}
          allowTransparency="true"
          scrolling="0"
          frameBorder="0"
          width="500"
          height="30">
        </iframe>
      </div>
    </div>
  );
};

Resource.propTypes = {
  resource: PropTypes.shape({
    login: PropTypes.string.isRequired,
    avatar_url: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,
    html_url: PropTypes.string.isRequired,
  }).isRequired,
};

export default Resource;
