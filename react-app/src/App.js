import React, {useState, useEffect} from 'react'
import api from './api'

const App = () => {
  const [clubs, setClubs] = useState ([]);
  const [formData, setFormData] = useState({
    brand: '',
    model: '',
    club_type: '',
  });

  const fetchClubs = async () => {
    const response = await api.get('/clubs/');
    setClubs(response.data)
  };
  useEffect(() => {
    fetchClubs();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value,
    });
  };


  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/clubs/', formData);
    fetchClubs();
    setFormData({
    brand: '',
    model: '',
    club_type: ''
    });
  };


  return (
    <div>
    <nav className='navbar navbar-dark bg-primary'>
      <div className='container-fluid'>
        <a className='navbar-brand' href="#">
          Finance App
        </a>
      </div>
    </nav>

    <div className='container'>
      <form onSubmit={handleFormSubmit}>
        <div className='mb-3 mt-3'>
          <label htmlFor='brand' className='form-label'>
            brand
          </label>
          <input type='text' className='form-control' id='brand' name='brand' onChange={handleInputChange} value={formData.brand}/>
        </div>

        <div className='mb-3'>
          <label htmlFor='model' className='form-label'>
          model
          </label>
          <input type='text' className='form-control' id='model' name='model' onChange={handleInputChange} value={formData.model}/>
        </div>

        <div className='mb-3'>
          <label htmlFor='club_type' className='form-label'>
          club_type
          </label>
          <input type='text' className='form-control' id='club_type' name='club_type' onChange={handleInputChange} value={formData.club_type}/>
        </div>

      </form>

      <table className='table table-striped table-bordered table-hover'>
        <thead>
          <tr>
          <th>brand</th>
          <th>model</th>
          <th>club_type</th>
          <th>income</th>
          <th>date</th>
        </tr>
        </thead>
        <tbody>
          {clubs.map((transaction) =>(
            <tr key={transaction.id}>
              <td>{transaction.brand}</td>
              <td>{transaction.model}</td>
              <td>{transaction.club_type}</td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
    </div>
  )
}
export default App;