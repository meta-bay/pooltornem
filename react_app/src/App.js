import "./App.css";
import Dashboard from "./Dashboard";
import Landingpage from "./Landingpage";
import Register from "./Register";
import Login from "./Login";
import PlayerTable from "./PlayerTable";
import Contact from "./Contact";
import {
  BrowserRouter as Router,
  Route,
  Routes,
  Outlet,
  useLocation,
} from "react-router-dom";
import Tournament from "./Tournament";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Landingpage />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/match" element={<Tournament />} />
          <Route path="/players" element={<PlayerTable />} />
          <Route path="/contact-us" element={<Contact />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
