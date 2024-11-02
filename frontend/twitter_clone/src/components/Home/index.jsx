import React, { useState, useEffect } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'

import Sidebar from '../Sidebar';
import TwitterForm from '../TwitterForm';
import Tweet from '../Tweet';

import { v4 } from "uuid"
import { getAvatar, getRandomImage } from '../../utils/generateImages';

import TrendItem from '../TrendItem';
import FollowItem from '../FollowItem';

const Home = () => {
    const [tweets, setTweets] = useState([]);

    useEffect(() => {
        const interval = setInterval(() => {
                addNewRandomTweets()
        }, 5000);
        return () => clearInterval(interval)
    }, []) 

    const addNewRandomTweets = () => {
        const randomTweets = [
            "Hoje é um ótimo dia para aprender algo novo!",
            "Aproveitando cada momento, um tweet de cada vez.",
            "Não esqueça de sorrir, isso faz toda a diferença!",
            "Qual é a sua música favorita hoje?",
            "Se você pudesse viajar para qualquer lugar, para onde iria?",
            "A vida é cheia de pequenas alegrias, aproveite!",
            "O que você está lendo atualmente? Recomendações?",
            "Dicas para um dia produtivo: organize-se e foque!",
            "Café ou chá? Qual a sua escolha para começar o dia?",
            "Hoje é dia de compartilhar gratidão. O que você agradece?"
        ];

        const randomTweet = randomTweets[Math.floor(Math.random() * randomTweets.length)]

        addNewTweet(randomTweet, Math.random() > 0.7)
    }

    const addNewTweet = (content, includeImage = false) => {
        const newTweet = {
            id: v4(),
            name: "User",
            username: `user${Math.floor(Math.random() * 1000)}`,
            avatar: getAvatar(`user${Math.floor(Math.random() * 1000)}@email.com`),
            content,
            time: new Date().toLocaleString([], {
                hour: '2-digit',
                minute: '2-digit'
            }),
            image: includeImage ? getRandomImage() : null,
            likes: 0,
            retweets: 0,
            comments: 0,
        }

        setTweets((prevTweets) => [newTweet, ...prevTweets])
    }

    return (
        <div className='flex mx-auto max-w-7xl'>
            <Sidebar />
            <main className='flex-grow border-l border-r border-gray-700 max-w-xl'>
                <header className='sticky top-0 z-10 bg-twitter-background bg-opacity-80 backdrop-blur-sm'>
                    <h2 className='px-4 py-3 text-xl font-bold'>For you</h2>
                </header>
                <TwitterForm onTweet={(content) => addNewTweet(content, Math.random() > 0.6)} />
                <div>
                    {tweets.map(tweet => (
                        <Tweet key={tweet.id} tweet={tweet} />
                    ))}
                </div>
            </main>
            <aside className='hidden xl:block w-80 px-4'>
                <div className='sticky top-0 pt-2'>
                    <div className='relative'>
                        <FontAwesomeIcon icon={faSearch} className='absolute top-3 left-3 text-grey-500' />
                        <input placeholder='Search Twitter' className='w-full bg-gray-800 text-white rounded-full outline-none py-2 pl-10 pr-4' />
                    </div>

                    <div className='bg-gray-800 rounded-xl mt-4 p-4'>
                        <h2 className='font-bold text-xl mb-4'>Subscribe to Premium</h2>
                        <p className='text-gray-500 mb-4'>Subscribe to unlock new features and if elegible, receive a share of ads revenue.</p>
                        <button className='bg-twitter-blue text-white font-bold py-2 px-4 rounded-full hover:bg-blue-600 transition durantion-200'>Subscribe</button>
                    </div>

                    <div className='bg-gray-800 rounded-xl mt-4 p-4'>
                        <h2 className='font-bold text-xl mb-4'>What's happening</h2>
                        <TrendItem category="NFL • LIVE" name="Cardinals at Bills" tweetCount={undefined} />
                        <TrendItem category="Sports • Trending" name="Cardinals at Bills" tweetCount={undefined} />
                        <TrendItem category="Sports • Trending" name="Kyle Dugger" tweetCount={undefined} />
                        <TrendItem category="Sports • Trending" name="Anthony Richardson" tweetCount="12,111" />
                        <TrendItem category="Sports • Trending" name="Bryce Young" tweetCount="5,621" />
                        <TrendItem category="Sports • Trending" name="Daboll" tweetCount="1,334" />
                    </div>
                    <div className='bg-gray-800 rounded-xl mt-4 p-4'>
                        <h2 className='font-bold text-xl mb-4'>Who to follow</h2>
                        <FollowItem name="Bill Gates" username="Billgates" />
                        <FollowItem name="Will Smith" username="WillSmith" />
                        <FollowItem name="Analice Leite" username="AnaliceLeite" />
                        <FollowItem name="Luis Gustavo" username="LuisGustavo" />
                    </div>
                </div>
            </aside>
        </div>
    );
}

export default Home