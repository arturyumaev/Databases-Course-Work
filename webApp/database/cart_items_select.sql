select *, count(*) as amount from (
    select g.description,
           g.category,
           g.gender,
           c.size,
           g.color,
           g.price * (1 - g.discount) as price,
           c.vendor
    from cart c
    join goods g
    on c.vendor = g.vendor
    where userid = 'MGWdB5xVh7'
) as items
group by vendor, size
having count(*) >= 1