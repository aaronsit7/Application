import React, { useState } from 'react';
import axios from 'axios';
import { serverUrl } from './url';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${serverUrl}/login`, { username, password });
      setMessage(response.data.message);
    } catch (error) {
      setMessage(error.response.data.message || 'Login failed.');
    }
  };

  return (
    <div className="flex h-screen">
      <div className="hidden lg:flex items-center justify-center flex-1 bg-white text-black">
        <div className="max-w-md text-center">
          <svg xmlns="http://www.w3.org/2000/svg" width="524.67004" height="531.39694" className="w-full" alt="https://undraw.co/illustrations" title="https://undraw.co/illustrations" viewBox="0 0 524.67004 531.39694">
            {/* SVG content */}
          </svg>
        </div>
      </div>
      <div className="w-full bg-gray-100 lg:w-1/2 flex items-center justify-center">
        <div className="max-w-md w-full p-6">
          <h1 className="text-3xl font-semibold mb-6 text-black text-center">Log In</h1>
          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label htmlFor="username" className="block text-sm font-medium text-gray-700">Username</label>
              <input
                type="text"
                id="username"
                name="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="mt-1 p-2 w-full border rounded-md focus:border-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-300 transition-colors duration-300"
              />
            </div>
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700">Password</label>
              <input
                type="password"
                id="password"
                name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mt-1 p-2 w-full border rounded-md focus:border-gray-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-300 transition-colors duration-300"
              />
            </div>
            <div>
              <button type="submit" className="w-full bg-black text-white p-2 rounded-md hover:bg-gray-800 focus:outline-none focus:bg-black focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 transition-colors duration-300">Log In</button>
            </div>
          </form>
          {message && <p className="mt-4 text-sm text-gray-600 text-center">{message}</p>}
          <div className="mt-4 text-sm text-gray-600 text-center">
            <p>Don't have an account? <a href="/" className="text-black hover:underline">Sign up here</a></p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
