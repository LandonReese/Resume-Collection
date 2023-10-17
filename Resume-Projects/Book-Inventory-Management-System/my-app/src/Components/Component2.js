// List Checked out Books
import React, { useState, useEffect } from "react";

function ListUnavailableBooks() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/books")
      .then((res) => res.json())
      .then((data) => setBooks(data.filter((book) => !book.avail)));
  }, []);

  return (
    <div>
      <h2>Checked Out Books</h2>
      <ul>
        {books.map((book) => (
          <li key={book._id}>
            {book.title} by {book.author}. ID: {book._id}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ListUnavailableBooks;
