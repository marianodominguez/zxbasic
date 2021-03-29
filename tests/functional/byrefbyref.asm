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
_v:
	DEFB 00
core.ZXBASIC_USER_DATA_END:
core.__MAIN_PROGRAM__:
	ld hl, _v
	push hl
	call _primero
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
_primero:
	push ix
	ld ix, 0
	add ix, sp
	ld l, (ix+4)
	ld h, (ix+5)
	push hl
	call _segundo
_primero__leave:
	ld sp, ix
	pop ix
	exx
	pop hl
	ex (sp), hl
	exx
	ret
_segundo:
	push ix
	ld ix, 0
	add ix, sp
	ld h, (ix+5)
	ld l, (ix+4)
	ld (hl), 2
_segundo__leave:
	ld sp, ix
	pop ix
	exx
	pop hl
	ex (sp), hl
	exx
	ret
	;; --- end of user code ---
	END
