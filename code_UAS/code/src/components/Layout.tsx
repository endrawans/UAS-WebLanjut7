import React from "react";

const Layout = ({ children }) => {
  return (
    <div>
      <nav style={{ padding: 20, background: "#eee" }}>
        <h2>Library Admin</h2>
      </nav>

      <main style={{ padding: 20 }}>
        {children}
      </main>
    </div>
  );
};

export default Layout;
