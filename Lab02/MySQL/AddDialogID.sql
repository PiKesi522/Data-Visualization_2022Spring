CREATE DEFINER=`root`@`localhost` PROCEDURE `AddDialogID`()
BEGIN
	DECLARE seq INT;
	DECLARE p_text VARCHAR(255);
	DECLARE pointer CURSOR FOR SELECT text FROM dialog;
	DECLARE EXIT HANDLER FOR NOT FOUND CLOSE pointer;
	
	OPEN pointer;
	SET seq = 1;
	REPEAT
		FETCH pointer INTO p_text;
		UPDATE dialog SET dialog.id = seq WHERE dialog.text = p_text;
		SET seq = seq + 1;
	UNTIL 0 END REPEAT;
	CLOSE pointer;
END
