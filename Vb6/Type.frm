VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Begin VB.Form Form1 
   BackColor       =   &H00EC6962&
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Input Harga Motor"
   ClientHeight    =   8520
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   11775
   Icon            =   "Type.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   8520
   ScaleWidth      =   11775
   ShowInTaskbar   =   0   'False
   Begin VB.CommandButton Command3 
      BackColor       =   &H00979B04&
      Caption         =   "hapus"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   2400
      Picture         =   "Type.frx":08CA
      Style           =   1  'Graphical
      TabIndex        =   4
      Top             =   7200
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Caption         =   "simpan"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   1320
      Picture         =   "Type.frx":104D
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   7200
      Width           =   1095
   End
   Begin VB.TextBox Text5 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   3000
      MaxLength       =   12
      TabIndex        =   14
      Text            =   "Text2"
      Top             =   1200
      Width           =   3135
   End
   Begin VB.TextBox Text4 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   3000
      MaxLength       =   7
      TabIndex        =   12
      Text            =   "Text2"
      Top             =   720
      Width           =   2295
   End
   Begin VB.TextBox Text1 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   7200
      MaxLength       =   10
      TabIndex        =   1
      Text            =   "Text1"
      Top             =   360
      Visible         =   0   'False
      Width           =   2655
   End
   Begin VB.TextBox Text2 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   7200
      MaxLength       =   25
      TabIndex        =   7
      Text            =   "Text2"
      Top             =   840
      Visible         =   0   'False
      Width           =   4455
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00979B04&
      Caption         =   "baru"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   240
      Picture         =   "Type.frx":18DB
      Style           =   1  'Graphical
      TabIndex        =   6
      Top             =   7200
      Width           =   1095
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "keluar"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   10320
      Picture         =   "Type.frx":1F83
      Style           =   1  'Graphical
      TabIndex        =   3
      Top             =   7200
      Width           =   1095
   End
   Begin VB.TextBox Text3 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   3000
      MaxLength       =   7
      TabIndex        =   0
      Text            =   "Text2"
      Top             =   240
      Width           =   2295
   End
   Begin MSAdodcLib.Adodc Adodc1 
      Height          =   735
      Left            =   4560
      Top             =   7200
      Visible         =   0   'False
      Width           =   1455
      _ExtentX        =   2566
      _ExtentY        =   1296
      ConnectMode     =   0
      CursorLocation  =   3
      IsolationLevel  =   -1
      ConnectionTimeout=   15
      CommandTimeout  =   30
      CursorType      =   3
      LockType        =   3
      CommandType     =   1
      CursorOptions   =   0
      CacheSize       =   50
      MaxRecords      =   0
      BOFAction       =   0
      EOFAction       =   0
      ConnectStringType=   3
      Appearance      =   1
      BackColor       =   -2147483643
      ForeColor       =   -2147483640
      Orientation     =   0
      Enabled         =   -1
      Connect         =   "DSN=Softtech"
      OLEDBString     =   ""
      OLEDBFile       =   ""
      DataSourceName  =   "Softtech"
      OtherAttributes =   ""
      UserName        =   ""
      Password        =   ""
      RecordSource    =   "select * from TType"
      Caption         =   "Adodc1"
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      _Version        =   393216
   End
   Begin MSDataGridLib.DataGrid DataGrid1 
      Bindings        =   "Type.frx":272C
      Height          =   5325
      Left            =   240
      TabIndex        =   2
      Top             =   1680
      Width           =   11235
      _ExtentX        =   19817
      _ExtentY        =   9393
      _Version        =   393216
      AllowUpdate     =   0   'False
      BackColor       =   16777215
      ForeColor       =   589833
      HeadLines       =   2
      RowHeight       =   15
      FormatLocked    =   -1  'True
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   3
      BeginProperty Column00 
         DataField       =   "Ket_Nomesin"
         Caption         =   "No.Mesin"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   "Ket_Norangka"
         Caption         =   "No. Rangka"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   ""
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column02 
         DataField       =   "OTR"
         Caption         =   "Harga OTR"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   0
         EndProperty
      EndProperty
      SplitCount      =   1
      BeginProperty Split0 
         MarqueeStyle    =   3
         Locked          =   -1  'True
         RecordSelectors =   0   'False
         BeginProperty Column00 
            ColumnAllowSizing=   -1  'True
            ColumnWidth     =   3075,024
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   3644,788
         EndProperty
         BeginProperty Column02 
            Alignment       =   1
            ColumnWidth     =   4034,835
         EndProperty
      EndProperty
   End
   Begin VB.Label Label5 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Harga On The Road"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00524A05&
      Height          =   195
      Left            =   600
      TabIndex        =   15
      Top             =   1260
      Width           =   1680
   End
   Begin VB.Label Label6 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Ketentuan No. Rangka"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00524A05&
      Height          =   195
      Left            =   600
      TabIndex        =   13
      Top             =   780
      Width           =   1920
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Kode Type"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00524A05&
      Height          =   195
      Left            =   2640
      TabIndex        =   11
      Top             =   1920
      Visible         =   0   'False
      Width           =   915
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Nama Type"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00524A05&
      Height          =   195
      Left            =   5040
      TabIndex        =   10
      Top             =   2160
      Visible         =   0   'False
      Width           =   975
   End
   Begin VB.Label Label3 
      Caption         =   "0"
      Height          =   495
      Left            =   3360
      TabIndex        =   9
      Top             =   4560
      Width           =   1215
   End
   Begin VB.Label Label4 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Ketentuan No. Mesin"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00524A05&
      Height          =   195
      Left            =   600
      TabIndex        =   8
      Top             =   300
      Width           =   1755
   End
   Begin VB.Image Image1 
      Height          =   10455
      Left            =   -600
      Picture         =   "Type.frx":2741
      Stretch         =   -1  'True
      Top             =   -1920
      Width           =   13815
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim con As ADODB.Connection
Dim rs As ADODB.Recordset

Private Sub Command1_Click()
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text4.Text = ""
    Text5.Text = ""
    Call layar
    Text3.SetFocus
End Sub

Private Sub Command2_Click()
    Dim msql As String
    If Text4.Text <> "" And Text5.Text <> "" And Text3.Text <> "" Then
        msql = "select * from TType where ket_nomesin ='" & Text3.Text & "'"
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
            msql = "delete from TType where ket_nomesin ='" & Text3.Text & "'"
            con.Execute msql, , adCmdText
        End If
        msql = "Insert Into TType " _
               & "([kd_type],[Nama_type],[Harga_dasar],[Stok_sisa],[Stok_awal],[Ket_nomesin],[Ket_Norangka],[OTR]) " _
                   & "VALUES ('" & RTrim(Text1.Text) & "', '" & RTrim(Text2.Text) & "','" & Val(Label3.Caption) & "','" & Val(Label3.Caption) & "','" & Val(Label3.Caption) & "','" & Text3.Text & "','" & Text4.Text & "','" & Val(Format(Text5.Text, "")) & "');"
            con.Execute msql, , adCmdText
        Command1.SetFocus
    End If
    Call layar
End Sub
Sub layar()
    Dim msql As String
    msql = "select * from TType"
    Adodc1.RecordSource = msql
    Adodc1.Refresh
End Sub

Private Sub Command3_Click()
    If Text3.Text <> "" And Text4.Text <> "" Then
        msql = "select * from TType where ket_nomesin='" & Text3.Text & "'"
        Set rs = con.Execute(msql)
    
        If Not rs.EOF Then
            pesan = MsgBox("APAKAH ANDA YAKIN INGIN MENGHAPUS DATA INI ?", vbYesNo, "JAYA MOTOR")
            If pesan = vbYes Then
                msql = "delete from TType where ket_nomesin ='" & Text3.Text & "'"
                con.Execute msql, , adCmdText
                MsgBox "DATA TELAH DIHAPUS", , "JAYA MOTOR"
            End If
        End If
    
        Call layar
    End If
End Sub

Private Sub Command4_Click()
    Unload Me
End Sub


Private Sub DataGrid1_dblClick()
    On Error Resume Next
    Text1.Text = RTrim(Adodc1.Recordset!Kd_type)
    Text2.Text = RTrim(Adodc1.Recordset!Nama_type)
    Text3.Text = RTrim(Adodc1.Recordset!Ket_nomesin)
    Text4.Text = RTrim(Adodc1.Recordset!ket_norangka)
    Text5.Text = Format(Adodc1.Recordset!OTR, "###,###")
End Sub

Private Sub Form_Load()
    Set con = New ADODB.Connection
    con.Open "Softtech"
    
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text4.Text = ""
    Text5.Text = ""
    
    Top = 0
    Left = 0
End Sub

Private Sub Form_Unload(Cancel As Integer)
    con.Close
    Set con = Nothing
End Sub

Private Sub Text1_Change()
    If Text1.Text <> "" Then
        Adodc1.RecordSource = "select * from TType where kd_type LIKE '" & Text1.Text & "%" & "' order by kd_type"
        Adodc1.Refresh
    End If
End Sub

Private Sub Text1_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text1.Text <> "" Then
            msql = "select * from TType where kd_type='" & Text1.Text & "'"
        
            Set rs = con.Execute(msql)
        
            With rs
                If Not .EOF Then
                    Text1.Text = RTrim(!Kd_type)
                    Text2.Text = RTrim(!Nama_type)
                    Text3.Text = RTrim(!Ket_nomesin)
                    Text4.Text = RTrim(!ket_norangka)
                    Text5.Text = Format(!OTR, "###,###")
                Else
                    Text2.Text = ""
                    Text2.SetFocus
                End If
                rs.Close
                Adodc1.Refresh
            End With
        End If
    End If
End Sub

Private Sub Text2_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text2.Text <> "" Then
            Text3.SetFocus
        End If
    End If
End Sub

Private Sub Text3_Change()
    If Text3.Text <> "" Then
        Adodc1.RecordSource = "select * from TType where ket_nomesin LIKE '" & Text3.Text & "%" & "' order by ket_nomesin"
        Adodc1.Refresh
    End If
End Sub

Private Sub Text3_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text3.Text <> "" Then
            msql = "select * from TType where ket_nomesin='" & Text3.Text & "'"
        
            Set rs = con.Execute(msql)
        
            With rs
                If Not .EOF Then
                    Text1.Text = RTrim(!Kd_type)
                    Text2.Text = RTrim(!Nama_type)
                    Text3.Text = RTrim(!Ket_nomesin)
                    Text4.Text = RTrim(!ket_norangka)
                    Text5.Text = Format(!OTR, "###,###")
                Else
                    Text4.Text = ""
                    Text4.SetFocus
                End If
                rs.Close
                Adodc1.Refresh
            End With
        End If
    End If
End Sub

Private Sub Text4_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text4.Text <> "" Then
            Text5.SetFocus
        End If
    End If
End Sub

Private Sub Text5_Change()
    If Text5.Text <> "" Then
        Text5.Text = Format(Text5.Text, "###,###")
        SendKeys "{End}"
    End If
End Sub

Private Sub Text5_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text5.Text <> "" Then
            Command2.SetFocus
        End If
    End If
End Sub

Private Sub Text5_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

