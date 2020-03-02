create table goods (
    [vendor] int not null primary key,
    [gender] varchar(6) not null,
    [photo] varchar(255) not null,
    [rating] int not null,
    [price] float not null,
    [discount] float not null, 
    [discount_bool] boolean not null,
    [new] boolean not null,
    [description] text not null,
    [category] varchar(255) not null,
    [color] varchar(255) not null
);

create table availability (
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [vendor] int not null,
    [size]  int not null,
    [number] int not null,

    foreign key (vendor)
       references goods (vendor)
);