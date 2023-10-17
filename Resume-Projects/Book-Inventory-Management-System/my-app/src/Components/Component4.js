// Check in a book
import React, { useState, useEffect } from "react";

const url = "http://localhost:5000/books";

function CheckInBooks() {
  const [books, setBooks] = useState([]);

  const loadAllBooks = () => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setBooks(data.filter((book) => !book.avail)));
  };

  useEffect(() => {
    loadAllBooks();
  }, []);

  // This function will handle setting avail to true
  const checkin = (id) => {
    console.log(`Checking in book with ID ${id}`);
    fetch(`${url}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ avail: true }),
    })
      .then((res) => {
        if (res.ok) {
          console.log(`Book with ID ${id} checked in successfully`);
          loadAllBooks(); // Reload all books after checkin
        } else {
          throw new Error("Book not found or already checked in");
        }
      })
      .catch((err) => console.error(err));
      window.location.reload();
  };

  return (
    <div>
      <h2>Check In a Book</h2>
      <ul>
        {books.map((book) => (
          <li key={book._id}>
            {book.title} by {book.author}. ID: {book._id}
            <button onClick={() => checkin(book._id)}>Check In</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CheckInBooks;