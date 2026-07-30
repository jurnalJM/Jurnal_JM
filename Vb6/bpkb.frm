VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{86CF1D34-0C5F-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCT2.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Begin VB.Form Form24 
   BackColor       =   &H00EC6962&
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Informasi Surat BPKB Sudah Keluar"
   ClientHeight    =   8640
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   8325
   Icon            =   "bpkb.frx":0000
   LinkTopic       =   "Form24"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   8640
   ScaleWidth      =   8325
   ShowInTaskbar   =   0   'False
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "KELUAR"
      Height          =   1095
      Left            =   2040
      Picture         =   "bpkb.frx":08CA
      Style           =   1  'Graphical
      TabIndex        =   6
      Top             =   7200
      Width           =   1095
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00979B04&
      Caption         =   "BARU"
      Height          =   1095
      Left            =   600
      Picture         =   "bpkb.frx":1073
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   7200
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Height          =   495
      Left            =   7080
      Picture         =   "bpkb.frx":171B
      Style           =   1  'Graphical
      TabIndex        =   1
      Top             =   480
      Width           =   495
   End
   Begin MSDataGridLib.DataGrid DataGrid1 
      Bindings        =   "bpkb.frx":1B5D
      Height          =   6015
      Left            =   600
      TabIndex        =   0
      Top             =   1080
      Width           =   6855
      _ExtentX        =   12091
      _ExtentY        =   10610
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
      ColumnCount     =   3
      BeginProperty Column00 
         DataField       =   "Tgl_KelBPKB"
         Caption         =   "Tanggal Keluar BPKB"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd MMM yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   "No_mesin"
         Caption         =   "Nomor Mesin"
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
      BeginProperty Column02 
         DataField       =   "Nama_Pemilik"
         Caption         =   "Nama Pemilik Surat"
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
      SplitCount      =   1
      BeginProperty Split0 
         MarqueeStyle    =   3
         RecordSelectors =   0   'False
         BeginProperty Column00 
            ColumnAllowSizing=   0   'False
            ColumnWidth     =   1709,858
         EndProperty
         BeginProperty Column01 
            ColumnAllowSizing=   0   'False
            ColumnWidth     =   2145,26
         EndProperty
         BeginProperty Column02 
            ColumnAllowSizing=   0   'False
            ColumnWidth     =   2894,74
         EndProperty
      EndProperty
   End
   Begin MSAdodcLib.Adodc Adodc1 
      Height          =   735
      Left            =   840
      Top             =   6720
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
      RecordSource    =   "select * from TSurat where KeluarBPKB='Sudah'"
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
   Begin MSComCtl2.DTPicker DTPicker1 
      Height          =   375
      Left            =   2880
      TabIndex        =   2
      Top             =   480
      Width           =   1935
      _ExtentX        =   3413
      _ExtentY        =   661
      _Version        =   393216
      Format          =   59310080
      CurrentDate     =   38208
   End
   Begin MSComCtl2.DTPicker DTPicker2 
      Height          =   375
      Left            =   5040
      TabIndex        =   3
      Top             =   480
      Width           =   1935
      _ExtentX        =   3413
      _ExtentY        =   661
      _Version        =   393216
      Format          =   59310080
      CurrentDate     =   38208
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Tanggal Pembayaran"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   195
      Left            =   600
      TabIndex        =   4
      Top             =   600
      Width           =   1815
   End
   Begin VB.Image Image1 
      Height          =   14535
      Left            =   0
      Picture         =   "bpkb.frx":1B72
      Stretch         =   -1  'True
      Top             =   0
      Width           =   20895
   End
End
Attribute VB_Name = "Form24"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub Command1_Click()
    Dim msql As String
    msql = "select * from TSurat where KeluarBPKB='Sudah'"
    Adodc1.RecordSource = msql
    Adodc1.Refresh
    Adodc1.Refresh
    DTPicker1.Value = Date
    DTPicker2.Value = Date
End Sub

Private Sub Command2_Click()
    Dim msql As String
    msql = "select * from TSurat where KeluarBPKB='Sudah' and tgl_keluarBPKB >= '" & Format(DTPicker1.Value, "MM-dd-yy") & "' and tgl_keluarBPKB <= '" & Format(DTPicker2.Value, "MM-dd-yy") & "'"
    Adodc1.RecordSource = msql
    Adodc1.Refresh
    Adodc1.Refresh
End Sub

Private Sub Command4_Click()
    Unload Me
End Sub

Private Sub Form_Load()
    DTPicker1.Value = Date
    DTPicker2.Value = Date
    Left = 0
    Top = 0

End Sub

