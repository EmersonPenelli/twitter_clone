import { useState, useEffect, useRef } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCalendarAlt, faChartBar, faFilm, faImage, faMapMarkedAlt, faSmile } from '@fortawesome/free-solid-svg-icons';
import { tweet, fetchTweets } from '../../api/tweet_api';
// import Tweet from '../Tweet'; 

const TwiiterForm = ({ onTweet }) => {
    const [tweets, setTweets] = useState([]);
    const textAreaRef = useRef();

    useEffect(() => {
        const loadTweets = async () => {
            const result = await fetchTweets();
            console.log("Tweets fetched:", result);
            if (result.success) {
                setTweets(result.data);
            } else {
                console.error(result.message);
            }
        };
        loadTweets();
    }, []);

    const handleSubmit = async () => {
        const content = textAreaRef.current.value.trim();
        const userId = localStorage.getItem('user_id');

        if (content && userId) { // Verifica se ambos não são nulos
            const result = await tweet(userId, content);
            if (result.success) {
                onTweet(content);
                textAreaRef.current.value = "";
                setTweets([result.data, ...tweets]); // Atualiza os tweets com o novo tweet
            } else {
                console.error(result.message);
            }
        } else {
            console.error("User ID or content is null.");
        }
    };

    return (
        <div className="border-b border-gray-800 p-4">
            <textarea 
                placeholder="What's happening ?" 
                className="w-full bg-transparent text-white text-xl resize-none outline-none" 
                ref={textAreaRef}
            />
            <div className='flex justify-between items-center mt-4'>
                <div className='flex space-x-4'>
                    <div><FontAwesomeIcon icon={faImage} className="text-blue-400 cursor-pointer" /></div>
                    <div><FontAwesomeIcon icon={faFilm} className="text-blue-400 cursor-pointer" /></div>
                    <div><FontAwesomeIcon icon={faChartBar} className="text-blue-400 cursor-pointer" /></div>
                    <div><FontAwesomeIcon icon={faSmile} className="text-blue-400 cursor-pointer" /></div>
                    <div><FontAwesomeIcon icon={faCalendarAlt} className="text-blue-400 cursor-pointer" /></div>
                    <div><FontAwesomeIcon icon={faMapMarkedAlt} className="text-blue-400 cursor-pointer" /></div>
                </div>
                <button 
                    className='bg-blue-400 text-white font-bold px-4 py-2 rounded-full hover:bg-blue-600 transition duration-200' 
                    onClick={handleSubmit}
                >
                    Tweet
                </button>
            </div>

            {/* <div className="mt-4">
                {tweets.map((tweet) => (
                    <Tweet key={tweet.id} tweet={tweet} /> 
                ))}
            </div> */}
        </div>
    );
}

export default TwiiterForm;
