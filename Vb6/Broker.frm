VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Begin VB.Form Form4 
   BackColor       =   &H00EC6962&
   BorderStyle     =   1  'Fixed Single
   Caption         =   "Master Link"
   ClientHeight    =   8805
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   11505
   Icon            =   "Broker.frx":0000
   LinkTopic       =   "Form4"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   8805
   ScaleWidth      =   11505
   Begin VB.TextBox Text4 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   375
      Left            =   2400
      MaxLength       =   25
      TabIndex        =   11
      Text            =   "Text2"
      Top             =   2280
      Width           =   2535
   End
   Begin VB.TextBox Text3 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   735
      Left            =   2400
      MaxLength       =   100
      MultiLine       =   -1  'True
      TabIndex        =   9
      Text            =   "Broker.frx":08CA
      Top             =   1320
      Width           =   7575
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "KELUAR"
      Height          =   1095
      Left            =   9960
      Picture         =   "Broker.frx":08D0
      Style           =   1  'Graphical
      TabIndex        =   8
      Top             =   7440
      Width           =   1095
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00979B04&
      Caption         =   "HAPUS"
      Height          =   1095
      Left            =   3120
      Picture         =   "Broker.frx":1079
      Style           =   1  'Graphical
      TabIndex        =   7
      Top             =   7440
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Caption         =   "SIMPAN"
      Height          =   1095
      Left            =   1680
      Picture         =   "Broker.frx":17FC
      Style           =   1  'Graphical
      TabIndex        =   6
      Top             =   7440
      Width           =   1095
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00979B04&
      Caption         =   "BARU"
      Height          =   1095
      Left            =   360
      Picture         =   "Broker.frx":208A
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   7440
      Width           =   1095
   End
   Begin MSAdodcLib.Adodc Adodc1 
      Height          =   735
      Left            =   2520
      Top             =   4080
      Visible         =   0   'False
      Width           =   1575
      _ExtentX        =   2778
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
      RecordSource    =   "select * from TBroker"
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
      Bindings        =   "Broker.frx":2732
      Height          =   4335
      Left            =   240
      TabIndex        =   4
      Top             =   2880
      Width           =   11055
      _ExtentX        =   19500
      _ExtentY        =   7646
      _Version        =   393216
      AllowUpdate     =   0   'False
      BackColor       =   12648447
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
      ColumnCount     =   4
      BeginProperty Column00 
         DataField       =   "kd_broker"
         Caption         =   "Kode Link"
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
      BeginProperty Column01 
         DataField       =   "Nama_broker"
         Caption         =   "Link"
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
         DataField       =   "Alamat"
         Caption         =   "Alamat"
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
      BeginProperty Column03 
         DataField       =   "Telpon"
         Caption         =   "Telpon"
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
      SplitCount      =   1
      BeginProperty Split0 
         MarqueeStyle    =   3
         RecordSelectors =   0   'False
         BeginProperty Column00 
            ColumnWidth     =   1604,976
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   2459,906
         EndProperty
         BeginProperty Column02 
            ColumnWidth     =   5309,858
         EndProperty
         BeginProperty Column03 
         EndProperty
      EndProperty
   End
   Begin VB.TextBox Text2 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   375
      Left            =   2400
      MaxLength       =   25
      TabIndex        =   2
      Text            =   "Text2"
      Top             =   840
      Width           =   4095
   End
   Begin VB.TextBox Text1 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   375
      Left            =   2400
      MaxLength       =   10
      TabIndex        =   1
      Text            =   "Text1"
      Top             =   360
      Width           =   3015
   End
   Begin VB.Label Label4 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Telpon"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   195
      Left            =   480
      TabIndex        =   12
      Top             =   2370
      Width           =   570
   End
   Begin VB.Label Label3 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Alamat"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   195
      Left            =   480
      TabIndex        =   10
      Top             =   1410
      Width           =   615
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Nama Link"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   195
      Left            =   480
      TabIndex        =   3
      Top             =   930
      Width           =   870
   End
   Begin VB.Label Label1 
      BackStyle       =   0  'Transparent
      Caption         =   "Kode Link"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   195
      Left            =   480
      TabIndex        =   0
      Top             =   450
      Width           =   1200
   End
   Begin VB.Image Image1 
      Height          =   14535
      Left            =   0
      Picture         =   "Broker.frx":2747
      Stretch         =   -1  'True
      Top             =   0
      Width           =   20895
   End
End
Attribute VB_Name = "Form4"
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
    Text1.SetFocus
End Sub

Private Sub Command2_Click()
    Dim msql As String
    If Text1.Text <> "" And Text2.Text <> "" Then
        msql = "select * from TBroker where kd_broker='" & Text1.Text & "'"
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
            msql = "delete from TBroker where kd_broker ='" & Text1.Text & "'"
            con.Execute msql, , adCmdText
        End If
        msql = "Insert Into TBroker " _
               & "([kd_broker],[Nama_broker],[Alamat],[Telpon]) " _
                   & "VALUES ('" & Text1.Text & "', '" & Text2.Text & "', '" & Text3.Text & "', '" & Text4.Text & "');"
            con.Execute msql, , adCmdText
        Command1.SetFocus
    End If
    Call layar
End Sub

Sub layar()
    Dim msql As String
    msql = "select * from TBroker"
    Adodc1.RecordSource = msql
    Adodc1.Refresh
    Adodc1.Refresh
End Sub

Private Sub Command3_Click()
    If Text1.Text <> "" And Text2.Text <> "" Then
        msql = "select * from TBroker where kd_broker='" & Text1.Text & "'"
        Set rs = con.Execute(msql)
    
        If Not rs.EOF Then
            pesan = MsgBox("APAKAH ANDA YAKIN INGIN MENGHAPUS DATA INI ?", vbYesNo, "JAYA MOTOR")
            If pesan = vbYes Then
                msql = "delete from TBroker where kd_broker ='" & Text1.Text & "'"
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

Private Sub DataGrid1_DblClick()
    On Error Resume Next
    Text1.Text = RTrim(Adodc1.Recordset!kd_Broker)
    Text2.Text = RTrim(Adodc1.Recordset!Nama_broker)
    Text3.Text = RTrim(Adodc1.Recordset!Alamat)
    Text4.Text = RTrim(Adodc1.Recordset!Telpon)
End Sub

Private Sub Form_Load()
    Set con = New ADODB.Connection
    con.Open "Softtech"
    
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text4.Text = ""
    
    Top = 0
    Left = 0
    
End Sub

Private Sub Text1_Change()
    If Text1.Text <> "" Then
        Adodc1.RecordSource = "select * from TBroker where kd_broker LIKE '" & Text1.Text & "%" & "' order by kd_broker"
        Adodc1.Refresh
    End If
End Sub

Private Sub Text1_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text1.Text <> "" Then
            msql = "select * from TBroker where kd_broker='" & Text1.Text & "'"
        
            Set rs = con.Execute(msql)
            
            With rs
                If Not .EOF Then
                    Text1.Text = RTrim(!kd_Broker)
                    Text2.Text = RTrim(!Nama_broker)
                    Text3.Text = RTrim(!Alamat)
                    Text4.Text = RTrim(!Telpon)
                Else
                    Text2.Text = ""
                    Text2.SetFocus
                End If
                .Close
            End With
            Adodc1.Refresh
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

Private Sub Text4_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text4.Text = "" Then
            Text4.Text = "-"
        End If
        Command2.SetFocus
    End If
End Sub
