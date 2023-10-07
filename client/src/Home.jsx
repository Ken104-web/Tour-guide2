// import image2 from "./image.jpg"
// import image3 from "./beach.jpeg"
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";


function Home(){
const [sites, setSites] = useState([]);
const [selectedSite, setSelectedSite] = useState(null);

useEffect(() => {
    fetch('api/sites')
    .then((r) => r.json())
    .then(data => setSites(data));
}, [])

const handleSiteChange = (e) => {
    const selectedSiteId = e.target.value;
    setSelectedSite(selectedSiteId)
};

return (
        <div id='home'>
            <span>
                <select
                    id="siteDropdown"
                     onChange={handleSiteChange}
                     value={selectedSite || ""}>
                         <option value="">Select a Site</option>
          {sites.map((site) => (
            <option key={site.id} value={site.id}>
              {site.location}
              <Link to={`specificsite/${site.id}`}>{site.location}</Link>
            </option>
          ))}
            </select>
            </span>
            
            <table>
  <thead>
    <tr>
      <th>Popular Sites</th>
    </tr>
  </thead>
  <tbody>
    {sites.map((site) => (
      <tr key={site.id}>
        <td><a href={`/specificsite/${site.id}`}>{site.location}</a></td>
      </tr>
    ))}
  </tbody>
</table>

                {/* <h1>Popular sites</h1>
            {sites.map((site) => (
          <p key={site.id} id="image">
            <Link to={`specificsite/${site.id}`}>{site.location}</Link>
          </p>
            ))} */}
            

        </div>
    )
}
export default Home;