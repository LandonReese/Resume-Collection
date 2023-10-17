// List Available Books
import React, { useState, useEffect } from "react";

function ListAvailableBooks() {
  const [books, setBooks] = useState([]);

  const loadAllBooks = () => {
    fetch("http://localhost:5000/books")
      .then((res) => res.json())
      .then((data) => setBooks(data));
  };

  useEffect(() => {
    loadAllBooks();
  }, []);

  return (
    <div>
      <h2>Available Books</h2>
      <ul>
        {books
          .filter((book) => book.avail)
          .map((book) => (
            <li key={book._id}>
              {book.title} by {book.author}. ID: {book._id}
            </li>
          ))}
      </ul>
      <button onClick={loadAllBooks}>Load All Books</button>
    </div>
  );
}

export default ListAvailableBooks;