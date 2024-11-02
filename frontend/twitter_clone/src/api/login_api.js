import axios from 'axios';
import { API_BASE_URL } from "./base_api";

export const login = async (email, password) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/token/`, {
            email: email,
            password: password,
        });

        return response.data;
    } catch (error) {
        console.error("Erro ao fazer login:", error.response?.data || error.message);
        throw error;  
    }
};

export const logout = async () => {
    const refreshToken = localStorage.getItem('user_refresh_token'); 

    console.log("Token de logout:", refreshToken);

    if (!refreshToken) {
        console.error("Token de refresh não encontrado. Usuário não está logado.");
        return { success: false, message: "Token de refresh não encontrado. Usuário não está logado." };
    }

    try {
        const response = await axios.post(`${API_BASE_URL}/api/auth/logout/`, {
            refresh: refreshToken 
        }, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('user_token')}`, 
            }
        });

        // Remover tokens do localStorage
        localStorage.removeItem('user_token');
        localStorage.removeItem('user_refresh_token');

        return { success: true, message: "Logout realizado com sucesso." };
    } catch (error) {
        console.error("Erro durante o logout:", error.response ? error.response.data : error.message);
        return { success: false, message: error.response ? error.response.data : error.message };
    }
};


export const checkEmailExists = async (user_email) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/api/auth/check-email/`, {
            params: { email: user_email }
        });

        return response.status === 200; 
    } catch (error) {
        console.error("Erro ao verificar e-mail:", error);
        return false; 
    }
};



