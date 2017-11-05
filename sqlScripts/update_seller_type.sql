CREATE OR REPLACE PROCEDURE update_seller_type IS

  fetched_seller_type VARCHAR2(20) := '';
  BEGIN
    FOR rec IN (SELECT seller_id, COUNT(seller_id) AS counter FROM car_transaction GROUP BY seller_id)
    LOOP
        SELECT seller.seller_type INTO fetched_seller_type
        FROM seller WHERE seller.seller_id = rec.seller_id;

        IF rec.counter > 2 AND fetched_seller_type NOT IN ('company') THEN
            UPDATE seller SET seller.seller_type = 'tradesman' WHERE rec.seller_id = seller.seller_id;
        ELSIF rec.counter <= 2 AND fetched_seller_type NOT IN ('company') THEN
            UPDATE seller SET seller.seller_type = 'individual' WHERE rec.seller_id = seller.seller_id;
        END IF;    
    END LOOP;

    UPDATE seller SET seller.seller_type = 'individual' WHERE seller.seller_type = 'null';   

  END;
 /
 --call update_seller_type()