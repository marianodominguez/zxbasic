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
_y:
	DEFB 01h
	DEFB 00h
	DEFB 00h
	DEFB 00h
core.ZXBASIC_USER_DATA_END:
core.__MAIN_PROGRAM__:
	ld hl, (_y)
	ld de, (_y + 2)
	call core.__SGNU32
	ld (0), a
	ld hl, 0
	ld b, h
	ld c, l
core.__END_PROGRAM:
	di
	ld hl, (core.__CALL_BACK__)
	ld sp, hl
	exx
	pop hl
	exx
	pop iy
	pop ix
	ei
	ret
	;; --- end of user code ---
#line 1 "/zxbasic/src/arch/zx48k/library-asm/sgnu32.asm"
	; Returns SGN (SIGN) for 32 bits unsigned integer
	    push namespace core
__SGNU32:
	    ld a, h
	    or l
	    or d
	    or e
	    ret z
	    ld a, 1
	    ret
	    pop namespace
#line 21 "sgnu32.bas"
	END
