import React, { useState, useEffect } from 'react'
import { RentBox } from './RentBox'


export function BookDetail({book, user, setPage}) {
    const [rentBox, setRentBox] = useState(false)

    const showBox = () => {
        if (user.is_authenticated) {
            setRentBox(true)
        }
        else {
            setPage('Login')
        }    
    }
    const hideBox = () => {
        if (rentBox) {
        setRentBox(false)
        }
    }
    useEffect(hideBox, [book])

    return (
        <>
        <div className='book-page' onClick={hideBox}>
            {book.image ? 
            <div>  
                <img className='image' src={book.image} />               
            </div>: ''}
            <div className='book-detail'>
                <h2>{book.title}</h2>
                <h4>Author: {book.author}</h4>
                <p>Categories : {book.category.toString()}</p>
                <p>Year : {book.year}</p>
                <button className='btn-gray' onClick={showBox} disabled={!user.is_authenticated}>Rent this book.</button>
                <p>{book.description}</p>
            </div>
        </div>
        {rentBox && <RentBox hideBox={hideBox} book={book}/>}
        </>
    )
}