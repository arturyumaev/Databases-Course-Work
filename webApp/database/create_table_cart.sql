create table cart (
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [userid] varchar(10) not null,
    [vendor] int not null,
    [size]  int not null

    foreign key (vendor)
       references goods (vendor)
);