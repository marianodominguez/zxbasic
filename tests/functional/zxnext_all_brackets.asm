N equ 0
NN equ 1234

adc a,[hl]
adc a,[ix+N]
adc a,[iy+N]
add a,[hl]
add a,[ix+N]
add a,[iy+N]
and [hl]
and [ix+N]
and [iy+N]
bit 0,[hl]
bit 1,[hl]
bit 2,[hl]
bit 3,[hl]
bit 4,[hl]
bit 5,[hl]
bit 6,[hl]
bit 7,[hl]
bit 0,[ix+N]
bit 1,[ix+N]
bit 2,[ix+N]
bit 3,[ix+N]
bit 4,[ix+N]
bit 5,[ix+N]
bit 6,[ix+N]
bit 7,[ix+N]
bit 0,[iy+N]
bit 1,[iy+N]
bit 2,[iy+N]
bit 3,[iy+N]
bit 4,[iy+N]
bit 5,[iy+N]
bit 6,[iy+N]
bit 7,[iy+N]
cp [hl]
cp [ix+N]
cp [iy+N]
dec [hl]
dec [ix+N]
dec [iy+N]
ex [sp],hl
ex [sp],ix
ex [sp],iy
in a,[c]
in a,[N]
in b,[c]
in c,[c]
in d,[c]
in e,[c]
in h,[c]
in l,[c]
inc [hl]
inc [ix+N]
inc [iy+N]
jp [hl]
jp [ix]
jp [iy]
ld [bc],a
ld [de],a
ld [hl],a
ld [hl],c
ld [hl],b
ld [hl],e
ld [hl],d
ld [hl],h
ld [hl],l
ld [hl],N
ld [ix+N],a
ld [ix+N],c
ld [ix+N],b
ld [ix+N],e
ld [ix+N],d
ld [ix+N],h
ld [ix+N],l
ld [ix+N],N
ld [iy+N],a
ld [iy+N],c
ld [iy+N],b
ld [iy+N],e
ld [iy+N],d
ld [iy+N],h
ld [iy+N],l
ld [iy+N],N
ld [NN],a
ld [NN],bc
ld [NN],de
ld [NN],hl
ld [NN],ix
ld [NN],iy
ld [NN],sp
ld a,[bc]
ld a,[de]
ld a,[hl]
ld a,[ix+N]
ld a,[iy+N]
ld a,[NN]
ld b,[hl]
ld b,[ix+N]
ld b,[iy+N]
ld bc,[NN]
ld c,[hl]
ld c,[ix+N]
ld c,[iy+N]
ld d,[hl]
ld d,[ix+N]
ld d,[iy+N]
ld de,[NN]
ld e,[hl]
ld e,[ix+N]
ld e,[iy+N]
ld h,[hl]
ld h,[ix+N]
ld h,[iy+N]
ld hl,[NN]
ld ix,[NN]
ld iy,[NN]
ld l,[hl]
ld l,[ix+N]
ld l,[iy+N]
ld sp,[NN]
or [hl]
or [ix+N]
or [iy+N]
out [c],a
out [c],b
out [c],c
out [c],d
out [c],e
out [c],h
out [c],l
out [N],a
res 0,[hl]
res 1,[hl]
res 2,[hl]
res 3,[hl]
res 4,[hl]
res 5,[hl]
res 6,[hl]
res 7,[hl]
res 0,[ix+N]
res 1,[ix+N]
res 2,[ix+N]
res 3,[ix+N]
res 4,[ix+N]
res 5,[ix+N]
res 6,[ix+N]
res 7,[ix+N]
res 0,[iy+N]
res 1,[iy+N]
res 2,[iy+N]
res 3,[iy+N]
res 4,[iy+N]
res 5,[iy+N]
res 6,[iy+N]
res 7,[iy+N]
rl [hl]
rl [ix+N]
rl [iy+N]
rlc [hl]
rlc [ix+N]
rlc [iy+N]
rr [hl]
rr [ix+N]
rr [iy+N]
rrc [hl]
rrc [ix+N]
rrc [iy+N]
sbc a,[hl]
sbc a,[ix+N]
sbc a,[iy+N]
set 0,[hl]
set 1,[hl]
set 2,[hl]
set 3,[hl]
set 4,[hl]
set 5,[hl]
set 6,[hl]
set 7,[hl]
set 0,[ix+N]
set 1,[ix+N]
set 2,[ix+N]
set 3,[ix+N]
set 4,[ix+N]
set 5,[ix+N]
set 6,[ix+N]
set 7,[ix+N]
set 0,[iy+N]
set 1,[iy+N]
set 2,[iy+N]
set 3,[iy+N]
set 4,[iy+N]
set 5,[iy+N]
set 6,[iy+N]
set 7,[iy+N]
sla [hl]
sla [ix+N]
sla [iy+N]
sra [hl]
sra [ix+N]
sra [iy+N]
srl [hl]
srl [ix+N]
srl [iy+N]
sub [hl]
sub [ix+N]
sub [iy+N]
xor [hl]
xor [ix+N]
xor [iy+N]
sll [hl]
sll [ix+N]
sll [iy+N]
jp [c]
