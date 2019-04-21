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


  // �����
// 50 - �����, 51 - �����, 52 - ������� ������, 53 - �������, 54 - ��������, 55 - ������
// 56 - �������, 57 - ��������, 58 - ������, 59 - ������
// 60 - ����, 61 - ���� �����, 62 - ��������, 63 - ����������, 64 - �������, 65 - �������
// 66 - ��������, 67 - ������, 68 - ��������, 69 - �����, 70 - ����, 71 - �������
// 72 - ��� ����, 73 - ������
begin
 hero := 50;
 ish[9,12] := hero;
 imgAvatar.Picture.LoadFromFile('.\Images\akami.jpg');
 mmo1.Text:='�����' +#13#10;
 mmo1.Text:=mmo1.Text + '����: 165'+#13#10;
 mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
 mmo1.Text:=mmo1.Text + '����: 100'+#13#10;
 mmo1.Text:=mmo1.Text + #13#10;
 mmo1.Text:=mmo1.Text + '����: 15'+#13#10;
 mmo1.Text:=mmo1.Text + '������: 5'+#13#10;
 mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
 mmo1.Text:=mmo1.Text + '����: 10'+#13#10;
 mmo1.Text:=mmo1.Text + #13#10;
 mmo1.Text:=mmo1.Text + '��������: ����� ����� ������. '+#13#10;
 mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
 mmo1.Text:=mmo1.Text + '���� ������'+#13#10;
 mmo1.Text:=mmo1.Text + '������'+#13#10;
end;

procedure TForm2.btn2Click(Sender: TObject);
begin
  hero := 51;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\artes.jpg');
mmo1.Text:='�����'+#13#10;
mmo1.Text:=mmo1.Text + '����: 205'+#13#10;
mmo1.Text:=mmo1.Text + '����: 100'+#13#10;
mmo1.Text:=mmo1.Text + '����: 75'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 21'+#13#10;
mmo1.Text:=mmo1.Text + '������: 8'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 6'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ��� ������ �����, ����������������� ����� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
end;

procedure TForm2.btn3Click(Sender: TObject);
begin
  hero := 52;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\deathOwner.jpg');
mmo1.Text:='������� ������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 175'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 135'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 17'+#13#10;
mmo1.Text:=mmo1.Text + '������: 2'+#13#10;
mmo1.Text:=mmo1.Text + '����: 3'+#13#10;
mmo1.Text:=mmo1.Text + '����: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������ ��������� ������ � � ����������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������'+#13#10;
mmo1.Text:=mmo1.Text + '������������ ��������'+#13#10;
end;

procedure TForm2.btn4Click(Sender: TObject);
begin
  hero := 53;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\deterok.jpg');
mmo1.Text:='�������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + '����: 120'+#13#10;
mmo1.Text:=mmo1.Text + '����: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 25'+#13#10;
mmo1.Text:=mmo1.Text + '������: 3'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 2'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: �������� ������ ������ ������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '����������'+#13#10;
end;

procedure TForm2.btn5Click(Sender: TObject);
begin
hero := 54;
ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\djepotai.jpg');
mmo1.Text:='��������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 170'+#13#10;
mmo1.Text:=mmo1.Text + '����: 100'+#13#10;
mmo1.Text:=mmo1.Text + '����: 75'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 15'+#13#10;
mmo1.Text:=mmo1.Text + '������: 8'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '������'+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
end;

procedure TForm2.btn6Click(Sender: TObject);
begin
  hero := 55;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\farion.jpg');
mmo1.Text:='������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 190'+#13#10;
mmo1.Text:=mmo1.Text + '����: 170'+#13#10;
mmo1.Text:=mmo1.Text + '����: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 13'+#13#10;
mmo1.Text:=mmo1.Text + '������: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ����� ����������� ����� �����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���������'+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '��������� ����'+#13#10;
end;

procedure TForm2.btn7Click(Sender: TObject);
begin
  hero := 56;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\garitos.jpg');
mmo1.Text:='�������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 220'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + '����: 110'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 19'+#13#10;
mmo1.Text:=mmo1.Text + '������: 7'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 6'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������ ������ ����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '��������� ����'+#13#10;
end;

procedure TForm2.btn8Click(Sender: TObject);
begin
  hero := 57;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\gendalf.jpg');
mmo1.Text:='��������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 160'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 13'+#13#10;
mmo1.Text:=mmo1.Text + '������: 3'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ��������� ��� ������� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '������� �������'+#13#10;
mmo1.Text:=mmo1.Text + '�����'+#13#10;
mmo1.Text:=mmo1.Text + '������'+#13#10;
mmo1.Text:=mmo1.Text + '�������'+#13#10;

end;

procedure TForm2.btn9Click(Sender: TObject);
begin
  hero := 58;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\illidan.jpg');
mmo1.Text:='�������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 90'+#13#10;
mmo1.Text:=mmo1.Text + '����: 80'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 18'+#13#10;
mmo1.Text:=mmo1.Text + '������: 7'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 9'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������ ������ ������ ����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '�������������'+#13#10;
mmo1.Text:=mmo1.Text + '���������'+#13#10;
end;

procedure TForm2.btn10Click(Sender: TObject);
begin
  hero := 59;
  ish[9,12] := hero;
imgAvatar.Picture.LoadFromFile('.\Images\jaina.jpg');
mmo1.Text:='������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 110'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 15'+#13#10;
mmo1.Text:=mmo1.Text + '������: 7'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������ ������� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '�������'+#13#10;
mmo1.Text:=mmo1.Text + '�������� ����'+#13#10;

end;

procedure TForm2.btn11Click(Sender: TObject);
begin
  hero := 60;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\kell.jpg');
mmo1.Text:='����'+#13#10;
mmo1.Text:=mmo1.Text + '����: 190'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + '����: 100'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 19'+#13#10;
mmo1.Text:=mmo1.Text + '������: 7'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������ ������ ����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '�������'+#13#10;
end;

procedure TForm2.btn12Click(Sender: TObject);
begin
  hero := 61;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\kelTuZed.jpg');
mmo1.Text:='���� �����'+#13#10;
mmo1.Text:=mmo1.Text + '����: 220'+#13#10;
mmo1.Text:=mmo1.Text + '����: 170'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 20'+#13#10;
mmo1.Text:=mmo1.Text + '������: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: �����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '����� �����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������'+#13#10;
end;

procedure TForm2.btn13Click(Sender: TObject);
begin
  hero := 62;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\magerion.jpg');
mmo1.Text:='��������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 220'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + '����: 125'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 19'+#13#10;
mmo1.Text:=mmo1.Text + '������: 8'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: �����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '������� ����'+#13#10;
mmo1.Text:=mmo1.Text + '���������'+#13#10;
mmo1.Text:=mmo1.Text + '���� ������'+#13#10;
end;

procedure TForm2.btn14Click(Sender: TObject);
begin
  hero := 63;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\mefistofor.jpg');
mmo1.Text:='����������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 155'+#13#10;
mmo1.Text:=mmo1.Text + '����: 180'+#13#10;
mmo1.Text:=mmo1.Text + '����: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 14'+#13#10;
mmo1.Text:=mmo1.Text + '������: 8'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������ ��������� �����������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '������������ ��������'+#13#10;
mmo1.Text:=mmo1.Text + '�������� ����'+#13#10;
mmo1.Text:=mmo1.Text + '�������� �����'+#13#10;
end;

procedure TForm2.btn15Click(Sender: TObject);
begin
  hero := 64;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\paladin.jpg');
mmo1.Text:='�������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 130'+#13#10;
mmo1.Text:=mmo1.Text + '����: 105'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 23'+#13#10;
mmo1.Text:=mmo1.Text + '������: 10'+#13#10;
mmo1.Text:=mmo1.Text + '����: 3'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������� ����� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '�������� ����'+#13#10;

end;

procedure TForm2.btn16Click(Sender: TObject);
begin
  hero := 65;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\pradmur.jpg');
mmo1.Text:='�������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 175'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 130'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 12'+#13#10;
mmo1.Text:=mmo1.Text + '������: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 6'+#13#10;
mmo1.Text:=mmo1.Text + '����: 7'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ���������� ������� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '�������� ����'+#13#10;
mmo1.Text:=mmo1.Text + '�������'+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '�������� �����'+#13#10;
end;

procedure TForm2.btn17Click(Sender: TObject);
begin
  hero := 66;
  ish[9,12] := hero;
//  imgAvatar.Picture.LoadFromFile('.\Images\sargaras.png');
mmo1.Text:='�������� - ��� ���� ���'+#13#10;
mmo1.Text:=mmo1.Text + '����: 180'+#13#10;
mmo1.Text:=mmo1.Text + '����: 180'+#13#10;
mmo1.Text:=mmo1.Text + '����: 95'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 18'+#13#10;
mmo1.Text:=mmo1.Text + '������: 7'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: �������� ��������� ������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '�����'+#13#10;
mmo1.Text:=mmo1.Text + '������ �����'+#13#10;
end;

procedure TForm2.btn18Click(Sender: TObject);
begin
  hero := 67;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\sauron.jpg');
mmo1.Text:='������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 205'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 145'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 15'+#13#10;
mmo1.Text:=mmo1.Text + '������: 9'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 6'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ��������� ���������, ���������� ������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���������� ������'+#13#10;
mmo1.Text:=mmo1.Text + '������ � ����������'+#13#10;
mmo1.Text:=mmo1.Text + '���������� ����'+#13#10;
mmo1.Text:=mmo1.Text + '������������ ��������'+#13#10;
end;

procedure TForm2.btn19Click(Sender: TObject);
begin
  hero := 68;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\silvana.jpg');
mmo1.Text:='��������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 175'+#13#10;
mmo1.Text:=mmo1.Text + '����: 120'+#13#10;
mmo1.Text:=mmo1.Text + '����: 105'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 19'+#13#10;
mmo1.Text:=mmo1.Text + '������: 6'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ���������� ������ ���'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������'+#13#10;
mmo1.Text:=mmo1.Text + '���������� ����'+#13#10;
mmo1.Text:=mmo1.Text + '�������'+#13#10;
end;

procedure TForm2.btn20Click(Sender: TObject);
begin
  hero := 69;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\trall.jpeg');
mmo1.Text:='�����'+#13#10;
mmo1.Text:=mmo1.Text + '����: 190'+#13#10;
mmo1.Text:=mmo1.Text + '����: 115'+#13#10;
mmo1.Text:=mmo1.Text + '����: 90'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 19'+#13#10;
mmo1.Text:=mmo1.Text + '������: 8'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ����� �����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;

end;

procedure TForm2.btn21Click(Sender: TObject);
begin
  hero := 70;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\uter.jpg');
mmo1.Text:='����'+#13#10;
mmo1.Text:=mmo1.Text + '����: 190'+#13#10;
mmo1.Text:=mmo1.Text + '����: 150'+#13#10;
mmo1.Text:=mmo1.Text + '����: 125'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 18'+#13#10;
mmo1.Text:=mmo1.Text + '������: 9'+#13#10;
mmo1.Text:=mmo1.Text + '����: 3'+#13#10;
mmo1.Text:=mmo1.Text + '����: 8'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������� ����� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
mmo1.Text:=mmo1.Text + '�������������'+#13#10;

end;

procedure TForm2.btn22Click(Sender: TObject);
begin
  hero := 71;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\varomir.jpg');
mmo1.Text:='�������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 175'+#13#10;
mmo1.Text:=mmo1.Text + '����: 130'+#13#10;
mmo1.Text:=mmo1.Text + '����: 100'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 16'+#13#10;
mmo1.Text:=mmo1.Text + '������: 7'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 11'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: �������� ��������� ����� ������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '���������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ����'+#13#10;
mmo1.Text:=mmo1.Text + '��'+#13#10;
end;

procedure TForm2.btn23Click(Sender: TObject);
begin
  hero := 72;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\vulDjin.jpg');
mmo1.Text:='��� ����'+#13#10;
mmo1.Text:=mmo1.Text + '����: 170'+#13#10;
mmo1.Text:=mmo1.Text + '����: 200'+#13#10;
mmo1.Text:=mmo1.Text + '����: 120'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 17'+#13#10;
mmo1.Text:=mmo1.Text + '������: 5'+#13#10;
mmo1.Text:=mmo1.Text + '����: 6'+#13#10;
mmo1.Text:=mmo1.Text + '����: 5'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ������� ����� �������'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '�������'+#13#10;
mmo1.Text:=mmo1.Text + '������ �����'+#13#10;
mmo1.Text:=mmo1.Text + '�������� �����'+#13#10;
mmo1.Text:=mmo1.Text + '���� �������'+#13#10;
end;

procedure TForm2.btn24Click(Sender: TObject);
begin
  hero := 73;
  ish[9,12] := hero;
  imgAvatar.Picture.LoadFromFile('.\Images\zadira.jpg');
mmo1.Text:='������'+#13#10;
mmo1.Text:=mmo1.Text + '����: 195'+#13#10;
mmo1.Text:=mmo1.Text + '����: 160'+#13#10;
mmo1.Text:=mmo1.Text + '����: 110'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '����: 19'+#13#10;
mmo1.Text:=mmo1.Text + '������: 9'+#13#10;
mmo1.Text:=mmo1.Text + '����: 4'+#13#10;
mmo1.Text:=mmo1.Text + '����: 10'+#13#10;
mmo1.Text:=mmo1.Text + #13#10;
mmo1.Text:=mmo1.Text + '��������: ����������������� ����� �����'+#13#10;
mmo1.Text:=mmo1.Text + '������� ������������: '+#13#10;
mmo1.Text:=mmo1.Text + '��'+#13#10;
mmo1.Text:=mmo1.Text + '�������� ����'+#13#10;
end;

procedure TForm2.btn25Click(Sender: TObject);
begin
Form2.Close;
end;

end.
