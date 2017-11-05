CREATE OR REPLACE PROCEDURE show_seller_stats IS
  BEGIN
    FOR rec IN (SELECT seller_id, COUNT(seller_id) AS counter FROM car_transaction GROUP BY seller_id)
    LOOP
        DBMS_OUTPUT.put_line ('SELLER_ID: ' || rec.seller_id || ' TRANSACTIONS: ' || rec.counter);
    END LOOP;
  END;
 /
 --call show_seller_stats()