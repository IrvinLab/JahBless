unit game;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls, ImgList, Jpeg, ExtCtrls;

type
  TForm1 = class(TForm)
    mmo1: TMemo;
    btn1: TButton;
    btn2: TButton;
    btn3: TButton;
    img00: TImage;
    img01: TImage;
    img02: TImage;
    img03: TImage;
    img04: TImage;
    img05: TImage;
    img06: TImage;
    img07: TImage;
    img08: TImage;
    img09: TImage;
    img0a: TImage;
    img0b: TImage;
    img0c: TImage;
    img0d: TImage;
    img0e: TImage;
    img0f: TImage;
    img0g: TImage;
    img0h: TImage;
    img0i: TImage;
    img0j: TImage;
    img0k: TImage;
    img0l: TImage;
    img0m: TImage;
    img10: TImage;
    img11: TImage;
    img12: TImage;
    img13: TImage;
    img14: TImage;
    img15: TImage;
    img17: TImage;
    img18: TImage;
    img19: TImage;
    img1a: TImage;
    img16: TImage;
    img1b: TImage;
    img1c: TImage;
    img1d: TImage;
    img1e: TImage;
    img1f: TImage;
    img1g: TImage;
    img1h: TImage;
    img1i: TImage;
    img1j: TImage;
    img1k: TImage;
    img1l: TImage;
    img1m: TImage;
    img20: TImage;
    img21: TImage;
    img22: TImage;
    img23: TImage;
    img24: TImage;
    img25: TImage;
    img26: TImage;
    img27: TImage;
    img28: TImage;
    img29: TImage;
    img2a: TImage;
    img2b: TImage;
    img2c: TImage;
    img2d: TImage;
    img2e: TImage;
    img2f: TImage;
    img2g: TImage;
    img2h: TImage;
    img2i: TImage;
    img2j: TImage;
    img2k: TImage;
    img2l: TImage;
    img2m: TImage;
    img30: TImage;
    img31: TImage;
    img32: TImage;
    img33: TImage;
    img34: TImage;
    img35: TImage;
    img36: TImage;
    img37: TImage;
    img38: TImage;
    img39: TImage;
    img3a: TImage;
    img3b: TImage;
    img3c: TImage;
    img3d: TImage;
    img3e: TImage;
    img3f: TImage;
    img3g: TImage;
    img3h: TImage;
    img3i: TImage;
    img3j: TImage;
    img3k: TImage;
    img3l: TImage;
    img3m: TImage;
    img40: TImage;
    img41: TImage;
    img42: TImage;
    img43: TImage;
    img44: TImage;
    img45: TImage;
    img46: TImage;
    img47: TImage;
    img48: TImage;
    img49: TImage;
    img4a: TImage;
    img4b: TImage;
    img4c: TImage;
    img4d: TImage;
    img4e: TImage;
    img4f: TImage;
    img4g: TImage;
    img4h: TImage;
    img4i: TImage;
    img4j: TImage;
    img4k: TImage;
    img4l: TImage;
    img4m: TImage;
    img50: TImage;
    img51: TImage;
    img52: TImage;
    img53: TImage;
    img54: TImage;
    img55: TImage;
    img56: TImage;
    img57: TImage;
    img58: TImage;
    img59: TImage;
    img5a: TImage;
    img5b: TImage;
    img5c: TImage;
    img5d: TImage;
    img5e: TImage;
    img5f: TImage;
    img5g: TImage;
    img5h: TImage;
    img5i: TImage;
    img5j: TImage;
    img5k: TImage;
    img5l: TImage;
    img5m: TImage;
    img60: TImage;
    img61: TImage;
    img62: TImage;
    img63: TImage;
    img64: TImage;
    img65: TImage;
    img66: TImage;
    img67: TImage;
    img68: TImage;
    img69: TImage;
    img6a: TImage;
    img6b: TImage;
    img6c: TImage;
    img6d: TImage;
    img6e: TImage;
    img6f: TImage;
    img6g: TImage;
    img6h: TImage;
    img6i: TImage;
    img6j: TImage;
    img6k: TImage;
    img6l: TImage;
    img6m: TImage;
    img70: TImage;
    img71: TImage;
    img72: TImage;
    img73: TImage;
    img74: TImage;
    img75: TImage;
    img76: TImage;
    img77: TImage;
    img78: TImage;
    img79: TImage;
    img7a: TImage;
    img7b: TImage;
    img7c: TImage;
    img7d: TImage;
    img7e: TImage;
    img7f: TImage;
    img7g: TImage;
    img7h: TImage;
    img7i: TImage;
    img7j: TImage;
    img7k: TImage;
    img7l: TImage;
    img7m: TImage;
    img80: TImage;
    img81: TImage;
    img82: TImage;
    img83: TImage;
    img84: TImage;
    img85: TImage;
    img86: TImage;
    img87: TImage;
    img88: TImage;
    img89: TImage;
    img8a: TImage;
    img8b: TImage;
    img8c: TImage;
    img8d: TImage;
    img8e: TImage;
    img8f: TImage;
    img8g: TImage;
    img8h: TImage;
    img8i: TImage;
    img8j: TImage;
    img8k: TImage;
    img8l: TImage;
    img8m: TImage;
    img90: TImage;
    img91: TImage;
    img92: TImage;
    img93: TImage;
    img94: TImage;
    img95: TImage;
    img96: TImage;
    img97: TImage;
    img98: TImage;
    img99: TImage;
    img9a: TImage;
    img9b: TImage;
    img9c: TImage;
    img9d: TImage;
    img9e: TImage;
    img9f: TImage;
    img9g: TImage;
    img9h: TImage;
    img9i: TImage;
    img9j: TImage;
    img9k: TImage;
    img9l: TImage;
    img9m: TImage;
    imga0: TImage;
    imga1: TImage;
    imga2: TImage;
    imga3: TImage;
    imga4: TImage;
    imga5: TImage;
    imga6: TImage;
    imga7: TImage;
    imga8: TImage;
    imga9: TImage;
    imgaa: TImage;
    imgab: TImage;
    imgac: TImage;
    imgad: TImage;
    imgae: TImage;
    imgaf: TImage;
    imgag: TImage;
    imgah: TImage;
    imgai: TImage;
    imgaj: TImage;
    imgak: TImage;
    imgal: TImage;
    imgam: TImage;
    imgb0: TImage;
    imgb1: TImage;
    imgb2: TImage;
    imgb3: TImage;
    imgb4: TImage;
    imgb5: TImage;
    imgb6: TImage;
    imgb7: TImage;
    imgb8: TImage;
    imgb9: TImage;
    imgba: TImage;
    imgbb: TImage;
    imgbc: TImage;
    imgbd: TImage;
    imgbe: TImage;
    imgbf: TImage;
    imgbg: TImage;
    imgbh: TImage;
    imgbi: TImage;
    imgbj: TImage;
    imgbk: TImage;
    imgbl: TImage;
    imgbm: TImage;
    imgc0: TImage;
    imgc1: TImage;
    imgc2: TImage;
    imgc3: TImage;
    imgc4: TImage;
    imgc5: TImage;
    imgc6: TImage;
    imgc7: TImage;
    imgc8: TImage;
    imgc9: TImage;
    imgca: TImage;
    imgcb: TImage;
    imgcc: TImage;
    imgcd: TImage;
    imgce: TImage;
    imgcf: TImage;
    imgcg: TImage;
    imgch: TImage;
    imgci: TImage;
    imgcj: TImage;
    imgck: TImage;
    imgcl: TImage;
    imgcm: TImage;
    imgd0: TImage;
    imgd1: TImage;
    imgd2: TImage;
    imgd3: TImage;
    imgd4: TImage;
    imgd5: TImage;
    imgd6: TImage;
    imgd7: TImage;
    imgd8: TImage;
    imgd9: TImage;
    imgda: TImage;
    imgdb: TImage;
    imgdc: TImage;
    imgdd: TImage;
    imgde: TImage;
    imgdf: TImage;
    imgdg: TImage;
    imgdh: TImage;
    imgdi: TImage;
    imgdj: TImage;
    imgdk: TImage;
    imgdl: TImage;
    imgdm: TImage;
    btn4: TButton;
    procedure FormCreate(Sender: TObject);
    procedure FormMouseMove(Sender: TObject; Shift: TShiftState; X,
      Y: Integer);
    procedure img00Click(Sender: TObject);
    procedure img0mClick(Sender: TObject);
    procedure btn1Click(Sender: TObject);
    procedure img9bClick(Sender: TObject);
    procedure btn4Click(Sender: TObject);





  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  //Form2: TForm2;
    ish : Array[0..13,0..22] of Integer;
  tek : Array[0..13,0..22] of Integer;
  x : Integer;
  y : Integer;
  n:  Integer;
  // ���������� �������
  Player1Pos : Array[0..13,0..22] of Integer; // ������� ����� (������ ��� ���� ��� ������)
  Player1Lvl : Integer; // Level ����
  Player1Zdor : Integer;
  Player1Mana : Integer;
  Player1Exp : Integer;      // ������� ����
  Player1ExpLvlUp : Integer; // ����������� ���� �� ���������� ������
  Player1Power : Integer;
  Player1Lovk : Integer;
  Player1Ydacha : Integer;
  Player1Zaklin : Array[0..15] of Integer; // ������� � ������� ����������
  Player1Invent : array[0..15] of Integer; // ������� � ��� �����
  Player1Race : Integer; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)

  Player2Pos : Array[0..13,0..22] of Integer; // ������� ����� (������ ��� ���� ��� ������)
  Player2Lvl : Integer; // Level ����
  Player2Zdor : Integer;
  Player2Mana : Integer;
  Player2Exp : Integer;      // ������� ����
  Player2ExpLvlUp : Integer; // ����������� ���� �� ���������� ������
  Player2Power : Integer;
  Player2Lovk : Integer;
  Player2Ydacha : Integer;
  Player2Zaklin : Array[0..15] of Integer; // ������� � ������� ����������
  Player2Invent : array[0..15] of Integer; // ������� � ��� �����
  Player2Race : Integer; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)

  Player3Pos : Array[0..13,0..22] of Integer; // ������� ����� (������ ��� ���� ��� ������)
  Player3Lvl : Integer; // Level ����
  Player3Zdor : Integer;
  Player3Mana : Integer;
  Player3Exp : Integer;      // ������� ����
  Player3ExpLvlUp : Integer; // ����������� ���� �� ���������� ������
  Player3Power : Integer;
  Player3Lovk : Integer;
  Player3Ydacha : Integer;
  Player3Zaklin : Array[0..15] of Integer; // ������� � ������� ����������
  Player3Invent : array[0..15] of Integer; // ������� � ��� �����
  Player3Race : Integer; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)

  Player4Pos : Array[0..13,0..22] of Integer; // ������� ����� (������ ��� ���� ��� ������)
  Player4Lvl : Integer; // Level ����
  Player4Zdor : Integer;
  Player4Mana : Integer;
  Player4Exp : Integer;      // ������� ����
  Player4ExpLvlUp : Integer; // ����������� ���� �� ���������� ������
  Player4Power : Integer;
  Player4Lovk : Integer;
  Player4Ydacha : Integer;
  Player4Zaklin : Array[0..15] of Integer; // ������� � ������� ����������
  Player4Invent : array[0..15] of Integer; // ������� � ��� �����
  Player4Race : Integer; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)

  // ���������� �����   ������ ��������� ������� - ����� ����
  botPos : Array[0..19,0..13,0..22] of Integer; // ������� ���� (������ ��� ���� ��� ������)
  botLvl : array[0..19] of Integer; // Level ����
  botZdor : array[0..19] of Integer;
  botMana : array[0..19] of Integer;
  botExp : array[0..19] of Integer;      // ������� ����
  botExpLvlUp : array[0..19] of Integer; // ����������� ���� �� ���������� ������
  botPower : array[0..19] of Integer;
  botLovk : array[0..19] of Integer;
  botYdacha : array[0..19] of Integer;
  botZaklin : Array[0..19,0..15] of Integer; // ������� � ������� ����������
  botInvent : array[0..19,0..15] of Integer; // ������� � ��� �����
  botProdaet : array[0..19] of Integer; // ���� = 1 �� � ���� ����� �������� ���������
  botVrag : array[0..19] of Integer; // ���� = 1 �� �� ��������� � ����
  botRace : array[0..19] of Integer; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)




implementation

uses new_game;

{$R *.dfm}



procedure TForm1.FormCreate(Sender: TObject);
var
 sas : Integer;
begin
  Randomize;
  // SAS;
  //img00.Picture.LoadFromFile('.\Images\razboinik_32.jpg');
  // img00.Left:=100;
  // img00.Top:=50;
  mmo1.Text:='';
  x:=0;
  y:=0;
  while (x <= 13) and (y <= 22)  do
  begin
    ish[x,y]:=0;
    x:=x+1;
    if x=13 then
    begin
      x:=0;
      y:=y+1;

    end;
    ish[0,21]:=24;
  end;
  img00.Picture.LoadFromFile('.\Images\weed.jpg');
  img01.Picture.LoadFromFile('.\Images\weed.jpg');
  img02.Picture.LoadFromFile('.\Images\weed.jpg');
  img03.Picture.LoadFromFile('.\Images\weed.jpg');
  img04.Picture.LoadFromFile('.\Images\weed.jpg');
  img05.Picture.LoadFromFile('.\Images\weed.jpg');
  img06.Picture.LoadFromFile('.\Images\weed.jpg');
  img07.Picture.LoadFromFile('.\Images\weed.jpg');
  img08.Picture.LoadFromFile('.\Images\weed.jpg');
  img09.Picture.LoadFromFile('.\Images\weed.jpg');
  img0a.Picture.LoadFromFile('.\Images\weed.jpg');
  img0b.Picture.LoadFromFile('.\Images\weed.jpg');
  img0c.Picture.LoadFromFile('.\Images\weed.jpg');
  img0d.Picture.LoadFromFile('.\Images\weed.jpg');
  img0e.Picture.LoadFromFile('.\Images\weed.jpg');
  img0f.Picture.LoadFromFile('.\Images\weed.jpg');
  img0g.Picture.LoadFromFile('.\Images\weed.jpg');
  img0h.Picture.LoadFromFile('.\Images\weed.jpg');
  img0i.Picture.LoadFromFile('.\Images\weed.jpg');
  img0j.Picture.LoadFromFile('.\Images\weed.jpg');
  img0k.Picture.LoadFromFile('.\Images\weed.jpg');
  img0l.Picture.LoadFromFile('.\Images\weed.jpg');
  img0m.Picture.LoadFromFile('.\Images\city_32.jpg'); ish[0,22]:=24; // �����
  img10.Picture.LoadFromFile('.\Images\weed.jpg');
  img11.Picture.LoadFromFile('.\Images\weed.jpg');
  img12.Picture.LoadFromFile('.\Images\weed.jpg');
  img13.Picture.LoadFromFile('.\Images\weed.jpg');
  img14.Picture.LoadFromFile('.\Images\weed.jpg');
  img15.Picture.LoadFromFile('.\Images\weed.jpg');
  img16.Picture.LoadFromFile('.\Images\weed.jpg');
  img17.Picture.LoadFromFile('.\Images\weed.jpg');
  img18.Picture.LoadFromFile('.\Images\weed.jpg');
  img19.Picture.LoadFromFile('.\Images\weed.jpg');
  img1a.Picture.LoadFromFile('.\Images\weed.jpg');
  img1b.Picture.LoadFromFile('.\Images\weed.jpg');
  img1c.Picture.LoadFromFile('.\Images\weed.jpg');
  img1d.Picture.LoadFromFile('.\Images\weed.jpg');
  img1e.Picture.LoadFromFile('.\Images\weed.jpg');
  img1f.Picture.LoadFromFile('.\Images\weed.jpg');
  img1g.Picture.LoadFromFile('.\Images\weed.jpg');
  img1h.Picture.LoadFromFile('.\Images\weed.jpg');
  img1i.Picture.LoadFromFile('.\Images\weed.jpg');
  img1j.Picture.LoadFromFile('.\Images\weed.jpg');
  img1k.Picture.LoadFromFile('.\Images\weed.jpg');
  img1l.Picture.LoadFromFile('.\Images\weed.jpg');
  img1m.Picture.LoadFromFile('.\Images\weed.jpg');
  img20.Picture.LoadFromFile('.\Images\weed.jpg');
  img21.Picture.LoadFromFile('.\Images\weed.jpg');
  img22.Picture.LoadFromFile('.\Images\weed.jpg');
  img23.Picture.LoadFromFile('.\Images\weed.jpg');
  img24.Picture.LoadFromFile('.\Images\weed.jpg');
  img25.Picture.LoadFromFile('.\Images\weed.jpg');
  img26.Picture.LoadFromFile('.\Images\weed.jpg');
  img27.Picture.LoadFromFile('.\Images\weed.jpg');
  img28.Picture.LoadFromFile('.\Images\weed.jpg');
  img29.Picture.LoadFromFile('.\Images\weed.jpg');
  img2a.Picture.LoadFromFile('.\Images\weed.jpg');
  img2b.Picture.LoadFromFile('.\Images\weed.jpg');
  img2c.Picture.LoadFromFile('.\Images\weed.jpg');
  img2d.Picture.LoadFromFile('.\Images\weed.jpg');
  img2e.Picture.LoadFromFile('.\Images\weed.jpg');
  img2f.Picture.LoadFromFile('.\Images\weed.jpg');
  img2g.Picture.LoadFromFile('.\Images\weed.jpg');
  img2h.Picture.LoadFromFile('.\Images\weed.jpg');
  img2i.Picture.LoadFromFile('.\Images\weed.jpg');
  img2j.Picture.LoadFromFile('.\Images\weed.jpg');
  img2k.Picture.LoadFromFile('.\Images\weed.jpg');
  img2l.Picture.LoadFromFile('.\Images\weed.jpg');
  img2m.Picture.LoadFromFile('.\Images\weed.jpg');
  img30.Picture.LoadFromFile('.\Images\weed.jpg');
  img31.Picture.LoadFromFile('.\Images\weed.jpg');
  img32.Picture.LoadFromFile('.\Images\weed.jpg');
  img33.Picture.LoadFromFile('.\Images\weed.jpg');
  img34.Picture.LoadFromFile('.\Images\weed.jpg');
  img35.Picture.LoadFromFile('.\Images\weed.jpg');
  img36.Picture.LoadFromFile('.\Images\weed.jpg');
  img37.Picture.LoadFromFile('.\Images\weed.jpg');
  img38.Picture.LoadFromFile('.\Images\weed.jpg');
  img39.Picture.LoadFromFile('.\Images\weed.jpg');
  img3a.Picture.LoadFromFile('.\Images\weed.jpg');
  img3b.Picture.LoadFromFile('.\Images\weed.jpg');
  img3c.Picture.LoadFromFile('.\Images\weed.jpg');
  img3d.Picture.LoadFromFile('.\Images\weed.jpg');
  img3e.Picture.LoadFromFile('.\Images\weed.jpg');
  img3f.Picture.LoadFromFile('.\Images\weed.jpg');
  img3g.Picture.LoadFromFile('.\Images\weed.jpg');
  img3h.Picture.LoadFromFile('.\Images\weed.jpg');
  img3i.Picture.LoadFromFile('.\Images\weed.jpg');
  img3j.Picture.LoadFromFile('.\Images\weed.jpg');
  img3k.Picture.LoadFromFile('.\Images\weed.jpg');
  img3l.Picture.LoadFromFile('.\Images\weed.jpg');
  img3m.Picture.LoadFromFile('.\Images\weed.jpg');
  img40.Picture.LoadFromFile('.\Images\weed.jpg');
  img41.Picture.LoadFromFile('.\Images\weed.jpg');
  img42.Picture.LoadFromFile('.\Images\weed.jpg');
  img43.Picture.LoadFromFile('.\Images\weed.jpg');
  img44.Picture.LoadFromFile('.\Images\weed.jpg');
  img45.Picture.LoadFromFile('.\Images\weed.jpg');
  img46.Picture.LoadFromFile('.\Images\weed.jpg');
  img47.Picture.LoadFromFile('.\Images\weed.jpg');
  img48.Picture.LoadFromFile('.\Images\weed.jpg');
  img49.Picture.LoadFromFile('.\Images\weed.jpg');
  img4a.Picture.LoadFromFile('.\Images\weed.jpg');
  img4b.Picture.LoadFromFile('.\Images\weed.jpg');
  img4c.Picture.LoadFromFile('.\Images\weed.jpg');
  img4d.Picture.LoadFromFile('.\Images\weed.jpg');
  img4e.Picture.LoadFromFile('.\Images\weed.jpg');
  img4f.Picture.LoadFromFile('.\Images\weed.jpg');
  img4g.Picture.LoadFromFile('.\Images\weed.jpg');
  img4h.Picture.LoadFromFile('.\Images\weed.jpg');
  img4i.Picture.LoadFromFile('.\Images\weed.jpg');
  img4j.Picture.LoadFromFile('.\Images\weed.jpg');
  img4k.Picture.LoadFromFile('.\Images\weed.jpg');
  img4l.Picture.LoadFromFile('.\Images\weed.jpg');
  img4m.Picture.LoadFromFile('.\Images\weed.jpg');
  img50.Picture.LoadFromFile('.\Images\weed.jpg');
  img51.Picture.LoadFromFile('.\Images\weed.jpg');
  img52.Picture.LoadFromFile('.\Images\weed.jpg');
  img53.Picture.LoadFromFile('.\Images\weed.jpg');
  img54.Picture.LoadFromFile('.\Images\weed.jpg');
  img55.Picture.LoadFromFile('.\Images\weed.jpg');
  img56.Picture.LoadFromFile('.\Images\weed.jpg');
  img57.Picture.LoadFromFile('.\Images\weed.jpg');
  img58.Picture.LoadFromFile('.\Images\weed.jpg');
  img59.Picture.LoadFromFile('.\Images\weed.jpg');
  img5a.Picture.LoadFromFile('.\Images\weed.jpg');
  img5b.Picture.LoadFromFile('.\Images\weed.jpg');
  img5c.Picture.LoadFromFile('.\Images\weed.jpg');
  img5d.Picture.LoadFromFile('.\Images\weed.jpg');
  img5e.Picture.LoadFromFile('.\Images\weed.jpg');
  img5f.Picture.LoadFromFile('.\Images\weed.jpg');
  img5g.Picture.LoadFromFile('.\Images\weed.jpg');
  img5h.Picture.LoadFromFile('.\Images\weed.jpg');
  img5i.Picture.LoadFromFile('.\Images\weed.jpg');
  img5j.Picture.LoadFromFile('.\Images\weed.jpg');
  img5k.Picture.LoadFromFile('.\Images\weed.jpg');
  img5l.Picture.LoadFromFile('.\Images\weed.jpg');
  img5m.Picture.LoadFromFile('.\Images\weed.jpg');
  img60.Picture.LoadFromFile('.\Images\weed.jpg');
  img61.Picture.LoadFromFile('.\Images\weed.jpg');
  img62.Picture.LoadFromFile('.\Images\weed.jpg');
  img63.Picture.LoadFromFile('.\Images\weed.jpg');
  img64.Picture.LoadFromFile('.\Images\weed.jpg');
  img65.Picture.LoadFromFile('.\Images\weed.jpg');
  img66.Picture.LoadFromFile('.\Images\weed.jpg');
  img67.Picture.LoadFromFile('.\Images\weed.jpg');
  img68.Picture.LoadFromFile('.\Images\weed.jpg');
  img69.Picture.LoadFromFile('.\Images\weed.jpg');
  img6a.Picture.LoadFromFile('.\Images\weed.jpg');
  img6b.Picture.LoadFromFile('.\Images\weed.jpg');
  img6c.Picture.LoadFromFile('.\Images\weed.jpg');
  img6d.Picture.LoadFromFile('.\Images\weed.jpg');
  img6e.Picture.LoadFromFile('.\Images\weed.jpg');
  img6f.Picture.LoadFromFile('.\Images\weed.jpg');
  img6g.Picture.LoadFromFile('.\Images\weed.jpg');
  img6h.Picture.LoadFromFile('.\Images\weed.jpg');
  img6i.Picture.LoadFromFile('.\Images\weed.jpg');
  img6j.Picture.LoadFromFile('.\Images\weed.jpg');
  img6k.Picture.LoadFromFile('.\Images\weed.jpg');
  img6l.Picture.LoadFromFile('.\Images\weed.jpg');
  img6m.Picture.LoadFromFile('.\Images\weed.jpg');
  img70.Picture.LoadFromFile('.\Images\weed.jpg');
  img71.Picture.LoadFromFile('.\Images\weed.jpg');
  img72.Picture.LoadFromFile('.\Images\weed.jpg');
  img73.Picture.LoadFromFile('.\Images\weed.jpg');
  img74.Picture.LoadFromFile('.\Images\weed.jpg');
  img75.Picture.LoadFromFile('.\Images\weed.jpg');
  img76.Picture.LoadFromFile('.\Images\weed.jpg');
  img77.Picture.LoadFromFile('.\Images\weed.jpg');
  img78.Picture.LoadFromFile('.\Images\weed.jpg');
  img79.Picture.LoadFromFile('.\Images\weed.jpg');
  img7a.Picture.LoadFromFile('.\Images\weed.jpg');
  img7b.Picture.LoadFromFile('.\Images\market_32.jpg'); ish[7,11]:=8; // �����
  img7c.Picture.LoadFromFile('.\Images\weed.jpg');
  img7d.Picture.LoadFromFile('.\Images\weed.jpg');
  img7e.Picture.LoadFromFile('.\Images\weed.jpg');
  img7f.Picture.LoadFromFile('.\Images\weed.jpg');
  img7g.Picture.LoadFromFile('.\Images\weed.jpg');
  img7h.Picture.LoadFromFile('.\Images\weed.jpg');
  img7i.Picture.LoadFromFile('.\Images\weed.jpg');
  img7j.Picture.LoadFromFile('.\Images\weed.jpg');
  img7k.Picture.LoadFromFile('.\Images\weed.jpg');
  img7l.Picture.LoadFromFile('.\Images\weed.jpg');
  img7m.Picture.LoadFromFile('.\Images\weed.jpg');
  img80.Picture.LoadFromFile('.\Images\weed.jpg');
  img81.Picture.LoadFromFile('.\Images\weed.jpg');
  img82.Picture.LoadFromFile('.\Images\weed.jpg');
  img83.Picture.LoadFromFile('.\Images\weed.jpg');
  img84.Picture.LoadFromFile('.\Images\weed.jpg');
  img85.Picture.LoadFromFile('.\Images\weed.jpg');
  img86.Picture.LoadFromFile('.\Images\weed.jpg');
  img87.Picture.LoadFromFile('.\Images\weed.jpg');
  img88.Picture.LoadFromFile('.\Images\weed.jpg');
  img89.Picture.LoadFromFile('.\Images\weed.jpg');
  img8a.Picture.LoadFromFile('.\Images\weed.jpg');
  img8b.Picture.LoadFromFile('.\Images\weed.jpg');
  img8c.Picture.LoadFromFile('.\Images\weed.jpg');
  img8d.Picture.LoadFromFile('.\Images\weed.jpg');
  img8e.Picture.LoadFromFile('.\Images\weed.jpg');
  img8f.Picture.LoadFromFile('.\Images\weed.jpg');
  img8g.Picture.LoadFromFile('.\Images\weed.jpg');
  img8h.Picture.LoadFromFile('.\Images\weed.jpg');
  img8i.Picture.LoadFromFile('.\Images\weed.jpg');
  img8j.Picture.LoadFromFile('.\Images\weed.jpg');
  img8k.Picture.LoadFromFile('.\Images\weed.jpg');
  img8l.Picture.LoadFromFile('.\Images\weed.jpg');
  img8m.Picture.LoadFromFile('.\Images\weed.jpg');
  img90.Picture.LoadFromFile('.\Images\weed.jpg');
  img91.Picture.LoadFromFile('.\Images\weed.jpg');
  img92.Picture.LoadFromFile('.\Images\weed.jpg');
  img93.Picture.LoadFromFile('.\Images\weed.jpg');
  img94.Picture.LoadFromFile('.\Images\weed.jpg');
  img95.Picture.LoadFromFile('.\Images\weed.jpg');
  img96.Picture.LoadFromFile('.\Images\weed.jpg');
  img97.Picture.LoadFromFile('.\Images\weed.jpg');
  img98.Picture.LoadFromFile('.\Images\weed.jpg');
  img99.Picture.LoadFromFile('.\Images\weed.jpg');
  img9a.Picture.LoadFromFile('.\Images\weed.jpg');
  img9b.Picture.LoadFromFile('.\Images\weed.jpg');
  img9c.Picture.LoadFromFile('.\Images\weed.jpg');
  img9d.Picture.LoadFromFile('.\Images\weed.jpg');
  img9e.Picture.LoadFromFile('.\Images\weed.jpg');
  img9f.Picture.LoadFromFile('.\Images\weed.jpg');
  img9g.Picture.LoadFromFile('.\Images\weed.jpg');
  img9h.Picture.LoadFromFile('.\Images\weed.jpg');
  img9i.Picture.LoadFromFile('.\Images\weed.jpg');
  img9j.Picture.LoadFromFile('.\Images\weed.jpg');
  img9k.Picture.LoadFromFile('.\Images\weed.jpg');
  img9l.Picture.LoadFromFile('.\Images\weed.jpg');
  img9m.Picture.LoadFromFile('.\Images\weed.jpg');
  imga0.Picture.LoadFromFile('.\Images\weed.jpg');
  imga1.Picture.LoadFromFile('.\Images\weed.jpg');
  imga2.Picture.LoadFromFile('.\Images\weed.jpg');
  imga3.Picture.LoadFromFile('.\Images\weed.jpg');
  imga4.Picture.LoadFromFile('.\Images\weed.jpg');
  imga5.Picture.LoadFromFile('.\Images\weed.jpg');
  imga6.Picture.LoadFromFile('.\Images\weed.jpg');
  imga7.Picture.LoadFromFile('.\Images\weed.jpg');
  imga8.Picture.LoadFromFile('.\Images\weed.jpg');
  imga9.Picture.LoadFromFile('.\Images\weed.jpg');
  imgaa.Picture.LoadFromFile('.\Images\weed.jpg');
  imgab.Picture.LoadFromFile('.\Images\weed.jpg');
  imgac.Picture.LoadFromFile('.\Images\weed.jpg');
  imgad.Picture.LoadFromFile('.\Images\weed.jpg');
  imgae.Picture.LoadFromFile('.\Images\weed.jpg');
  imgaf.Picture.LoadFromFile('.\Images\weed.jpg');
  imgag.Picture.LoadFromFile('.\Images\weed.jpg');
  imgah.Picture.LoadFromFile('.\Images\weed.jpg');
  imgai.Picture.LoadFromFile('.\Images\weed.jpg');
  imgaj.Picture.LoadFromFile('.\Images\weed.jpg');
  imgak.Picture.LoadFromFile('.\Images\weed.jpg');
  imgal.Picture.LoadFromFile('.\Images\weed.jpg');
  imgam.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb0.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb1.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb2.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb3.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb4.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb5.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb6.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb7.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb8.Picture.LoadFromFile('.\Images\weed.jpg');
  imgb9.Picture.LoadFromFile('.\Images\weed.jpg');
  imgba.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbb.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbc.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbd.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbe.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbf.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbg.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbh.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbi.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbj.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbk.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbl.Picture.LoadFromFile('.\Images\weed.jpg');
  imgbm.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc0.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc1.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc2.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc3.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc4.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc5.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc6.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc7.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc8.Picture.LoadFromFile('.\Images\weed.jpg');
  imgc9.Picture.LoadFromFile('.\Images\weed.jpg');
  imgca.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcb.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcc.Picture.LoadFromFile('.\Images\taverna_32.jpg'); ish[12,12]:=25; // �������
  imgcd.Picture.LoadFromFile('.\Images\weed.jpg');
  imgce.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcf.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcg.Picture.LoadFromFile('.\Images\weed.jpg');
  imgch.Picture.LoadFromFile('.\Images\weed.jpg');
  imgci.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcj.Picture.LoadFromFile('.\Images\weed.jpg');
  imgck.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcl.Picture.LoadFromFile('.\Images\weed.jpg');
  imgcm.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd0.Picture.LoadFromFile('.\Images\portal_32.jpg'); ish[13,0]:= 26; // ������
  imgd1.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd2.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd3.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd4.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd5.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd6.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd7.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd8.Picture.LoadFromFile('.\Images\weed.jpg');
  imgd9.Picture.LoadFromFile('.\Images\weed.jpg');
  imgda.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdb.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdc.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdd.Picture.LoadFromFile('.\Images\weed.jpg');
  imgde.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdf.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdg.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdh.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdi.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdj.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdk.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdl.Picture.LoadFromFile('.\Images\weed.jpg');
  imgdm.Picture.LoadFromFile('.\Images\weed.jpg');



  // ������� ������� ����� ���� �� ����� � �� ������
// 0 - �����, 1 - ����, 2 - ����, 3 - ����������(0 ��)
// 8 - �����, 9 - ���������� �����, 10 - ������
// 11 - ���������, 12 - ����, 13 - ���������, 23 - ������, 24 - ����� ������
// 25 - �������, 26 - ������

// �����
// 50 - �����, 51 - �����, 52 - ������� ������, 53 - �������, 54 - ��������, 55 - ������
// 56 - �������, 57 - ��������, 58 - ������, 59 - ������
// 60 - ����, 61 - ���� �����, 62 - ��������, 63 - ����������, 64 - �������, 65 - �������
// 66 - ��������, 67 - ������, 68 - ��������, 69 - �����, 70 - ����, 71 - �������
// 72 - ��� ����, 73 - ������

// �����
// 100 - ���� 1 ��, 101 - ���� 2 ��, 102 - ���� 3 ��, 103 - ����� 1 ��, 104 - ����� 2 ��
// 105 - ����� 3 ��, 106 - ���� 1 ��, 107 - ���� 2 ��, 108 - ���� 3 ��, 109 - ���� 4 ��
// 110 - ������ 0 ��, 111 - ������ 1 ��, 112 - ������ 2 ��, 113 - ������ 3 ��
// 114 - ��������� 1 ��, 115 - ��������� 2 ��, 116 - ��������� 3 ��
// 117 - ������� �� �������� 1 ��, 118 - �������, 119 - ������ 1 ��, 120 - ������ 2 ��
// 121 - ������ 3 ��, 122 - ������ 4 ��, 123 - ������ 1 ��, 124 - ������ 2 ��, 125 - ������ 3 ��
// 126 - ������� 1 ��, 127 - ������� 2 ��, 128 - ������� 3 ��, 129 - ������� 4 ��
// 130 - ���������, 131 - ����������� 1 ��, 132 - ����������� 2 ��, 133 - ��� 1 ��, 134 - ��� 2 ��
// 135 - ����������, 136 - ��� 1 ��, 137 - ��� 2 ��, 138 - ��� 3 ��, 139 - ��� 4 ��, 140 - ��� 5 ��
// 141 - ��� 6 ��, 142 - ��� 7 ��, 143 - ���-�����, 144 - ���������, 145 - ���������, 146 - ���������
// 147 - ������� �������� �����, 148 - ������ 1 ��, 149 - ������ 2 ��, 150 - ������ 3 ��
// 151 - ������ 4 ��, 152 - ������ 5 ��, 153 - ������ 6 ��, 154 - ������ 7 ��, 155 - ������ 8 ��
// 156 - ��������, 157 - ��������, 158 - ������ 1 ��, 159 - ������ 2 ��, 160 - ������ 3 ��
// 161 - ������ 4 ��, 162 - ������ 5 ��, 163 - ������ 6 ��, 164 - ������, 165 - ������
// 166 - �������-���� 1 ��, 167 - �������-���� 2 ��, 168 - �������-���� 3 ��
// 169 - �������-���� 4 ��, 170 - �������-���� 5 ��, 171 - �������-���� 6 ��
// 172 - �������-���� 7 ��


   sas := Random(6);      // ����� ��������������� ������� ������������ �����
   case sas of
   1:
     begin
       img00.Picture.LoadFromFile('.\Images\market_32.jpg');
       ish[0,0]:=8;
     end;

   2:
     begin
       img00.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[0,0]:=1;
     end;

   4:
     begin
       img00.Picture.LoadFromFile('.\Images\water.jpg');
       ish[0,0]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img05.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[0,5]:=1;
     end;

   4:
     begin
       img00.Picture.LoadFromFile('.\Images\water.jpg');
       ish[0,5]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img0f.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[0,15]:=1;
     end;

   4:
     begin
       img0f.Picture.LoadFromFile('.\Images\water.jpg');
       ish[0,15]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img15.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[1,5]:=1;
     end;

   4:
     begin
       img15.Picture.LoadFromFile('.\Images\water.jpg');
       ish[1,5]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img1a.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[1,10]:=1;
     end;

   4:
     begin
       img1a.Picture.LoadFromFile('.\Images\water.jpg');
       ish[1,10]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img1b.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[1,11]:=1;
     end;

   4:
     begin
       img1b.Picture.LoadFromFile('.\Images\water.jpg');
       ish[1,11]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img1k.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[1,19]:=1;
     end;

   4:
     begin
       img1k.Picture.LoadFromFile('.\Images\water.jpg');
       ish[1,19]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img20.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[2,0]:=1;
     end;

   4:
     begin
       img20.Picture.LoadFromFile('.\Images\water.jpg');
       ish[2,0]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img21.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[2,1]:=1;
     end;

   4:
     begin
       img21.Picture.LoadFromFile('.\Images\water.jpg');
       ish[2,1]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img22.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[2,2]:=1;
     end;

   4:
     begin
       img22.Picture.LoadFromFile('.\Images\water.jpg');
       ish[2,2]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img27.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[2,7]:=1;
     end;

   4:
     begin
       img27.Picture.LoadFromFile('.\Images\water.jpg');
       ish[2,7]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img2a.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[2,10]:=1;
     end;

   4:
     begin
       img2a.Picture.LoadFromFile('.\Images\water.jpg');
       ish[2,10]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img2b.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[2,11]:=1;
     end;

   4:
     begin
       img2b.Picture.LoadFromFile('.\Images\water.jpg');
       ish[2,11]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img3b.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[3,11]:=1;
     end;

   2:
     begin
       img3b.Picture.LoadFromFile('.\Images\water.jpg');
       ish[3,11]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img3e.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[3,14]:=1;
     end;

   4:
     begin
       img3e.Picture.LoadFromFile('.\Images\water.jpg');
       ish[3,14]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img4e.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[4,14]:=1;
     end;

   4:
     begin
       img4e.Picture.LoadFromFile('.\Images\water.jpg');
       ish[4,14]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img5e.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[5,14]:=1;
     end;

   2:
     begin
       img5e.Picture.LoadFromFile('.\Images\water.jpg');
       ish[5,14]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img5g.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[5,16]:=1;
     end;

   4:
     begin
       img5g.Picture.LoadFromFile('.\Images\water.jpg');
       ish[5,16]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img5h.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[5,17]:=1;
     end;

   4:
     begin
       img5h.Picture.LoadFromFile('.\Images\water.jpg');
       ish[5,17]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img5i.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[5,18]:=1;
     end;

   4:
     begin
       img5i.Picture.LoadFromFile('.\Images\water.jpg');
       ish[5,18]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img5k.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[5,20]:=1;
     end;

   4:
     begin
       img5k.Picture.LoadFromFile('.\Images\water.jpg');
       ish[5,20]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img6a.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[6,10]:=1;
     end;

   2:
     begin
       img6a.Picture.LoadFromFile('.\Images\water.jpg');
       ish[6,10]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img6g.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[6,16]:=1;
     end;

   4:
     begin
       img6g.Picture.LoadFromFile('.\Images\water.jpg');
       ish[6,16]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img6h.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[6,17]:=1;
     end;

   4:
     begin
       img6h.Picture.LoadFromFile('.\Images\water.jpg');
       ish[6,17]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img6i.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[6,18]:=1;
     end;

   4:
     begin
       img6i.Picture.LoadFromFile('.\Images\water.jpg');
       ish[6,18]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img6k.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[6,20]:=1;
     end;

   4:
     begin
       img6k.Picture.LoadFromFile('.\Images\water.jpg');
       ish[6,20]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img70.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,0]:=1;
     end;

   4:
     begin
       img70.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,0]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img72.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,2]:=1;
     end;

   4:
     begin
       img72.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,2]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img73.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,3]:=1;
     end;

   4:
     begin
       img73.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,3]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img74.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,4]:=1;
     end;

   2:
     begin
       img74.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,4]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img75.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,5]:=1;
     end;

   2:
     begin
       img75.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,5]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img77.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,7]:=1;
     end;

   5:
     begin
       img77.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,7]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img78.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,8]:=1;
     end;

   5:
     begin
       img78.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,8]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img79.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,9]:=1;
     end;

   5:
     begin
       img79.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,9]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img7g.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,16]:=1;
     end;

   5:
     begin
       img7g.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,16]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       img7h.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,17]:=1;
     end;

   5:
     begin
       img7h.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,17]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img7m.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[7,21]:=1;
     end;

   2:
     begin
       img7m.Picture.LoadFromFile('.\Images\water.jpg');
       ish[7,21]:=2;
     end;
   end;
   sas := Random(6);
   case sas of
   1:
     begin
       img8m.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[8,21]:=1;
     end;

   2:
     begin
       img8m.Picture.LoadFromFile('.\Images\water.jpg');
       ish[8,21]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img91.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[9,1]:=1;
     end;

   2:
     begin
       img91.Picture.LoadFromFile('.\Images\water.jpg');
       ish[9,1]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img99.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[9,9]:=1;
     end;

   2:
     begin
       img99.Picture.LoadFromFile('.\Images\water.jpg');
       ish[9,9]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       img9h.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[9,17]:=1;
     end;

   2:
     begin
       img9h.Picture.LoadFromFile('.\Images\water.jpg');
       ish[9,17]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       imga3.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[10,3]:=1;
     end;

   2:
     begin
       imga3.Picture.LoadFromFile('.\Images\water.jpg');
       ish[10,3]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       imga4.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[10,4]:=1;
     end;

   2:
     begin
       imga4.Picture.LoadFromFile('.\Images\water.jpg');
       ish[10,4]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imga5.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[10,5]:=1;
     end;

   5:
     begin
       imga5.Picture.LoadFromFile('.\Images\water.jpg');
       ish[10,5]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   1:
     begin
       imga8.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[10,8]:=1;
     end;

   2:
     begin
       imga8.Picture.LoadFromFile('.\Images\water.jpg');
       ish[10,8]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgab.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[10,11]:=1;
     end;

   4:
     begin
       imgab.Picture.LoadFromFile('.\Images\water.jpg');
       ish[10,11]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgbb.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[11,11]:=1;
     end;

   4:
     begin
       imgbb.Picture.LoadFromFile('.\Images\water.jpg');
       ish[11,11]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgc8.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[12,8]:=1;
     end;

   4:
     begin
       imgc8.Picture.LoadFromFile('.\Images\water.jpg');
       ish[12,8]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgc9.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[12,9]:=1;
     end;

   4:
     begin
       imgc9.Picture.LoadFromFile('.\Images\water.jpg');
       ish[12,9]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgcf.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[12,15]:=1;
     end;

   4:
     begin
       imgcf.Picture.LoadFromFile('.\Images\water.jpg');
       ish[12,15]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgcm.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[12,21]:=1;
     end;

   4:
     begin
       imgcm.Picture.LoadFromFile('.\Images\water.jpg');
       ish[12,21]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgd5.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[13,5]:=1;
     end;

   4:
     begin
       imgd5.Picture.LoadFromFile('.\Images\water.jpg');
       ish[13,5]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgd6.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[13,6]:=1;
     end;

   4:
     begin
       imgd6.Picture.LoadFromFile('.\Images\water.jpg');
       ish[13,6]:=2;
     end;
   end;

   sas := Random(6);
   case sas of
   2:
     begin
       imgda.Picture.LoadFromFile('.\Images\mount.jpg');
       ish[13,10]:=1;
     end;

   4:
     begin
       imgda.Picture.LoadFromFile('.\Images\water.jpg');
       ish[13,10]:=2;
     end;
   end;

end;





procedure TForm1.FormMouseMove(Sender: TObject; Shift: TShiftState; X,
  Y: Integer);
var
  xg : Integer;
  yg : Integer;
  nn : Integer;
  rangeArray : Array[0..28] of string;

begin
      xg := 16;
      yg := 64;
      nn:=0;
      rangeArray[0] := '0';
      rangeArray[1] := '1';
      rangeArray[2] := '2';
      rangeArray[3] := '3';
      rangeArray[4] := '4';
      rangeArray[5] := '5';
      rangeArray[6] := '6';
      rangeArray[7] := '7';
      rangeArray[8] := '8';
      rangeArray[9] := '9';
      rangeArray[10] := 'A';
      rangeArray[11] := 'B';
      rangeArray[12] := 'C';
      rangeArray[13] := 'D';
      rangeArray[14] := 'E';
      rangeArray[15] := 'F';
      rangeArray[16] := 'G';
      rangeArray[17] := 'H';
      rangeArray[18] := 'I';
      rangeArray[19] := 'J';
      rangeArray[20] := 'K';
      rangeArray[21] := 'L';
      rangeArray[22] := 'M';
      rangeArray[23] := 'N';
      rangeArray[24] := 'O';

      //kletkiIpersi;


	  
	    while xg <= 752 do
      begin
        Form1.Canvas.MoveTo(xg,64);
        Form1.Canvas.LineTo(xg,512);
        xg := xg + 32
      end;

      yg := 64;

      while yg <= 512 do
      begin
        Form1.Canvas.MoveTo(16,yg);
        Form1.Canvas.LineTo(752,yg);
        yg := yg + 32
      end;

      xg := 29;
      yg := 50;

      while nn <= 22 do
      begin
         Form1.Canvas.MoveTo(xg,yg);
         Form1.Canvas.TextOut(xg, yg, rangeArray[nn]);
         xg := xg + 32;
         nn:=nn+1;
      end;

      nn:=0;
      xg := 6;
      yg := 75;

      while nn <= 13 do
      begin
         Form1.Canvas.MoveTo(xg,yg);
         Form1.Canvas.TextOut(xg, yg, rangeArray[nn]);
         yg := yg + 32;
         nn:=nn+1;

      end;




end;



procedure TForm1.img00Click(Sender: TObject);
begin
if ish[0,0]= 8 then
begin
  mmo1.Text:='������: �����';
end;
end;

procedure TForm1.img0mClick(Sender: TObject);
begin
mmo1.Text:='������: ��������� ������' +#13#10 +#13#10;
mmo1.Text:=mmo1.Text + '�� ��� ������ ������� ���� � ����� � ������� �����������. ������ ������ ��������� ������, ��������� ��� ��������� �� ������ ����.'+#13#10 +#13#10;
mmo1.Text:=mmo1.Text + '���� ���� ������ ����� ������� ��� ����, �� ����, ��������� �� ��������� ����� ������������ � ��� �� �������� �� ������� �����, �� ��� ��� ���� �� �� ��� �� �������';

end;

procedure TForm1.btn1Click(Sender: TObject);
begin
Form2.Show;
end;

procedure TForm1.img9bClick(Sender: TObject);
begin
if (ish[9,12] <> 0) and (ish[9,12] <> 2) and (ish[9,12] <> 0) then
begin
mmo1.Text:= 'sas';


end;

end;

procedure TForm1.btn4Click(Sender: TObject);  // ����� ����
var
  newBotGeneration : integer;
  newBotPos : Array[0..19,0..13,0..22] of Integer; // ������� ���� (������ ��� ���� ��� ������)
  newBotLvl : array[0..19] of Integer; // Level ����
  newBotZdor : array[0..19] of Integer;
  newBotMana : array[0..19] of Integer;
  newBotExp : array[0..19] of Integer;      // ������� ����
  newBotExpLvlUp : array[0..19] of Integer; // ����������� ���� �� ���������� ������
  newBotPower : array[0..19] of Integer;
  newBotLovk : array[0..19] of Integer;
  newBotYdacha : array[0..19] of Integer;
  newBotZaklin : Array[0..19,0..15] of Integer; // ������� � ������� ����������
  newBotInvent : array[0..19,0..15] of Integer; // ������� � ��� �����
  newBotProdaet : array[0..19] of Integer; // ���� = 1 �� � ���� ����� �������� ���������
  newBotVrag : array[0..19] of Integer; // ���� = 1 �� �� ��������� � ����
  botRace : array[0..19] of Integer; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)
  xBot : Integer;
  yBot : Integer;
  botaNet : integer;
  nomerBota : Integer;
begin
  newBotGeneration := Random(5);
  if newBotGeneration <> 1 then
  xBot := 0;
  yBot := 0;
  nomerBota := 0;
  botaNet := 0;
  begin
   newBotGeneration := Random(72) + 100;

   while nomerBota <= 19 do
   begin
     while (xBot <= 22) and (yBot <= 13) do
     begin
       if newBotPos[nomerBota,yBot, xBot] = 0 then
       begin
         botaNet := botaNet + 1;
       end;

       if xBot = 22 then
       begin
         xBot := 0;
         yBot := yBot + 1;
       end;

       if (xBot = 22) and (yBot = 13) then
       begin
         xBot := 0;
         yBot := 0;
         nomerBota := nomerBota + 1;
       end;

       xBot := xBot + 1;

     end;
     if (newBotPos[nomerBota,yBot, xBot] = 0) and (botaNet = 308) then // ������ ��� �� � ������ ����
       begin
         newBotPos[nomerBota,yBot, xBot] = newBotGeneration;
         if newBotPos[nomerBota,yBot, xBot] = 71 then   // ��� ���� 1 ��
         begin
           botLvl[nomerBota] := 1; // Level ����
           botZdor[nomerBota] := 50;
           botMana[nomerBota] := 30;
           botExp[nomerBota] := 0;     // ������� ����
           botExpLvlUp[nomerBota] := 30; // ����������� ���� �� ���������� ������
           botPower[nomerBota] := 5;
           botLovk[nomerBota] := 3;
           botYdacha[nomerBota] := 1;
           botZaklin:[nomerBota,0]:=6;// �������� ����� (6)
           //newBotInvent : array[0..19,0..15] of Integer; // ������� � ��� �����
           botProdaet : array[0..19] of Integer; // ���� = 1 �� � ���� ����� �������� ���������
           if (Player1Race = 2) or (Player1Race = 3) then botVrag[nomerBota] := 1;
           if (Player1Race = 0) or (Player1Race = 1) then botVrag[nomerBota] := 0;
           // ���� = 1 �� �� ��������� � ����
           botRace[nomerBota]:=1; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)
         end;
         
         if newBotPos[nomerBota,yBot, xBot] = 71 then   // ��� ���� 2 ��
         begin
           botLvl[nomerBota] := 1; // Level ����
           botZdor[nomerBota] := 50;
           botMana[nomerBota] := 30;
           botExp[nomerBota] := 0;     // ������� ����
           botExpLvlUp[nomerBota] := 30; // ����������� ���� �� ���������� ������
           botPower[nomerBota] := 5;
           botLovk[nomerBota] := 3;
           botYdacha[nomerBota] := 1;
           botZaklin:[nomerBota,0]:=6;// �������� ����� (6)
           //newBotInvent : array[0..19,0..15] of Integer; // ������� � ��� �����
           botProdaet : array[0..19] of Integer; // ���� = 1 �� � ���� ����� �������� ���������
           if (Player1Race = 2) or (Player1Race = 3) then botVrag[nomerBota] := 1;
           if (Player1Race = 0) or (Player1Race = 1) then botVrag[nomerBota] := 0;
           // ���� = 1 �� �� ��������� � ����
           botRace[nomerBota]:=1; // ���� (0 - ����, 1 - �����, 2 - ����, 3 - ������, 4 - �������, 5 - ������)
         end;

       end;
   end;
  end;
end;

end.

// �����
// 100 - ���� 1 ��, 101 - ���� 2 ��, 102 - ���� 3 ��, 103 - ����� 1 ��, 104 - ����� 2 ��
// 105 - ����� 3 ��, 106 - ���� 1 ��, 107 - ���� 2 ��, 108 - ���� 3 ��, 109 - ���� 4 ��
// 110 - ������ 0 ��, 111 - ������ 1 ��, 112 - ������ 2 ��, 113 - ������ 3 ��
// 114 - ��������� 1 ��, 115 - ��������� 2 ��, 116 - ��������� 3 ��
// 117 - ������� �� �������� 1 ��, 118 - �������, 119 - ������ 1 ��, 120 - ������ 2 ��
// 121 - ������ 3 ��, 122 - ������ 4 ��, 123 - ������ 1 ��, 124 - ������ 2 ��, 125 - ������ 3 ��
// 126 - ������� 1 ��, 127 - ������� 2 ��, 128 - ������� 3 ��, 129 - ������� 4 ��
// 130 - ���������, 131 - ����������� 1 ��, 132 - ����������� 2 ��, 133 - ��� 1 ��, 134 - ��� 2 ��
// 135 - ����������, 136 - ��� 1 ��, 137 - ��� 2 ��, 138 - ��� 3 ��, 139 - ��� 4 ��, 140 - ��� 5 ��
// 141 - ��� 6 ��, 142 - ��� 7 ��, 143 - ���-�����, 144 - ���������, 145 - ���������, 146 - ���������
// 147 - ������� �������� �����, 148 - ������ 1 ��, 149 - ������ 2 ��, 150 - ������ 3 ��
// 151 - ������ 4 ��, 152 - ������ 5 ��, 153 - ������ 6 ��, 154 - ������ 7 ��, 155 - ������ 8 ��
// 156 - ��������, 157 - ��������, 158 - ������ 1 ��, 159 - ������ 2 ��, 160 - ������ 3 ��
// 161 - ������ 4 ��, 162 - ������ 5 ��, 163 - ������ 6 ��, 164 - ������, 165 - ������
// 166 - �������-���� 1 ��, 167 - �������-���� 2 ��, 168 - �������-���� 3 ��
// 169 - �������-���� 4 ��, 170 - �������-���� 5 ��, 171 - �������-���� 6 ��
// 172 - �������-���� 7 ��