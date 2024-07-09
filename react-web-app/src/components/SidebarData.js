import React from 'react';
// import * as FaIcons from 'react-icons/fa'
import * as AiIcons from 'react-icons/ai'

export const SidebarData = [
    {
        title: 'Home',
        path: '/',
        icon: <AiIcons.AiFillHome />,
        cName: 'nav-text'
    },
    {
        title: 'Manage Clubs',
        path: '/clubs',
        icon: <AiIcons.AiFillTool />,
        cName: 'nav-text'
    },
    {
        title: 'Record Shots',
        path: '/shots',
        icon: <AiIcons.AiOutlinePlus />,
        cName: 'nav-text'
    }
]