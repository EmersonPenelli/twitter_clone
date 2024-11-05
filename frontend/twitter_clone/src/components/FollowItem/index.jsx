import { useState, useEffect } from "react";
import { getAvatar } from "../../utils/generateImages";

const FollowItem = ({ name, username, userId, isFollowing, onToggleFollow }) => {
    const [following, setFollowing] = useState(isFollowing);
    const avatar = getAvatar(`${name + Math.floor(Math.random() * 1000)}@email.com`);

    useEffect(() => {
        setFollowing(isFollowing);
    }, [isFollowing]);

    const handleToggleFollow = async () => {
        await onToggleFollow(userId);
        setFollowing(prev => !prev); 
    };

    return (
        <div className="flex items-center justify-between py-3 hover:bg-gray-800 transition duration-200">
            <div className="flex items-center">
                <img src={avatar} alt="user avatar" className="w-12 h-12 rounded-full mr-3" />
                <div>
                    <p className="font-bold">{name}</p>
                    <p className="text-gray-500">{username}</p>
                </div>
            </div>
            <button
                className={`text-black font-bold px-4 py-2 rounded-full transition duration-200 ${following ? "bg-gray-300" : "bg-white hover:bg-gray-300"
                    }`}
                onClick={handleToggleFollow}
            >
                {following ? "Following" : "Follow"}
            </button>
        </div>
    );
};

export default FollowItem;
