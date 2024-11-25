import React from 'react';
import './dashboard.css'; // Si vous avez un fichier CSS spécifique pour cette page
import SideBar from './navbarhome';

function Page2() {
  return (
    <div className="dashboard-container">
      <SideBar />
      <div className="main-content">
        <div className="powerbi-container">
          <iframe 
            title="monpfe12" 
            width="1024" 
            height="1060" 
            src="https://app.powerbi.com/view?r=eyJrIjoiNjZhYjQyZDQtYmQ0ZC00NDIwLThlNzItZWY1MmU0YjBhZjFhIiwidCI6ImRiZDY2NjRkLTRlYjktNDZlYi05OWQ4LTVjNDNiYTE1M2M2MSIsImMiOjl9&pageName=64fc4453bb948937d17c" 
            frameBorder="0" 
            allowFullScreen="true">
          </iframe>
        </div>
      </div>
    </div>
  );
}

export default Page2;

