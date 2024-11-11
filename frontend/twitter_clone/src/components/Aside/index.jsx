import React, { useState, useEffect } from 'react';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

import { fetchUsers, toggleFollowUser } from '../../api/follow';

import TrendItem from '../TrendItem';
import FollowItem from '../FollowItem';
import { fetchUser, updateUserPremiumStatus } from '../../api/login_api'; // Adicione uma função para buscar o usuário

const Aside = ({ currentUser }) => {
    const [isSubscribed, setSubscribed] = useState(false);
    const [users, setUsers] = useState([]);

    useEffect(() => {

        const fetchPremiumStatus = async () => {
            const userId = localStorage.getItem('user_id');
            const response = await fetchUser(userId);
            if (response.success) {
                setSubscribed(response.data.is_premium);
            } else {
                console.error(response.message);
            }
        };

        const loadUsers = async () => {
            const response = await fetchUsers();
            if (response.success) {
                setUsers(response.data.map(user => ({
                    ...user,
                    isFollowing: user.is_following
                })));
            } else {
                console.error(response.message);
            }
        };

        fetchPremiumStatus(); 
        loadUsers();
    }, [currentUser]);

    const handleToggleFollow = async (userId) => {
        const response = await toggleFollowUser(userId);
        if (response.success) {
            setUsers(users.map(user =>
                user.id === userId ? { ...user, isFollowing: response.following } : user
            ));
        } else {
            console.error(response.message);
        }
    };

    const handleSubscribe = async () => {
        const userId = localStorage.getItem('user_id');

        const response = await updateUserPremiumStatus(userId);
        if (response.success) {
            setSubscribed(response.data.is_premium);
        } else {
            console.error(response.message);
        }
    };

    return (
        <aside className='hidden xl:block w-80 px-4'>
            <div className='sticky top-0 pt-2'>
                <div className='relative'>
                    <FontAwesomeIcon icon={faSearch} className='absolute top-3 left-3 text-grey-500' />
                    <input placeholder='Search Twitter' className='w-full bg-gray-800 text-white rounded-full outline-none py-2 pl-10 pr-4' />
                </div>

                <div className='bg-gray-800 rounded-xl mt-4 p-4'>
                    <h2 className='font-bold text-xl mb-4'>Subscribe to Premium</h2>
                    <p className='text-gray-500 mb-4'>Subscribe to unlock new features and if eligible, receive a share of ads revenue.</p>
                    <button
                        className='bg-twitter-blue text-white font-bold py-2 px-4 rounded-full hover:bg-blue-600 transition duration-200'
                        onClick={handleSubscribe}
                    >
                        {isSubscribed ? "Subscribed" : "Subscribe"}
                    </button>
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
                    {users.map((user, index) => (
                        <FollowItem
                            key={user.id || index}
                            name={user.name}
                            username={user.name}
                            userId={user.id}
                            isFollowing={user.isFollowing}
                            onToggleFollow={() => handleToggleFollow(user.id)}
                        />
                    ))}
                </div>
            </div>
        </aside>
    )
}

export default Aside;
