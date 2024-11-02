// components/LoginPage.tsx
import React, { useState } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTwitter } from '@fortawesome/free-brands-svg-icons';
import { useNavigate } from 'react-router-dom';

import { login } from '../../api/login_api';

const Login = ({ onLogin }) => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const [isLoginMode, setIsLoginMode] = useState(false); // Estado para controlar o modo
    const [isLoading, setIsLoading] = useState(false);
    const [itemActive, setItemActive] = useState(0);
    const [error, setError] = useState('');

    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);

        try {
            const data = await login(email, password);

            // Aqui você deve lidar com a informação de que o usuário existe
            if (data.access && data.refresh) {
                localStorage.setItem('user_token', data.access);
                localStorage.setItem('user_refresh_token', data.refresh);
                console.log("Tokens armazenados:", {
                    access: localStorage.getItem('user_token'),
                    refresh: localStorage.getItem('user_refresh_token')
                });

                setEmail('');
                setPassword('');
                onLogin();
                navigate('/home');
            } else {
                console.error("Tokens não recebidos na resposta do login.");
            }
        } catch (error) {
            console.log("Erro ao logar", error.response?.data || error.message);
        } finally {
            setIsLoading(false);
        }
    };


    return (
        <div className="flex h-screen bg-gray-900">
            <div className="flex-grow flex items-center justify-center">
                <form onSubmit={handleSubmit} className="p-6 rounded-lg w-96">
                    <div className='absolute top-10'>
                        <FontAwesomeIcon icon={faTwitter} className="text-6xl text-twitter-blue" />
                    </div>
                    {!isLoginMode && (
                        <div className="mb-4">
                            <input
                                type="name"
                                placeholder="Name"
                                value={name}
                                onChange={(e) => setName(e.target.value)}
                                className="w-full bg-gray-700 text-white rounded py-2 px-4"
                                required
                            />
                        </div>
                    )}
                    <div className="mb-4">
                        <input
                            type="email"
                            placeholder="Email address"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            className="w-full bg-gray-700 text-white rounded py-2 px-4"
                            required
                        />
                    </div>
                    <div className="mb-4">
                        <input
                            type="password"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="w-full bg-gray-700 text-white rounded py-2 px-4"
                            required
                        />
                    </div>
                    {!isLoginMode ? (
                        <p className='mb-8 text-sm'>By signing up, you agree with our <span className='text-twitter-blue font-bold cursor-pointer hover:underline'>Terms of Use</span></p>
                    ) : <p className='mb-8 text-sm'>Forgot your password? <span className='text-twitter-blue font-bold cursor-pointer hover:underline'>Click here</span></p>}
                    <button
                        type="submit"
                        className="w-full bg-twitter-blue text-white font-bold py-2 rounded hover:bg-blue-600 transition duration-200"
                    >
                        {isLoginMode ? 'Login' : 'Sign Up'}
                    </button>
                    <div className='absolute bottom-12'>
                        <p className='mt-6'>
                            {isLoginMode ? 'Not a member? ' : 'Already a member? '}
                            <span
                                className='text-twitter-blue font-bold cursor-pointer hover:underline'
                                onClick={() => setIsLoginMode(!isLoginMode)}
                            >
                                {isLoginMode ? 'Sign Up' : 'Login'}
                            </span>
                        </p>
                    </div>
                </form>
            </div>
            <div className="w-5/12 hidden md:flex flex-col items-center justify-center bg-gray-800 text-white p-6">
                <h2 className="text-2xl text-center mb-4">
                    It's what's happening
                </h2>
                <div className="flex items-center">
                    <h1 className="text-4xl font-bold mr-2 font-Comfortaa">Twitter</h1>
                    <FontAwesomeIcon icon={faTwitter} className="text-4xl" />
                </div>
            </div>
        </div>
    );
};

export default Login;
