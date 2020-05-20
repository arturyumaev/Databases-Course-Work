create table orders (
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [orderNumber] varchar(9) not null,
    [cartId] varchar(19) not null,
    [name] varchar(255) not null,
    [vendor] int not null,
    [size] int not null,
    [quantity] int not null,
    [email] varchar(255) not null,
    [time] varchar(255) not null
);