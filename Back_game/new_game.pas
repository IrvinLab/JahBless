unit new_game;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ExtCtrls;

type
  TForm2 = class(TForm)
    lbl1: TLabel;
    btn1: TButton;
    btn2: TButton;
    btn3: TButton;
    btn4: TButton;
    btn5: TButton;
    btn6: TButton;
    btn7: TButton;
    btn8: TButton;
    btn9: TButton;
    btn10: TButton;
    btn11: TButton;
    btn12: TButton;
    btn13: TButton;
    btn14: TButton;
    btn15: TButton;
    btn16: TButton;
    btn17: TButton;
    btn18: TButton;
    btn19: TButton;
    btn20: TButton;
    btn21: TButton;
    btn22: TButton;
    btn23: TButton;
    btn24: TButton;
    imgAvatar: TImage;
    mmo1: TMemo;
    btn25: TButton;
    procedure btn1Click(Sender: TObject);
    procedure btn2Click(Sender: TObject);
    procedure btn3Click(Sender: TObject);
    procedure btn4Click(Sender: TObject);
    procedure btn5Click(Sender: TObject);
    procedure btn6Click(Sender: TObject);
    procedure btn7Click(Sender: TObject);
    procedure btn8Click(Sender: TObject);
    procedure btn9Click(Sender: TObject);
    procedure btn10Click(Sender: TObject);
    procedure btn11Click(Sender: TObject);
    procedure btn12Click(Sender: TObject);
    procedure btn13Click(Sender: TObject);
    procedure btn14Click(Sender: TObject);
    procedure btn15Click(Sender: TObject);
    procedure btn16Click(Sender: TObject);
    procedure btn17Click(Sender: TObject);
    procedure btn18Click(Sender: TObject);
    procedure btn19Click(Sender: TObject);
    procedure btn20Click(Sender: TObject);
    procedure btn21Click(Sender: TObject);
    procedure btn22Click(Sender: TObject);
    procedure btn23Click(Sender: TObject);
    procedure btn24Click(Sender: TObject);
    procedure btn25Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form2: TForm2;
    hero : Integer;

implementation

uses game;

{$R *.dfm}

procedure TForm2.btn1Click(Sender: TObject);


  // Герои
// 50 - Аками, 51 - Артес, 52 - Владыка Смерти, 53 - Детерок, 54 - Джепотай, 55 - Фарион
// 56 - Гаритос, 57 - Гендальф, 58 - Илидан, 59 - Джайна
// 60 - Келл, 61 - Келл Тузед, 62 - Магерион, 63 - Мефистофор, 64 - Паладин, 65 - Прадмур
// 66 - Саргарас, 67 - Саурон, 68 - Сильвана, 69 - Тралл, 70 - Утер, 71 - Варомир
// 72 - Вул Джин, 73 - Задира
begin
 hero := 50;
 ish[9,12] := hero;
 imgAvatar.Picture.LoadFromFile('.\Images\akami.jpg');
 mmo1.Text:='Аками' +#13#10;
 mmo1.Text:=mmo1.Text + 'Здор: 165'+#13#10;
 mmo1.Text:=mmo1.Text + 'Мана: 150'+#13#10;
 mmo1.Text:=mmo1.Text + 'Опыт: 100'+#13#10;
 mmo1.Text:=mmo1.Text + #13#10;
 mmo1.Text:=mmo1.Text + 'Сила: 15'+#13#10;
 mmo1.Text:=mmo1.Text + 'Защита: 5'+#13#10;
 mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
 mmo1.Text:=mmo1.Text + 'Удач: 10'+#13#10;
 mmo1.Text:=mmo1.Text + #13#10;
 mmo1.Text:=mmo1.Text + 'Описание: Лидер тёмных эльфов. '+#13#10;
 mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
 mmo1.Text:=mmo1.Text + 'Мощь смерти'+#13#10;
 mmo1.Text:=mmo1.Text + 'Молния'+#13#10;
end;

procedure TForm2.btn2Click(Sender: TObject);
begin
  hero := 51;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\artes.jpg');
mmo1.Text:='Артес'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 205'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 100'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 75'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 21'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 8'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 6'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Сын короля людей, главнокомандующий армии порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь порядка'+#13#10;
end;

procedure TForm2.btn3Click(Sender: TObject);
begin
  hero := 52;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\deathOwner.jpg');
mmo1.Text:='Владыка Смерти'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 175'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 135'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 17'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 2'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 3'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Высший некромант нежити и её основатель'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Проклятье'+#13#10;
mmo1.Text:=mmo1.Text + 'Поцелуй смерти'+#13#10;
mmo1.Text:=mmo1.Text + 'Восстановить скелетов'+#13#10;
end;

procedure TForm2.btn4Click(Sender: TObject);
begin
  hero := 53;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\deterok.jpg');
mmo1.Text:='Детерок'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 150'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 120'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 25'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 3'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 2'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Обросший плотью боевой скелет'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Отравление'+#13#10;
end;

procedure TForm2.btn5Click(Sender: TObject);
begin
hero := 54;
ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\djepotai.jpg');
mmo1.Text:='Джепотай'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 170'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 100'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 75'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 15'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 8'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Воевода троллей'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Молния'+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь предков'+#13#10;
end;

procedure TForm2.btn6Click(Sender: TObject);
begin
  hero := 55;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\farion.jpg');
mmo1.Text:='Фарион'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 190'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 170'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 13'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Лидер магического круга орков'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Проклятье'+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь предков'+#13#10;
mmo1.Text:=mmo1.Text + 'Сжиграние маны'+#13#10;
end;

procedure TForm2.btn7Click(Sender: TObject);
begin
  hero := 56;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\garitos.jpg');
mmo1.Text:='Гаритос'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 220'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 150'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 110'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 19'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 7'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 6'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Высший боевой эльф'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь природы'+#13#10;
mmo1.Text:=mmo1.Text + 'Сжиграние маны'+#13#10;
end;

procedure TForm2.btn8Click(Sender: TObject);
begin
  hero := 57;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\gendalf.jpg');
mmo1.Text:='Гендальф'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 160'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 13'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 3'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Верховный маг гильдии порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Доспехи феникса'+#13#10;
mmo1.Text:=mmo1.Text + 'Обман'+#13#10;
mmo1.Text:=mmo1.Text + 'Молния'+#13#10;
mmo1.Text:=mmo1.Text + 'Лечение'+#13#10;

end;

procedure TForm2.btn9Click(Sender: TObject);
begin
  hero := 58;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\illidan.jpg');
mmo1.Text:='Иллидан'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 90'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 80'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 18'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 7'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Высший боевой темный эльф'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Кровожадность'+#13#10;
mmo1.Text:=mmo1.Text + 'Проклятье'+#13#10;
end;

procedure TForm2.btn10Click(Sender: TObject);
begin
  hero := 59;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\jaina.jpg');
mmo1.Text:='Джайна'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 150'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 110'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 15'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 7'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Колдун гильдии порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Лечение'+#13#10;
mmo1.Text:=mmo1.Text + 'Рассеять чары'+#13#10;

end;

procedure TForm2.btn11Click(Sender: TObject);
begin
  hero := 60;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\kell.jpg');
mmo1.Text:='Келл'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 190'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 150'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 100'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 19'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 7'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Боевой темный эльф'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Лечение'+#13#10;
end;

procedure TForm2.btn12Click(Sender: TObject);
begin
  hero := 61;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\kelTuZed.jpg');
mmo1.Text:='Келл Тузед'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 220'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 170'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 150'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 20'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Демон'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Кража магии'+#13#10;
mmo1.Text:=mmo1.Text + 'Поцелуй смерти'+#13#10;
end;

procedure TForm2.btn13Click(Sender: TObject);
begin
  hero := 62;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\magerion.jpg');
mmo1.Text:='Магерион'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 220'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 150'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 125'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 19'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 8'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Демон'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Пленить душу'+#13#10;
mmo1.Text:=mmo1.Text + 'Проклятье'+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь смерти'+#13#10;
end;

procedure TForm2.btn14Click(Sender: TObject);
begin
  hero := 63;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\mefistofor.jpg');
mmo1.Text:='Мефистофор'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 155'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 180'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 14'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 8'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Скелет постигший некромантию'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Восстановить скелетов'+#13#10;
mmo1.Text:=mmo1.Text + 'Сжигание маны'+#13#10;
mmo1.Text:=mmo1.Text + 'Огненная сфера'+#13#10;
end;

procedure TForm2.btn15Click(Sender: TObject);
begin
  hero := 64;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\paladin.jpg');
mmo1.Text:='Паладин'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 130'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 105'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 23'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 10'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 3'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Генерал армии порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Рассеять чары'+#13#10;

end;

procedure TForm2.btn16Click(Sender: TObject);
begin
  hero := 65;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\pradmur.jpg');
mmo1.Text:='Прадмур'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 175'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 130'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 12'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 6'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 7'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Волшебница гильдии порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Рассеять чары'+#13#10;
mmo1.Text:=mmo1.Text + 'Лечение'+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Огненная сфера'+#13#10;
end;

procedure TForm2.btn17Click(Sender: TObject);
begin
  hero := 66;
  ish[9,12] := hero;
//  imgAvatar.Picture.LoadFromFile('.\Images\sargaras.png');
mmo1.Text:='Саргарас - Его пока нет'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 180'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 180'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 95'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 18'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 7'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Духовный наставник эльфов'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь природы'+#13#10;
mmo1.Text:=mmo1.Text + 'Обман'+#13#10;
mmo1.Text:=mmo1.Text + 'Лунный обряд'+#13#10;
end;

procedure TForm2.btn18Click(Sender: TObject);
begin
  hero := 67;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\sauron.jpg');
mmo1.Text:='Саурон'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 205'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 145'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 15'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 9'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 6'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Некромант полудемон, повелитель нежити'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Пронзающая смерть'+#13#10;
mmo1.Text:=mmo1.Text + 'Добить и воскресить'+#13#10;
mmo1.Text:=mmo1.Text + 'Пронзающий крик'+#13#10;
mmo1.Text:=mmo1.Text + 'Восстановить скелетов'+#13#10;
end;

procedure TForm2.btn19Click(Sender: TObject);
begin
  hero := 68;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\silvana.jpg');
mmo1.Text:='Сильвана'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 175'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 120'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 105'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 19'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 6'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Эльфийский боевой маг'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь природы'+#13#10;
mmo1.Text:=mmo1.Text + 'Молния'+#13#10;
mmo1.Text:=mmo1.Text + 'Пронзающий крик'+#13#10;
mmo1.Text:=mmo1.Text + 'Лечение'+#13#10;
end;

procedure TForm2.btn20Click(Sender: TObject);
begin
  hero := 69;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\trall.jpeg');
mmo1.Text:='Тралл'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 190'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 115'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 19'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 8'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Вождь орков'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь предков'+#13#10;

end;

procedure TForm2.btn21Click(Sender: TObject);
begin
  hero := 70;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\uter.jpg');
mmo1.Text:='Утер'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 190'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 150'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 125'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 18'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 9'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 3'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Генерал армии порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь порядка'+#13#10;
mmo1.Text:=mmo1.Text + 'Кровожадность'+#13#10;

end;

procedure TForm2.btn22Click(Sender: TObject);
begin
  hero := 71;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\varomir.jpg');
mmo1.Text:='Варомир'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 175'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 130'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 100'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 16'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 7'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 11'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Духовный наставник тёмных эльфов'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Проклятье'+#13#10;
mmo1.Text:=mmo1.Text + 'Пленить душу'+#13#10;
mmo1.Text:=mmo1.Text + 'Яд'+#13#10;
end;

procedure TForm2.btn23Click(Sender: TObject);
begin
  hero := 72;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\vulDjin.jpg');
mmo1.Text:='Вул Джин'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 170'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 200'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 120'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 17'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 5'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 6'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Великий шаман троллей'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Лечение'+#13#10;
mmo1.Text:=mmo1.Text + 'Печать хаоса'+#13#10;
mmo1.Text:=mmo1.Text + 'Огненная сфера'+#13#10;
mmo1.Text:=mmo1.Text + 'Мощь предков'+#13#10;
end;

procedure TForm2.btn24Click(Sender: TObject);
begin
  hero := 73;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\zadira.jpg');
mmo1.Text:='Задира'+#13#10;
mmo1.Text:=mmo1.Text + 'Здор: 195'+#13#10;
mmo1.Text:=mmo1.Text + 'Мана: 160'+#13#10;
mmo1.Text:=mmo1.Text + 'Опыт: 110'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Сила: 19'+#13#10;
mmo1.Text:=mmo1.Text + 'Защита: 9'+#13#10;
mmo1.Text:=mmo1.Text + 'Ходы: 4'+#13#10;
mmo1.Text:=mmo1.Text + 'Удач: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + 'Описание: Главнокомандующий армии орков'+#13#10;
mmo1.Text:=mmo1.Text + 'Владеет заклинаниями: '+#13#10;
mmo1.Text:=mmo1.Text + 'Яд'+#13#10;
mmo1.Text:=mmo1.Text + 'Рассеять чары'+#13#10;
end;

procedure TForm2.btn25Click(Sender: TObject);
begin
Form2.Close;
end;

end.
