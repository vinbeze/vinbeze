// Lich pixel sprite. Half body mirrored, overlays for arms/staff/flame.
const PAL = {
  K:'#06040a', D:'#020104', R:'#160d22', r:'#25163a', h:'#3b2759', l:'#57407e',
  S:'#e4dbc0', s:'#9f9476', t:'#5a523c', E:'#c8ff8a', e:'#5fe02e',
  G:'#c99a2e', g:'#6e5212',
  B:'#5b4632', b:'#2e2117', O:'#f0ffd8', o:'#8cf04a', q:'#2f8a18'
};
const OX = 12, OY = 4, W = 72, H = 68;
const HALF = [
'.......................G',
'.......................G',
'..................G...GG',
'..............G...G...GG',
'..K...........G..GG..GGE',
'..KK..........GG.GG.GGEE',
'..KlK.........GGGGGGGGEE',
'..KlRK......KRgggggggggE',
'..KhlRK....KRrKKKKKKKKKK',
'..KhlRK...KRrrKDDDDDDDDD',
'..KhlRRK..KRrhKDDDtttttt',
'..KhhlRK.KRrhKDDtttsssss',
'..KRhlRRKKRrhKDtssssSSSS',
'..KRhhlRKKRrhKDtsSSSSSSS',
'..KRhhlRRKRrhKDsKKSSSSSS',
'..KRRhlRRKRrhKDsKKKKSSSS',
'..KRRhhlRKRrhKDsKEEKKKSS',
'..KRRhhlRKRrhKDsSKEEEKKS',
'..KRRRhlRKRrhKDssSKKKKKS',
'..KRRRhhRKRrhKDDsSSSSSSK',
'..KRRRhhRKRrhKDDtsSSSSKK',
'..KRRRRhRKRrhKDDtssSSSSS',
'..KRRRRhRKRrhKDDDtsSSSSS',
'..KRRRRhRKRrhKDDDKSKSKSK',
'..KRRRRhRKRrhKDDDKSKSKSK',
'..KRRRRRRKRrhKDDDDtSSSSS',
'.S.KRRRRRKRrhrKDDDDtssss',
'.SS.KRRRRKRrhhrKDDDDDDts',
'.SSs.KRRKRrhrrrKDDDDDDDD',
'KSSSS.KKRrhrrrrrKDDDDDDD',
'KSSSSSKRRrhrrrrrrKDDSDSD',
'KsSSSSSKRhhrrrrrrKDSDDDD',
'KssSSSsKRhrrrrrrrKDDSSSS',
'.KssssKKRrhrrrrrrKDDDDDD',
'..KKKKRRrhrrrrrrrKDSSSSS',
'...KRRrrhrrrrrrrrKDDDDDK',
'...KRrrhhrrrrrrrrrKDSSSS',
'...KRrrhrrrrrrrrrrKDDDDK',
'...KRrhhrrrrrrrrrrrKKKKK',
'...KRrhrrrrrrrrrrrrRRRRR',
'...KRrhrrrrrrrrrrrRRRRRR',
'...KggggggggggggggggKSSS',
'...KRrhrrrrrrrrrrrRRRKSS',
'...KRrhrrrrrrrrrrRRRRrRR',
'..KRrhhrrrrrrrrRRRRRrRRR',
'..KRrhrrrrrrrrRRRRRrRRRR',
'..KRrhrrrrrrrRRRRRrRRRRR',
'.KRrhhrrrrrrRRRRRrRRRRRR',
'.KRrhrrrrrrRRRRRrRRRRRRR',
'.KRrhrrrrrRRRRRRrRRRRRRR',
'.KRhhrrrrRRRRRRrRRRRRRRR',
'KRrhrrrrRRRRRRrRRRRRRRRR',
'KRrhrrrRRRRRRRrRRRRRRRRR',
'KRhrrrrRRRRRRrRRRRRRRRRR',
'KRhrrrRRRRRRRrRRRRRRRRRR',
'KRrrrRRRRRRRrRRRRRRRRRRR',
'KRrKRRRRKRRRrRRKRRRRKRRR',
'KRK.KRRK.KRrRK..KRRK.KRR',
'KK...KK..KRRK....KK..KRK',
'..........KRK.........K.',
'...........K............',
];
const LEFT_ARM = {x:1, y:21, rows:[
'.S.S.S........','.S.S.S.S......','.S.S.S.S......','.SSSSSsS......','..sSSSs.......',
'...sSs........','....Ss........','....sS........','.....Ss.......','.....sS.......',
'....KRRK......','...KRrrRK.....','...KRhrrRK....','..KRhrrrrRK...','..KRhrrrrrRKK.',
'.KRhrrrrrrrRRK','.KRhrrrrrrrRRK','KRhrrrrrrrRRK.','KRhrrrrrrRRK..','KRrrrrrRRKK...',
'KRrKRRKRK.....','KK..KK.K......']};
const RIGHT_SLEEVE = {x:54, y:32, rows:[
'..KK........','.KRRK.......','.KRrRK......','.KRrrRK.....','.KRrrrRK....','.KRrhrrRK...',
'.KRrhrrrRK..','.KRrhrrrrRK.','.KRrhrrrrRRK','.KRrrhrrRRRK','.KRrrrRRKKK.','.KKRRKK.....']};
const ORB = {x:60, y:0, rows:[
'B........B','Bb..qq..bB','.B.qooq.B.','.BqoOOoqB.','.BqOOOOqB.',
'.BqoOOoqB.','..BqooqB..','..BBqqBB..','...BbbB...','....Bb....']};
const HAND = {x:62, y:39, rows:['.SSSS.','SsSSsS','SSssSS','.sSSs.']};
const FLAME_A = ['....o...','...oo...','..oOo.o.','..oOOoo.','.oOOOOo.','.oOOOOo.','..oOOo..','...oo...'];
const FLAME_B = ['...o....','...oo.o.','..ooOo..','.oOOOo..','.oOOOOo.','..oOOOo.','..oOOo..','...oo...'];
const FLAME_POS = {x:1, y:13};
const EYES = []; // filled in build: positions of 'E' pixels in face
function blank(){ return Array.from({length:H},()=>Array(W).fill('.')); }
function stamp(g, s){ s.rows.forEach((row,yy)=>[...row].forEach((c,xx)=>{ if(c!=='.') g[s.y+yy][s.x+xx]=c; })); }
function build(){
  const g = blank();
  stamp(g, LEFT_ARM); stamp(g, RIGHT_SLEEVE);
  for(let y=10;y<H-2;y++){ g[y][64]='B'; g[y][65]='b'; }
  HALF.forEach((row,y)=>{ if(row.length!==24) throw new Error('row '+y+' len '+row.length);
    [...row].forEach((c,x)=>{ if(c!=='.'){ g[OY+y][OX+x]=c; g[OY+y][OX+47-x]=c; } }); });
  stamp(g, ORB); stamp(g, HAND);
  return g;
}
return {PAL,W,H,OX,OY,build,FLAME_A,FLAME_B,FLAME_POS};
