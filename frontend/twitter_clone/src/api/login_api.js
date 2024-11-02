import axios from 'axios';
import { API_BASE_URL } from "./base_api";

export const login = async (email, password) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/auth/login/`, { email, password });
        if (response.status === 200 && response.data.access && response.data.refresh) {
            return { success: true, data: response.data };
        } else {
            return { success: false, message: "Tokens não recebidos na resposta do login." };
        }
    } catch (error) {
        console.error("Erro ao fazer login:", error.response ? error.response.data : error.message);
        return { success: false, message: error.response?.data?.message || "Erro ao fazer login." };
    }
};

export const register = async (name, email, password) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/auth/register/`, { name, email, password });
        if (response.status === 201) {
            return { success: true, message: "Cadastro realizado com sucesso! Faça o login." };
        } else {
            return { success: false, message: "Erro desconhecido ao tentar registrar o usuário." };
        }
    } catch (error) {
        console.error("Erro ao registrar usuário:", error.response ? error.response.data : error.message);
        return { success: false, message: error.response?.data?.message || "Erro ao registrar usuário." };
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
        return { success: false, message: error.response?.data?.message || "Erro durante o logout." };
    }
};

export const checkEmailExists = async (user_email) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/api/auth/check-email/`, {
            params: { email: user_email }
        });

        return { success: response.status === 200, exists: response.status === 200 }; 
    } catch (error) {
        console.error("Erro ao verificar e-mail:", error);
        return { success: false, message: error.response?.data?.message || "Erro ao verificar e-mail." };
    }
};
