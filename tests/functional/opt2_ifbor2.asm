	org 32768
core.__START_PROGRAM:
	di
	push ix
	push iy
	exx
	push hl
	exx
	ld hl, 0
	add hl, sp
	ld (core.__CALL_BACK__), hl
	ei
	jp core.__MAIN_PROGRAM__
core.__CALL_BACK__:
	DEFW 0
core.ZXBASIC_USER_DATA:
	; Defines USER DATA Length in bytes
core.ZXBASIC_USER_DATA_LEN EQU core.ZXBASIC_USER_DATA_END - core.ZXBASIC_USER_DATA
	core..__LABEL__.ZXBASIC_USER_DATA_LEN EQU core.ZXBASIC_USER_DATA_LEN
	core..__LABEL__.ZXBASIC_USER_DATA EQU core.ZXBASIC_USER_DATA
core.ZXBASIC_USER_DATA_END:
core.__MAIN_PROGRAM__:
	call _x
	ld hl, 0
	ld b, h
	ld c, l
core.__END_PROGRAM:
	di
	ld hl, (core.__CALL_BACK__)
	ld sp, hl
	exx
	pop hl
	pop iy
	pop ix
	exx
	ei
	ret
_x:
	push ix
	ld ix, 0
	add ix, sp
	ld hl, 0
	push hl
	inc sp
	ld a, (ix-1)
	or 1
	jp z, _x__leave
	inc (ix-1)
_x__leave:
	ld sp, ix
	pop ix
	ret
	;; --- end of user code ---
	END
