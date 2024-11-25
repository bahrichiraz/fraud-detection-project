import React from 'react';
import NavBar from './navbarhome';

const HomePage = () => {
    return (
        <div>
            <NavBar />
            <div className="content">
                <h1>Welcome to the Home Page!</h1>
                <p>This is the content you want to show to logged-in users.</p>
            </div>
        </div>
    );
}

export default HomePage;





