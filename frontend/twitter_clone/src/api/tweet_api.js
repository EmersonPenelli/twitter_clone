import axios from 'axios';
import { API_BASE_URL } from "./base_api";

export const tweet = async (userId, content) => {
    try {
        const payload = {
            user: userId,
            content
        };
        
        console.log("Payload enviado:", payload); 

        const response = await axios.post(`${API_BASE_URL}/api/tweets/`, payload);
        
        if (response.status === 201) { 
            return { success: true, data: response.data };
        } else {
            return { success: false, message: "Tweet sent successfully." };
        }
    } catch (error) {
        console.error("Error tweeting:", error.response ? error.response.data : error.message);
        return { success: false, message: error.response?.data?.message || "An error occurred." };
    }
};

export const fetchTweets = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/api/tweets/`, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('user_token')}`
            }
        });
        if (response.status === 200) {
            return { success: true, data: response.data };
        } else {
            return { success: false, message: "Failed to fetch tweets." };
        }
    } catch (error) {
        console.error("Error fetching tweets:", error.response ? error.response.data : error.message);
        return { success: false, message: error.response?.data || "An error occurred." };
    }
};