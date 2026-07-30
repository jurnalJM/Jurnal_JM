VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{86CF1D34-0C5F-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCT2.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Begin VB.Form Form6 
   BackColor       =   &H00EC6962&
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Penjualan Motor"
   ClientHeight    =   7845
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   12705
   Icon            =   "JualSubsidi.frx":0000
   LinkTopic       =   "Form6"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   7845
   ScaleWidth      =   12705
   ShowInTaskbar   =   0   'False
   Begin VB.TextBox Text19 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   7455
      IMEMode         =   3  'DISABLE
      Left            =   240
      MaxLength       =   15
      PasswordChar    =   "*"
      TabIndex        =   83
      Text            =   "Text1"
      Top             =   120
      Width           =   12255
   End
   Begin VB.TextBox Text20 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      MaxLength       =   20
      TabIndex        =   86
      Text            =   "20"
      Top             =   2280
      Width           =   4455
   End
   Begin MSAdodcLib.Adodc Adodc2 
      Height          =   735
      Left            =   7920
      Top             =   3720
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
      RecordSource    =   "select * from TAlamat order by kd_alamat"
      Caption         =   "Adodc2"
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
   Begin VB.Frame Frame7 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Caption         =   "Frame5"
      Height          =   2415
      Left            =   2160
      TabIndex        =   84
      Top             =   3240
      Width           =   4455
      Begin MSDataGridLib.DataGrid DataGrid2 
         Bindings        =   "JualSubsidi.frx":08CA
         Height          =   2175
         Left            =   120
         TabIndex        =   85
         Top             =   120
         Width           =   4215
         _ExtentX        =   7435
         _ExtentY        =   3836
         _Version        =   393216
         AllowUpdate     =   0   'False
         BackColor       =   12648447
         ColumnHeaders   =   0   'False
         HeadLines       =   1
         RowHeight       =   15
         FormatLocked    =   -1  'True
         BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
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
         ColumnCount     =   1
         BeginProperty Column00 
            DataField       =   "Kd_Alamat"
            Caption         =   ""
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
            BeginProperty Column00 
               ColumnWidth     =   3855,118
            EndProperty
         EndProperty
      End
   End
   Begin MSAdodcLib.Adodc Adodc1 
      Height          =   735
      Left            =   6720
      Top             =   7440
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
      RecordSource    =   "select * from TNoSIN where kd_type='ucha'"
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
   Begin VB.Frame Frame5 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Caption         =   "Frame5"
      Height          =   2415
      Left            =   2160
      TabIndex        =   80
      Top             =   3720
      Width           =   3135
      Begin MSDataGridLib.DataGrid DataGrid1 
         Bindings        =   "JualSubsidi.frx":08DF
         Height          =   2175
         Left            =   120
         TabIndex        =   81
         Top             =   120
         Width           =   2895
         _ExtentX        =   5106
         _ExtentY        =   3836
         _Version        =   393216
         AllowUpdate     =   0   'False
         BackColor       =   12648447
         ColumnHeaders   =   0   'False
         HeadLines       =   1
         RowHeight       =   15
         FormatLocked    =   -1  'True
         BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
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
         ColumnCount     =   1
         BeginProperty Column00 
            DataField       =   "No_mesin"
            Caption         =   ""
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
            BeginProperty Column00 
               ColumnWidth     =   2415,118
            EndProperty
         EndProperty
      End
   End
   Begin VB.Frame Frame3 
      BackColor       =   &H00EC6962&
      BorderStyle     =   0  'None
      Height          =   2415
      Left            =   6120
      TabIndex        =   59
      Top             =   7800
      Width           =   5895
      Begin VB.CommandButton Command5 
         BackColor       =   &H00FF8080&
         Caption         =   "OK"
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   0
         Style           =   1  'Graphical
         TabIndex        =   60
         Top             =   0
         Width           =   1215
      End
      Begin MSComCtl2.DTPicker DTPicker4 
         Height          =   375
         Left            =   2160
         TabIndex        =   61
         Top             =   960
         Width           =   2055
         _ExtentX        =   3625
         _ExtentY        =   661
         _Version        =   393216
         BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Format          =   95354880
         CurrentDate     =   38200
      End
      Begin VB.Image Image1 
         Height          =   660
         Left            =   840
         Picture         =   "JualSubsidi.frx":08F4
         Top             =   960
         Width           =   720
      End
      Begin VB.Label Label30 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Masukkan Tanggal Perjanjian Penyelesaian Uang Muka"
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
         Left            =   600
         TabIndex        =   62
         Top             =   480
         Width           =   4665
      End
      Begin VB.Shape Shape28 
         FillStyle       =   0  'Solid
         Height          =   375
         Left            =   2280
         Top             =   1080
         Width           =   2055
      End
   End
   Begin VB.Frame Frame4 
      BackColor       =   &H00EC6962&
      Height          =   1575
      Left            =   0
      TabIndex        =   48
      Top             =   9240
      Visible         =   0   'False
      Width           =   5655
      Begin VB.OptionButton Option4 
         BackColor       =   &H00EC6962&
         Caption         =   "Belum"
         Height          =   495
         Left            =   3720
         TabIndex        =   16
         Top             =   240
         Visible         =   0   'False
         Width           =   1215
      End
      Begin VB.OptionButton Option3 
         BackColor       =   &H00EC6962&
         Caption         =   "Sekarang"
         Height          =   495
         Left            =   1920
         TabIndex        =   15
         Top             =   240
         Value           =   -1  'True
         Width           =   1215
      End
      Begin MSComCtl2.DTPicker DTPicker2 
         Height          =   375
         Left            =   1920
         TabIndex        =   17
         Top             =   840
         Visible         =   0   'False
         Width           =   2055
         _ExtentX        =   3625
         _ExtentY        =   661
         _Version        =   393216
         Format          =   95354880
         CurrentDate     =   38200
      End
      Begin VB.Shape Shape23 
         FillStyle       =   0  'Solid
         Height          =   375
         Left            =   2040
         Top             =   960
         Visible         =   0   'False
         Width           =   2055
      End
      Begin VB.Label Label26 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Tanggal Keluar"
         BeginProperty Font 
            Name            =   "Verdana"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00000000&
         Height          =   195
         Left            =   240
         TabIndex        =   50
         Top             =   840
         Visible         =   0   'False
         Width           =   1470
      End
      Begin VB.Label Label25 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Motor Keluar"
         BeginProperty Font 
            Name            =   "Verdana"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H00000000&
         Height          =   195
         Left            =   240
         TabIndex        =   49
         Top             =   480
         Width           =   1245
      End
   End
   Begin VB.TextBox Text18 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   5400
      MaxLength       =   5
      TabIndex        =   78
      Text            =   "Text1"
      Top             =   600
      Width           =   1095
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00979B04&
      Caption         =   "HAPUS"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   10080
      Picture         =   "JualSubsidi.frx":113A
      Style           =   1  'Graphical
      TabIndex        =   75
      Top             =   6360
      Visible         =   0   'False
      Width           =   1095
   End
   Begin VB.CommandButton Command6 
      BackColor       =   &H00979B04&
      Caption         =   "EDIT"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   9000
      Picture         =   "JualSubsidi.frx":18BD
      Style           =   1  'Graphical
      TabIndex        =   74
      ToolTipText     =   "Cetak"
      Top             =   6360
      Width           =   1095
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "KELUAR"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   11280
      Picture         =   "JualSubsidi.frx":2000
      Style           =   1  'Graphical
      TabIndex        =   71
      Top             =   6360
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Caption         =   "SIMPAN"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   7920
      Picture         =   "JualSubsidi.frx":27A9
      Style           =   1  'Graphical
      TabIndex        =   70
      Top             =   6360
      Width           =   1095
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00979B04&
      Caption         =   "BARU"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   1095
      Left            =   6840
      Picture         =   "JualSubsidi.frx":3037
      Style           =   1  'Graphical
      TabIndex        =   69
      Top             =   6360
      Width           =   1095
   End
   Begin VB.TextBox Text17 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      MaxLength       =   20
      TabIndex        =   66
      Text            =   "Text3"
      Top             =   3240
      Width           =   3135
   End
   Begin VB.TextBox Text16 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      MaxLength       =   15
      TabIndex        =   0
      Text            =   "Text1"
      Top             =   120
      Width           =   2175
   End
   Begin VB.TextBox Text15 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   615
      Left            =   2160
      MaxLength       =   100
      MultiLine       =   -1  'True
      ScrollBars      =   2  'Vertical
      TabIndex        =   64
      Text            =   "JualSubsidi.frx":36DF
      Top             =   1560
      Width           =   4455
   End
   Begin VB.ComboBox Combo1 
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   315
      Left            =   2160
      Style           =   2  'Dropdown List
      TabIndex        =   58
      Top             =   5820
      Width           =   2055
   End
   Begin VB.TextBox Text9 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   8880
      MaxLength       =   11
      TabIndex        =   19
      Text            =   "Text9"
      Top             =   5280
      Width           =   3135
   End
   Begin VB.TextBox Text10 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   8880
      MaxLength       =   11
      TabIndex        =   20
      Text            =   "Text10"
      Top             =   5760
      Width           =   3135
   End
   Begin VB.Frame Frame6 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Height          =   2415
      Left            =   6720
      TabIndex        =   43
      Top             =   2280
      Width           =   5655
      Begin VB.TextBox Text13 
         Alignment       =   1  'Right Justify
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   2160
         MaxLength       =   11
         TabIndex        =   11
         Text            =   "Text13"
         Top             =   240
         Width           =   3135
      End
      Begin VB.TextBox Text14 
         Alignment       =   1  'Right Justify
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   2160
         MaxLength       =   11
         TabIndex        =   12
         Text            =   "Text14"
         Top             =   840
         Width           =   3135
      End
      Begin VB.TextBox Text12 
         Alignment       =   1  'Right Justify
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   2160
         MaxLength       =   11
         TabIndex        =   14
         Text            =   "Text12"
         Top             =   1800
         Visible         =   0   'False
         Width           =   3135
      End
      Begin VB.TextBox Text11 
         Alignment       =   1  'Right Justify
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   2160
         MaxLength       =   11
         TabIndex        =   13
         Text            =   "Text11"
         Top             =   1320
         Width           =   3135
      End
      Begin VB.Label Label35 
         Alignment       =   1  'Right Justify
         Appearance      =   0  'Flat
         BackColor       =   &H00C0C0FF&
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Label13"
         ForeColor       =   &H80000008&
         Height          =   375
         Left            =   2160
         TabIndex        =   63
         Top             =   1800
         Width           =   3135
      End
      Begin VB.Label Label34 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Leasing / AHM"
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
         Left            =   120
         TabIndex        =   47
         Top             =   1890
         Width           =   1215
      End
      Begin VB.Label Label39 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Dealer"
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
         Left            =   120
         TabIndex        =   46
         Top             =   1410
         Width           =   555
      End
      Begin VB.Label Label22 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "AHM / Main Dealer"
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
         Left            =   120
         TabIndex        =   45
         Top             =   930
         Width           =   1575
      End
      Begin VB.Label Label31 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Dana Subsidi"
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
         Left            =   120
         TabIndex        =   44
         Top             =   330
         Width           =   1080
      End
   End
   Begin VB.TextBox Text1 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      MaxLength       =   15
      TabIndex        =   1
      Text            =   "Text1"
      Top             =   1080
      Width           =   4455
   End
   Begin VB.OptionButton Option1 
      BackColor       =   &H00C0C0FF&
      Caption         =   "&Cash"
      Height          =   495
      Left            =   11040
      TabIndex        =   3
      Top             =   0
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.OptionButton Option2 
      BackColor       =   &H00C0C0FF&
      Caption         =   "&Kredit"
      Height          =   495
      Left            =   5640
      TabIndex        =   4
      Top             =   0
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.TextBox Text2 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      Locked          =   -1  'True
      MaxLength       =   10
      TabIndex        =   2
      Text            =   "Text2"
      Top             =   3720
      Width           =   2775
   End
   Begin VB.TextBox Text3 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      MaxLength       =   20
      TabIndex        =   8
      Text            =   "Text3"
      Top             =   2760
      Width           =   3135
   End
   Begin VB.TextBox Text4 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   2160
      MaxLength       =   3
      TabIndex        =   9
      Text            =   "Text4"
      Top             =   5160
      Width           =   2295
   End
   Begin VB.TextBox Text5 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   10200
      MaxLength       =   11
      TabIndex        =   10
      Text            =   "Text5"
      Top             =   1680
      Width           =   1815
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Height          =   1335
      Left            =   240
      TabIndex        =   24
      Top             =   6240
      Width           =   6375
      Begin VB.TextBox Text6 
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   1920
         MaxLength       =   10
         TabIndex        =   5
         Text            =   "Text6"
         Top             =   240
         Width           =   3135
      End
      Begin VB.Label Label16 
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Label16"
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H80000008&
         Height          =   375
         Left            =   1920
         TabIndex        =   41
         Top             =   840
         Width           =   4335
      End
      Begin VB.Label Label14 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Kode Leasing"
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
         Left            =   0
         TabIndex        =   26
         Top             =   240
         Width           =   1110
      End
      Begin VB.Label Label15 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Nama Leasing"
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
         Left            =   0
         TabIndex        =   25
         Top             =   840
         Width           =   1170
      End
   End
   Begin VB.TextBox Text7 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   8880
      MaxLength       =   10
      TabIndex        =   6
      Text            =   "Text7"
      Top             =   480
      Width           =   3135
   End
   Begin VB.Frame Frame2 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Height          =   1335
      Left            =   6840
      TabIndex        =   21
      Top             =   1080
      Width           =   5535
      Begin VB.TextBox Text8 
         Alignment       =   1  'Right Justify
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   375
         Left            =   2040
         MaxLength       =   11
         TabIndex        =   7
         Text            =   "Text8"
         Top             =   600
         Visible         =   0   'False
         Width           =   2895
      End
      Begin VB.Label Label9 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Discount (Rp.)"
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
         Left            =   0
         TabIndex        =   82
         Top             =   720
         Width           =   1200
      End
      Begin VB.Label Label19 
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         BorderStyle     =   1  'Fixed Single
         Caption         =   "Label16"
         BeginProperty Font 
            Name            =   "Tahoma"
            Size            =   8.25
            Charset         =   0
            Weight          =   400
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         ForeColor       =   &H80000008&
         Height          =   375
         Left            =   2040
         TabIndex        =   42
         Top             =   120
         Width           =   3135
      End
      Begin VB.Label Label20 
         AutoSize        =   -1  'True
         BackStyle       =   0  'Transparent
         Caption         =   "Komisi Link"
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
         Left            =   0
         TabIndex        =   23
         Top             =   600
         Visible         =   0   'False
         Width           =   945
      End
      Begin VB.Label Label18 
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
         Left            =   0
         TabIndex        =   22
         Top             =   120
         Width           =   870
      End
   End
   Begin MSComCtl2.DTPicker DTPicker1 
      Height          =   375
      Left            =   2160
      TabIndex        =   27
      Top             =   600
      Width           =   1935
      _ExtentX        =   3413
      _ExtentY        =   661
      _Version        =   393216
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Format          =   95354880
      CurrentDate     =   38200
   End
   Begin MSComCtl2.DTPicker DTPicker3 
      Height          =   375
      Left            =   8880
      TabIndex        =   18
      Top             =   4800
      Width           =   2055
      _ExtentX        =   3625
      _ExtentY        =   661
      _Version        =   393216
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Format          =   95354880
      CurrentDate     =   38200
   End
   Begin VB.Label Label45 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "L45"
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
      Left            =   0
      TabIndex        =   88
      Top             =   0
      Visible         =   0   'False
      Width           =   300
   End
   Begin VB.Label Label38 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "HandPhone"
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
      Left            =   240
      TabIndex        =   87
      Top             =   2370
      Width           =   960
   End
   Begin VB.Label Label44 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Wilayah"
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
      Left            =   4320
      TabIndex        =   79
      Top             =   690
      Width           =   675
   End
   Begin VB.Label Label43 
      Caption         =   "cek"
      Height          =   495
      Left            =   5400
      TabIndex        =   77
      Top             =   2760
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label42 
      Caption         =   "Label42"
      Height          =   495
      Left            =   4440
      TabIndex        =   76
      Top             =   3840
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label41 
      Caption         =   "Label41"
      Height          =   495
      Left            =   4440
      TabIndex        =   73
      Top             =   3840
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label40 
      Caption         =   "Label40"
      Height          =   495
      Left            =   6120
      TabIndex        =   72
      Top             =   0
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label33 
      Caption         =   "Label38"
      Height          =   495
      Left            =   5760
      TabIndex        =   68
      Top             =   4200
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label37 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "No. Rangka"
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
      Left            =   240
      TabIndex        =   67
      Top             =   3330
      Width           =   945
   End
   Begin VB.Label Label36 
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
      Left            =   240
      TabIndex        =   65
      Top             =   1650
      Width           =   615
   End
   Begin VB.Label Label32 
      Caption         =   "Belum"
      Height          =   495
      Left            =   4800
      TabIndex        =   57
      Top             =   -120
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label21 
      Caption         =   "Label21"
      Height          =   495
      Left            =   11280
      TabIndex        =   56
      Top             =   1800
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label24 
      Caption         =   "Label24"
      Height          =   495
      Left            =   11160
      TabIndex        =   55
      Top             =   720
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label23 
      Caption         =   "Label23"
      Height          =   495
      Left            =   10920
      TabIndex        =   54
      Top             =   2520
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label29 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Uang Muka Dibayar"
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
      Left            =   6840
      TabIndex        =   53
      Top             =   5850
      Width           =   1650
   End
   Begin VB.Label Label28 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Ketentuan DP"
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
      Left            =   6840
      TabIndex        =   52
      Top             =   5370
      Width           =   1155
   End
   Begin VB.Label Label27 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Tanggal Bayar"
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
      Left            =   6840
      TabIndex        =   51
      Top             =   4800
      Width           =   1215
   End
   Begin VB.Label Label10 
      Appearance      =   0  'Flat
      BackColor       =   &H00C0C0FF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label10"
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   2160
      TabIndex        =   40
      Top             =   120
      Width           =   2175
   End
   Begin VB.Label LABEL12 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label12"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   2160
      TabIndex        =   39
      Top             =   4200
      Visible         =   0   'False
      Width           =   4455
   End
   Begin VB.Label Label13 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label13"
      BeginProperty Font 
         Name            =   "Tahoma"
         Size            =   8.25
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   2160
      TabIndex        =   38
      Top             =   4680
      Width           =   2655
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "No. Transaksi"
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
      Left            =   240
      TabIndex        =   37
      Top             =   210
      Width           =   1125
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Tanggal"
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
      Left            =   240
      TabIndex        =   36
      Top             =   690
      Width           =   675
   End
   Begin VB.Label Label3 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Sistem Pembayaran"
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
      Left            =   240
      TabIndex        =   35
      Top             =   5880
      Width           =   1710
   End
   Begin VB.Label Label4 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Nama Pemohon"
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
      Left            =   240
      TabIndex        =   34
      Top             =   1170
      Width           =   1320
   End
   Begin VB.Label Label5 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Harga Dasar"
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
      Left            =   240
      TabIndex        =   33
      Top             =   4770
      Width           =   1050
   End
   Begin VB.Label Label6 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "No. Mesin Motor"
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
      Left            =   240
      TabIndex        =   32
      Top             =   2850
      Width           =   1350
   End
   Begin VB.Label Label7 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Warna"
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
      Left            =   240
      TabIndex        =   31
      Top             =   5250
      Width           =   555
   End
   Begin VB.Label Label8 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Kode Type Motor"
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
      Left            =   240
      TabIndex        =   30
      Top             =   3810
      Width           =   1440
   End
   Begin VB.Label Label11 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Nama Type Motor"
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
      Left            =   240
      TabIndex        =   29
      Top             =   4290
      Visible         =   0   'False
      Width           =   1500
   End
   Begin VB.Label Label17 
      AutoSize        =   -1  'True
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
      Left            =   6840
      TabIndex        =   28
      Top             =   480
      Width           =   810
   End
   Begin VB.Image Image2 
      Height          =   14535
      Left            =   0
      Picture         =   "JualSubsidi.frx":36E6
      Stretch         =   -1  'True
      Top             =   0
      Width           =   20895
   End
End
Attribute VB_Name = "Form6"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim con As ADODB.Connection
Dim rs As ADODB.Recordset

Private Sub Combo1_Click()
    If Combo1.Text = "Cash" Then
        Label23.Caption = "Cash"
        Frame1.Enabled = False
        Text6.Text = "JM"
        Label16.Caption = "JAYA MOTOR"
        'Text9.Text = Label13.Caption
        'Text9.Enabled = False
        'Text10.Enabled = False
    Else
        Frame1.Enabled = True
        Label23.Caption = "Kredit"
        Text9.Enabled = True
        'Text9.Text = ""
        Text10.Enabled = True
       'Text6.Text = ""
        Label16.Caption = ""
    End If
End Sub

Private Sub Combo1_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Combo1.Text = "Cash" Then
            Frame1.Enabled = False
            Text9.Enabled = False
            Text10.Enabled = False
            Text7.Enabled = True
            Text7.SetFocus
            Label23.Caption = "Cash"
        ElseIf Combo1.Text = "Kredit" Then
            Frame1.Enabled = True
            Text9.Enabled = True
            Text10.Enabled = True
            Text6.Enabled = True
            Text6.SetFocus
            Label23.Caption = "Kredit"
        End If
    End If
End Sub

Private Sub Command1_Click()
 '   Call buat_baru
 '   Call load_nomor
    
    If frmLogin.Combo1.Text = "USER" Then
        Command6.Enabled = False
    Else
        Command6.Enabled = True
    End If
    Command6.Enabled = False
    
    Command2.Enabled = True
'    DTPicker1.Value = Date
    Text1.Text = ""
    Label24.Caption = "Sudah"
    Text2.Text = ""
    Text18.Text = ""
    Text1.Locked = True
    Text3.Text = ""
    Text4.Text = ""
    Label42.Caption = "cek"
    Label45.Caption = ""
    Text5.Text = "0"
    Text6.Text = ""
    Text7.Text = ""
    Text8.Text = ""
    Text9.Text = ""
    Text10.Text = ""
    Text11.Text = ""
    Text20.Text = ""
    Combo1.Clear
    Combo1.AddItem "Cash"
    Combo1.AddItem "Kredit"
    Label35.Caption = ""
    Text13.Text = ""
    Text14.Text = ""
    Label12.Caption = ""
    Label13.Caption = ""
    Label16.Caption = ""
    Label19.Caption = ""
    DTPicker2.Value = Date
'    DTPicker3.Value = Date
    Label23.Caption = ""
    Label24.Caption = ""
    Option3.Value = False
    Option4.Value = False
    Frame1.Enabled = False
    DTPicker2.Enabled = False
    Text7.Enabled = False
    Frame3.Visible = False
    Text1.Enabled = True
    Text15.Text = ""
    Text16.Text = ""
    Text17.Text = ""
    DTPicker4.Value = Date
    Text9.Text = ""
    Text16.SetFocus

End Sub

Sub baruss()
    Command2.Enabled = True
  '  DTPicker1.Value = Date
    Text1.Text = ""
    Label24.Caption = "Sudah"
    Text2.Text = ""
    Text1.Locked = True
    Text3.Text = ""
    Text4.Text = ""
    Text18.Text = ""
    Label42.Caption = ""
    Text5.Text = "0"
    Text6.Text = ""
    Text7.Text = ""
    Text8.Text = ""
    Text9.Text = ""
    Text10.Text = ""
    Text11.Text = ""
    Combo1.Clear
    Combo1.AddItem "Cash"
    Combo1.AddItem "Kredit"
    Label35.Caption = ""
    Text13.Text = ""
    Text14.Text = ""
    Label12.Caption = ""
    Label13.Caption = ""
    Label16.Caption = ""
    Label19.Caption = ""
    DTPicker2.Value = Date
  '  DTPicker3.Value = Date
    Label23.Caption = ""
    Label24.Caption = ""
    Option3.Value = False
    Option4.Value = False
    Frame1.Enabled = False
    DTPicker2.Enabled = False
    Text7.Enabled = False
    Frame3.Visible = False
    Text1.Enabled = True
    Text15.Text = ""
    Text17.Text = ""
    DTPicker4.Value = Date
    Text9.Text = ""
    Text16.SetFocus

End Sub
Private Sub Command2_Click()
    Label43.Caption = "biasa"
    Label40.Caption = "0"
    Label40.Caption = Val(Format(Label13.Caption, "")) - Val(Format(Text9.Text, ""))
    Label40.Caption = Val(Label40.Caption) + Val(Format(Text12.Text, ""))
    If Text1.Text <> "" And Text3.Text <> "" And Label19.Caption <> "" And Text15.Text <> "" And Text17.Text <> "" And Text7.Text <> "" Then ' And Text9.Text <> "" And Text10.Text <> "" Then
    cekmuka = Val(Format(Text9.Text, "")) - Val(Format(Text13.Text, "")) 'belum disc
        If Val(cekmuka) > Val(Format(Text10.Text, "")) Then
            DTPicker4.Value = DateSerial(2001, 1, 1)
            Command5_Click
            'pesan = MsgBox("UANG MUKA YANG DIBAYARKAN BELUM MENCUKUPI", vbOKCancel, "JAYA MOTOR")
            'If pesan = vbOK Then
            '    Frame3.Visible = True
            '    Frame3.Top = 5000
            '    Frame3.Left = 7000
            '    DTPicker4.Value = Date
            '    DTPicker4.Enabled = True
            '    DTPicker4.SetFocus
            'Else
            '    Text10.Enabled = True
            '    Text10.SetFocus
            '    SendKeys "{Home}+{end}"
            'End If
        Else
            If Val(Format(Text9.Text, "")) > 0 Then
                Text10.Text = Format(cekmuka, "###,###")
            Else
                Text10.Text = ""
            End If
            'Call tmb_nomor
            If Label24.Caption = "Sudah" Then
            '    Call cekstok
                Call STOK_KURANG
            End If
            Call sav_infr    'server
            Call sav_infr2    'client
            Dim msql As String
            msql = "Insert Into TPenjualan " _
                & "([Nota],[Tanggal],[nama_pemohon],[Sistem_bayar],[Harga_dasar],[Subsidi],[No_Mesin],[DP],[BayarDP],[Warna],[Tgl_bayar],[kd_type],[Disc],[tgl_janjian],[Alamat],[No_rangka],[kd_broker]) " _
                & "VALUES ('" & Text16.Text & "', '" & Format(DTPicker1.Value, "MM-dd-yy") & "', '" & Text1.Text & "', '" & Format(Label23.Caption, "") & "', '" & Val(Format(Label13.Caption, "")) & "', '" & "Ya" & "', '" & Text3.Text & "', '" & Val(Format(Text9.Text, "")) & "', '" & Val(Format(Text10.Text, "")) & "', '" & Text4.Text & "', '" & Format(DTPicker3.Value, "MM-dd-yy") & "', '" & Text2.Text & "', '" & Val(Format(Text5.Text, "")) & "', '" & Format(DTPicker4.Value, "MM-dd-yy") & "', '" & Text15.Text & "', '" & Text17.Text & "', '" & Text7.Text & "');"
                con.Execute msql, , adCmdText
            
           ' Call save_komisi
            If Label23.Caption = "Kredit" Then
                Call save_lising
            End If
    
            Call save_PiutBroker
            Call save_status
            Call save_subsidi
            Call cicilanDP
            MsgBox "DATA TERSEBUT TELAH DISIMPAN", , "JAYA MOTOR"
            Command1_Click
        End If
    Else
        MsgBox "DATA BELUM LENGKAP !", , "JAYA MOTOR"
    End If
End Sub

Sub cicilanDP()
    Dim msql As String
    msql = "select * from TCicilan where No_mesin='" & Text3.Text & "' and tanggal_Cicil= '" & Format(DTPicker3.Value, "MM-dd-yy") & "'"
        
    Set rs = con.Execute(msql)
        
    With rs
        If .EOF Then
            msql = "Insert Into TCicilan " _
                 & "([Tanggal_Cicil],[No_Mesin],[Nominal]) " _
                 & "VALUES ('" & Format(DTPicker3.Value, "MM-dd-yy") & "', '" & Text3.Text & "', '" & Val(Format(Text10.Text, "")) & "');"
            con.Execute msql, , adCmdText
        Else
            msql = "update TCicilan set " & _
                " Nominal ='" & Val(Format(Text10.Text, "")) & "' " & _
                " where No_mesin='" & Text3.Text & "' and tanggal_Cicil= '" & Format(DTPicker3.Value, "MM-dd-yy") & "'"
            con.Execute msql, , adCmdText
        End If
    End With
End Sub

Sub sav_infr()
    KETENTUAN = Val(Format(Text9.Text, ""))
    terang = MonthName(Month(DTPicker1.Value)) & " " & Year(DTPicker1.Value)
    Dim NotePO As String
    Dim reLain As String
    Dim msql As String
    If Combo1.Text = "Cash" Then
        NotePO = "Cash Sale"
        reLain = "1"
    Else
        NotePO = "-"
        reLain = "0"
    End If
    msql = "Insert Into TInformasi_01 " _
        & "([Tanggal],[Nota],[Nama],[Alamat],[Telp],[Broker],[No_rangka],[No_Mesin],[type],[Warna],[Ket_DP],[DP],[Piutang_tempo],[kd_lising],[Tgl_lunas],[Pelunasan],[No_polisi],[Nama_pemilik],[No_BPKB],[Tgl_serahTerima],[Subsidi],[Keterangan],[Disc],[komisi_broker],[Post],[wilayah],[Refund],[Lain_lain],[Tgl_refund],[Disc_tambahan],[Tanggal_PO],[Tanggal_Fee]) " _
        & "VALUES ('" & Format(DTPicker1.Value, "MM-dd-yy") & "', '" & Text16.Text & "', '" & Text1.Text & "', '" & Text15.Text & "', '" & Text20.Text & "', '" & Text7.Text & "', '" & Text17.Text & "', '" & Text3.Text & "', '" & Text2.Text & "', '" & Text4.Text & "', '" & Val(KETENTUAN) & "', '" & Val(Format(Text10.Text, "")) & "', '" & Format(DTPicker4.Value, "MM-dd-yy") & "', '" & Text6.Text & "', '" & DateSerial("01", "01", "01") & "', '" & Val("0") & "', '" & "---" & "', '" & "---" & "', '" & "---" & "', '" & DateSerial("01", "01", "01") & "', '" & Val(Format(Text13.Text, "")) & "', '" & terang & "', '" & Val(Format(Text5.Text, "")) & "','" & Val(Format(Text8.Text, "")) & "','tidak','" & Text18.Text & "', '" & Val(reLain) & "', '" & Val(reLain) & "', '" & DateSerial("01", "01", "01") & "','0','" & NotePO & "', '" & DateSerial("01", "01", "01") & "');"
    con.Execute msql, , adCmdText
End Sub

Sub sav_infr2()
    KETENTUAN = Val(Format(Text9.Text, ""))
    terang = MonthName(Month(DTPicker1.Value)) & " " & Year(DTPicker1.Value)
    Dim msql As String
    msql = "Insert Into TTemp_Informasi " _
        & "([Tanggal],[Nota],[Nama],[Alamat],[Broker],[No_rangka],[No_Mesin],[type],[Warna],[Ket_DP],[DP],[Piutang_tempo],[kd_lising],[Tgl_lunas],[Pelunasan],[No_polisi],[Nama_pemilik],[No_BPKB],[Tgl_serahTerima],[Subsidi],[Keterangan],[Disc],[komisi_broker],[wilayah],[Refund],[Lain_lain],[tgl_refund]) " _
        & "VALUES ('" & Format(DTPicker1.Value, "MM-dd-yy") & "', '" & Text16.Text & "', '" & Text1.Text & "', '" & Text15.Text & "', '" & Text7.Text & "', '" & Text17.Text & "', '" & Text3.Text & "', '" & Text2.Text & "', '" & Text4.Text & "', '" & Val(KETENTUAN) & "', '" & Val(Format(Text10.Text, "")) & "', '" & Format(DTPicker4.Value, "MM-dd-yy") & "', '" & Text6.Text & "', '" & DateSerial("01", "01", "01") & "', '" & Val("0") & "', '" & "---" & "', '" & "---" & "', '" & "---" & "', '" & DateSerial("01", "01", "01") & "', '" & Val(Format(Text13.Text, "")) & "', '" & terang & "', '" & Val(Format(Text5.Text, "")) & "','" & Val(Format(Text8.Text, "")) & "','" & Text18.Text & "', '" & Val("0") & "', '" & Val("0") & "', '" & DateSerial("01", "01", "01") & "');"
    con.Execute msql, , adCmdText
End Sub

Sub cekstok()
    Dim msql As String
    msql = "select * from TType where kd_type='" & Text2.Text & "'"
        
    Set rs = con.Execute(msql)
        
    If Not rs.EOF Then
        If rs.Fields("stok_sisa") <= 0 Then
            MsgBox "PERSEDIAN STOK MOTOR TIDAK MENCUKUPI/KOSONG", , "JAYA MOTOR"
            Text2.Enabled = True
            Text2.SetFocus
            SendKeys "{Home}+{End}"
            Exit Sub
        End If
    End If
End Sub

Sub STOK_KURANG()
    Dim msql As String
    msql = "update TNoSIN set " & _
        " Stok=Stok - 1 " & _
        " where no_mesin='" & Text3.Text & "' and stok > 0"
    con.Execute msql, , adCmdText
End Sub

Sub save_subsidi()
  Dim msql As String
    msql = "Insert Into TSubsidi " _
         & "([nota],[No_mesin],[Total_subsidi],[Dealer],[MainDealer],[Lising]) " _
         & "VALUES ('" & Text16.Text & "', '" & Text3.Text & "', '" & Val(Format(Text13.Text, "")) & "', '" & Val(Format(Text14.Text, "")) & "', '" & Val(Format(Text11.Text, "")) & "', '" & Val(Format(Label35.Caption, "")) & "');"
    con.Execute msql, , adCmdText
End Sub

Sub save_lising()
  Dim msql As String
  Dim ststu As String
  If Text9.Text <> "" Then
    Label40.Caption = Val(Format(Label13.Caption, "")) - Val(Format(Text9.Text, "")) + Val(Format(Label35.Caption, ""))
  Else
    Label40.Caption = Val(Format(Label13.Caption, "")) - Val(Format(Text13.Text, ""))
  End If
  ststu = "Belum"
  Dim hitungan As Currency
    msql = "Insert Into TKreditan " _
         & "([nota],[No_mesin],[Kd_lising],[Piutang],[Status],[Bayar],[Konsumen],[tanggal]) " _
         & "VALUES ('" & Text16.Text & "', '" & Text3.Text & "', '" & Text6.Text & "', '" & Val(Label40.Caption) & "', '" & Label32.Caption & "','" & Val("0") & "','" & Text1.Text & "','" & Format(DTPicker1.Value, "MM-dd-yy") & "');"
    con.Execute msql, , adCmdText
End Sub

Sub save_komisi()
  Dim msql As String
    msql = "Insert Into TIntensif " _
         & "([No_mesin],[Kd_broker],[Komisi],[Tanggal]) " _
         & "VALUES ('" & Text3.Text & "', '" & Text7.Text & "', '" & Val(Format(Text8.Text, "")) & "', '" & Format(DTPicker1.Value, "MM-dd-yy") & "');"
    con.Execute msql, , adCmdText
End Sub

Sub save_PiutBroker()
    Dim sisinya As Currency
    If Text9.Text <> "" Then
        If Combo1.Text = "Cash" Then
            Label33.Caption = Val(Format(Label13.Caption, "")) - Val(Format(Text13.Text, ""))
            sisinya = Val(Format(Label13.Caption, "")) - (Val(Format(Text13.Text, "")) + Val(Format(Text10.Text, "")))
        ElseIf Combo1.Text = "Kredit" Then
            Label33.Caption = Val(Format(Text9.Text, "")) - Val(Format(Text13.Text, ""))
            'sisinya = Val(Label33.Caption) - Val(Format(Text9.Text, ""))
            sisinya = Val(Format(Text9.Text, "")) - (Val(Format(Text13.Text, "")) + Val(Format(Text10.Text, "")))
        End If
    Else
        Label33.Caption = Val(Label40.Caption)
        sisinya = Label33.Caption
    End If
    Dim msql As String
    msql = "Insert Into TPiutangBroker " _
         & "([No_mesin],[Kd_broker],[Tanggal],[Biaya],[Sisa]) " _
         & "VALUES ('" & Text3.Text & "', '" & Text7.Text & "', '" & Format(DTPicker3.Value, "MM-dd-yy") & "', '" & Val(Label33.Caption) & "', '" & sisinya & "');"
    con.Execute msql, , adCmdText
End Sub

Sub save_status()
  Dim msql As String
  Dim statusi As String
  statusi = "Belum"
    msql = "Insert Into TStatus_motor " _
         & "([Nota],[No_mesin],[Status_keluar],[Tgl_keluar],[kd_type],[status_suratSTNK],[status_suratBPKB]) " _
         & "VALUES ('" & Text16.Text & "', '" & Text3.Text & "', '" & Label24.Caption & "', '" & Format(DTPicker2.Value, "MM-dd-yy") & "', '" & Text2.Text & "', '" & Label32.Caption & "', '" & Label32.Caption & "');"
    con.Execute msql, , adCmdText
End Sub

Private Sub Command3_Click()
    Dim msql As String
    msql = "delete from TInformasi_01 where nota ='" & Text16.Text & "'"
    con.Execute msql, , adCmdText

    msql = "delete from TTemp_Informasi where nota ='" & Text16.Text & "'"
    con.Execute msql, , adCmdText

    msql = "delete from TPenjualan where nota ='" & Text16.Text & "'"
    con.Execute msql, , adCmdText
    
    msql = "delete from TIntensif where No_mesin ='" & Text3.Text & "'"
    con.Execute msql, , adCmdText
    
    If Label23.Caption = "Kredit" Then
        msql = "delete from TKreditan where nota ='" & Text16.Text & "'"
        con.Execute msql, , adCmdText
    End If
    
    msql = "delete from TPiutangBroker where no_mesin ='" & Text3.Text & "'"
    con.Execute msql, , adCmdText
    
    msql = "delete from TStatus_motor where nota ='" & Text16.Text & "'"
    con.Execute msql, , adCmdText

    msql = "delete from TSubsidi where nota ='" & Text16.Text & "'"
    con.Execute msql, , adCmdText

    msql = "delete from TCicilan where no_mesin ='" & Text3.Text & "'"
    con.Execute msql, , adCmdText
End Sub

Private Sub Command4_Click()
    Unload Me
End Sub

Private Sub Command5_Click()
    Frame3.Visible = False
    Call sav_infr2       'client
    Call sav_infr       'server
    Dim msql As String
    msql = "Insert Into TPenjualan " _
        & "([Nota],[Tanggal],[nama_pemohon],[Sistem_bayar],[Harga_dasar],[Subsidi],[No_Mesin],[DP],[BayarDP],[Warna],[Tgl_bayar],[kd_type],[Disc],[tgl_janjian],[Alamat],[No_rangka],[kd_broker]) " _
        & "VALUES ('" & Text16.Text & "', '" & Format(DTPicker1.Value, "MM-dd-yy") & "', '" & Text1.Text & "', '" & Label23.Caption & "', '" & Val(Format(Label13.Caption, "")) & "', '" & "Ya" & "', '" & Text3.Text & "', '" & Val(Format(Text9.Text, "")) & "', '" & Val(Format(Text10.Text, "")) & "', '" & Text4.Text & "', '" & Format(DTPicker3.Value, "MM-dd-yy") & "', '" & Text2.Text & "', '" & Val(Format(Text5.Text, "")) & "', '" & Format(DTPicker4.Value, "MM-dd-yy") & "', '" & Text15.Text & "', '" & Text17.Text & "', '" & Text7.Text & "');"
    con.Execute msql, , adCmdText
    Call save_komisi
    'Call tmb_nomor
    If Label24.Caption = "Sudah" Then
        If Label43.Caption = "biasa" Then
        '    Call cekstok
            Call STOK_KURANG
        End If
    End If
    If Label23.Caption = "Kredit" Then
        Call save_lising
    End If
    Call save_PiutBroker
    Call save_status
    Call save_subsidi
    Call cicilanDP
    MsgBox "DATA TERSEBUT TELAH DISIMPAN", , "JAYA MOTOR"
    Command1_Click
End Sub

Private Sub Command6_Click()
    Command3_Click
    Label43.Caption = "tidak"
    Label40.Caption = "0"
    Label40.Caption = Val(Format(Label13.Caption, "")) - Val(Format(Text9.Text, ""))
    Label40.Caption = Val(Label40.Caption) + Val(Format(Text12.Text, ""))
    If Text1.Text <> "" And Text3.Text <> "" And Label19.Caption <> "" And Text13.Text <> "" And Text11.Text <> "" And Text15.Text <> "" And Text17.Text <> "" And Text7.Text <> "" Then ' And Text9.Text <> "" And Text10.Text <> "" Then
    cekmuka = Val(Format(Text9.Text, "")) - Val(Format(Text13.Text, "")) 'belum disc
        If Val(cekmuka) > Val(Format(Text10.Text, "")) Then
            DTPicker4.Value = DateSerial(2001, 1, 1)
        Else
            If Val(Format(Text9.Text, "")) > 0 Then
                Text10.Text = Format(cekmuka, "###,###")
            Else
                Text10.Text = ""
            End If
            'Call tmb_nomor        'Call tmb_nomor
        End If
        Call sav_infr   'server
        Call sav_infr2    'client
        Dim msql As String
        msql = "Insert Into TPenjualan " _
            & "([Nota],[Tanggal],[nama_pemohon],[Sistem_bayar],[Harga_dasar],[Subsidi],[No_Mesin],[DP],[BayarDP],[Warna],[Tgl_bayar],[kd_type],[Disc],[tgl_janjian],[Alamat],[No_rangka],[kd_broker]) " _
            & "VALUES ('" & Text16.Text & "', '" & Format(DTPicker1.Value, "MM-dd-yy") & "', '" & Text1.Text & "', '" & Format(Label23.Caption, "") & "', '" & Val(Format(Label13.Caption, "")) & "', '" & "Ya" & "', '" & Text3.Text & "', '" & Val(Format(Text9.Text, "")) & "', '" & Val(Format(Text10.Text, "")) & "', '" & Text4.Text & "', '" & Format(DTPicker3.Value, "MM-dd-yy") & "', '" & Text2.Text & "', '" & Val(Format(Text5.Text, "")) & "', '" & Format(DTPicker4.Value, "MM-dd-yy") & "', '" & Text15.Text & "', '" & Text17.Text & "', '" & Text7.Text & "');"
            con.Execute msql, , adCmdText
        
      '  Call save_komisi
        If Label23.Caption = "Kredit" Then
            Call save_lising
        End If

        Call save_PiutBroker
        Call save_status
        Call save_subsidi
        Call cicilanDP
        MsgBox "DATA TERSEBUT TELAH DISIMPAN", , "JAYA MOTOR"
        Command1_Click
    Else
        MsgBox "DATA BELUM LENGKAP !", , "JAYA MOTOR"
    End If
End Sub

Private Sub DataGrid1_dblClick()
    Text3.Text = RTrim(Adodc1.Recordset!No_mesin)
    Text17.Text = RTrim(Adodc1.Recordset!no_rangka)
    Call cekNosin
    Frame5.Visible = False
    Text4.SetFocus
End Sub

Private Sub DataGrid2_DblClick()
    Text15.Text = RTrim(Adodc2.Recordset!kd_alamat)
    Frame7.Visible = False
    Text15.SetFocus
    SendKeys "{End}"
End Sub

Private Sub DTPicker2_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Text13.Enabled = True
        Text13.SetFocus
    End If
End Sub

Private Sub Form_Activate()
    Text16.SetFocus
End Sub

Private Sub Form_Load()
    Set con = New ADODB.Connection
    con.Open "Softtech"
    Label21.Caption = Date

    If frmLogin.Combo1.Text = "USER" Then
        Command6.Enabled = False
    Else
        Command6.Enabled = True
    End If
    Command6.Enabled = False
    
    'Call buat_baru
    'Call load_nomor
    Top = 0
    Left = 0
    Text19.Text = ""
    Text19.Visible = False
    DTPicker1.Value = Date
    Text1.Text = ""
    Text18.Text = ""
    Text1.Locked = True
    Text2.Text = ""
    Text3.Text = ""
    Label24.Caption = "Sudah"
    Text4.Text = ""
    Text5.Text = "0"
    Text6.Text = ""
    Text7.Text = ""
    Text8.Text = ""
    Text9.Text = ""
    Text20.Text = ""
    Label45.Caption = ""
    Text15.Text = ""
    Text16.Text = ""
    Text17.Text = ""
    DTPicker4.Value = Date
    Text10.Text = ""
    Text11.Text = ""
    Label35.Caption = ""
    Text13.Text = ""
    Text14.Text = ""
    Label12.Caption = ""
    Label13.Caption = ""
    Label16.Caption = ""
    Label19.Caption = ""
    DTPicker2.Value = Date
    DTPicker3.Value = Date
    Label23.Caption = ""
    Label24.Caption = ""
    
    Combo1.Clear
    Combo1.AddItem "Cash"
    Combo1.AddItem "Kredit"
    
    Frame1.Enabled = False
    DTPicker2.Enabled = False
    Text7.Enabled = False
    Frame3.Visible = False
    Command3.Enabled = False
    
    Frame5.Visible = False
    Frame7.Visible = False
End Sub

Sub buat_baru()
    Dim msql As String
    
    msql = "select * from TNomor where tanggal='" & Label21.Caption & "'"
    Set rs = con.Execute(msql)
       
    If rs.EOF Then
        msql = "Insert Into TNomor " _
               & "([Nomor],[Tanggal]) " _
                   & "VALUES ('" & Val("0") & "', '" & Label21.Caption & "');"
            con.Execute msql, , adCmdText
    End If
  
End Sub

Private Sub Form_Unload(Cancel As Integer)
    con.Close
    Set con = Nothing
End Sub

Private Sub Option1_Click()
    Text7.Enabled = True
    Text7.SetFocus
    Label23.Caption = "Cash"
End Sub

Private Sub Option2_Click()
    Frame1.Enabled = True
    Text6.Enabled = True
    Text6.SetFocus
    Label23.Caption = "Kredit"
End Sub

Private Sub Option3_Click()
'    Text9.Enabled = True
  '  Text9.SetFocus
   
    'Text13.Enabled = True
    'Text13.SetFocus
End Sub

Private Sub Option4_Click()
    DTPicker2.Enabled = True
    Label24.Caption = "Belum"
End Sub

Private Sub Text1_Click()
    If Text1.Locked = True Then
        MsgBox "Tekan enter setelah mengisi nomor transaksi", vbCritical, "JAYA MOTOR"
        Text16.SetFocus
        SendKeys "{End}"
    End If
End Sub

Private Sub Text1_GotFocus()
   If Text18.Text = "" Then
        MsgBox "Wilayah pengambilan belum dimasukkan", vbCritical
        Text18.SetFocus
    End If
End Sub

Private Sub Text1_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text1.Text <> "" Then
            Text15.Enabled = True
            Text15.SetFocus
        End If
    End If
End Sub

Private Sub Text10_Change()
    Text10.Text = Format(Text10.Text, "###,###")
    SendKeys "{End}"
    If Combo1.Text = "Cash" Then
        batas = Val(Format(Label13.Caption, "")) - Val(Format(Text13.Text, ""))
    ElseIf Combo1.Text = "Kredit" Then
        batas = Val(Format(Text9.Text, "")) - Val(Format(Text13.Text, ""))
    End If
    If Text9.Text <> "" Then
        If Val(Format(Text10.Text, "")) > Val(batas) Then
            If Label42.Caption = "cek" Then
                MsgBox "PEMBAYARAN MELEBIHI BATAS TAGIHAN", , "JAYA MOTOR"
                Text10.Text = Format(batas, "###,###")
                Text10.SetFocus
                SendKeys "{end}"
            End If
        End If
    End If
End Sub
Private Sub Text10_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text10_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text10.Text <> "" And Text1.Text <> "" Then
            Command2.Enabled = True
            Command2.SetFocus
        End If
    End If
End Sub

Private Sub Text11_Change()
    If Text11.Text <> "0" Then
        Text11.Text = Format(Text11.Text, "###,###")
        SendKeys "{End}"
    End If
    Label35.Caption = Val(Format(Text13.Text, "")) - Val(Format(Text14.Text, "")) - Val(Format(Text11.Text, ""))
    If Val(Label35.Caption) < 0 Then
        Text11.Text = Format(Val(Format(Text13.Text, "")) - Val(Format(Text14.Text, "")), "###,###")
    End If
    Label35.Caption = Format(Label35.Caption, "###,###")
End Sub

Private Sub Text11_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        'If Text11.Text <> "" And Combo1.Text <> "Cash" Then
            Text9.Enabled = True
            Text9.SetFocus
        'Else
         '   Command2.Enabled = True
         '   Command2.SetFocus
        'End If
    End If
End Sub
Private Sub Text11_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text12_Change()
    Label35.Caption = Format(Label35.Caption, "###,###")
    SendKeys "{End}"
End Sub
Private Sub Text12_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text13_Change()
    If Text13.Text <> "0" Then
        Text13.Text = Format(Text13.Text, "###,###")
        SendKeys "{End}"
    End If
End Sub

Private Sub Text13_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text13.Text <> "" Then
            Text14.Enabled = True
            Text14.SetFocus
        End If
    End If
End Sub
Private Sub Text13_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text14_Change()
    If Text14.Text <> "0" Then
        Text14.Text = Format(Text14.Text, "###,###")
        SendKeys "{End}"
    End If
    If Val(Format(Text14.Text, "")) > Val(Format(Text13.Text, "")) Then
        Text14.Text = Text13.Text
    End If
End Sub

Private Sub Text14_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text14.Text <> "" Then
            Text11.Enabled = True
            Text11.SetFocus
        End If
    End If
End Sub
Private Sub Text14_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text15_KeyDown(KeyCode As Integer, Shift As Integer)
    Frame7.Visible = True
    Adodc2.RecordSource = "select * from TAlamat where kd_alamat LIKE '" & Text15.Text & "%" & "' ORDER by kd_alamat"
    Adodc2.Refresh
    If KeyCode = 13 Then
        If Text15.Text <> "" Then
            Text20.SetFocus
            Frame7.Visible = False
        End If
    End If
End Sub

Private Sub Text16_Change()
    Label24.Caption = "Sudah"
    DTPicker2.Value = DTPicker1.Value
    DTPicker2.Enabled = False
End Sub

Sub untensifnya()
    Dim msql As String
    msql = "select * from TIntensif where no_mesin='" & Text3.Text & "' and kd_broker='" & Text7.Text & "'"
        
    Set rs = con.Execute(msql)
    With rs
        If Not rs.EOF Then
            Text8.Text = Format(!Komisi, "###,###")
        End If
    End With
End Sub
Sub brokker()
    Dim msql As String
    msql = "select * from TBroker where kd_broker='" & Text7.Text & "'"
        
    Set rs = con.Execute(msql)
        
    If Not rs.EOF Then
        Text7.Text = RTrim(rs.Fields("kd_broker"))
        Label19.Caption = RTrim(rs.Fields("Nama_broker"))
        Text8.Enabled = True
    End If
End Sub

Sub subsisdi()
    Dim msql As String
    msql = "select * from TSubsidi where nota='" & Text16.Text & "'"
        
    Set rs = con.Execute(msql)
    With rs
        If Not .EOF Then
            Text13.Text = !Total_subsidi
            Text14.Text = !Dealer
            Text11.Text = !MainDealer
            Label35.Caption = Format(!lising, "###,###")
        End If
    End With
End Sub

Sub leasings()
    Dim msql As String
    msql = "select * from TInformasi_01 where nota='" & Text16.Text & "'"
        
    Set rs = con.Execute(msql)
    With rs
        If Not rs.EOF Then
            Text18.Text = RTrim(!Wilayah)
            Text6.Text = RTrim(!kd_lising)
            Text10.Text = !DP
            If Text6.Text = "JM" Then
                Combo1.Text = "Cash"
            Else
                Combo1.Text = "Kredit"
            End If
            Call kodenya
        End If
    End With
End Sub

Sub kodenya()
    Dim msql As String
    msql = "select * from TLising where kd_lising='" & Text6.Text & "'"
        
    Set rs = con.Execute(msql)
        
    If Not rs.EOF Then
        Text6.Text = RTrim(rs.Fields("kd_lising"))
        Label16.Caption = RTrim(rs.Fields("Nama_lising"))
        Text7.Enabled = True
    End If
End Sub
Sub types()
    Dim msql As String
    msql = "select * from TType where kd_type='" & Text2.Text & "'"
        
    Set rs = con.Execute(msql)
    With rs
        If Not rs.EOF Then
            Text2.Text = RTrim(rs.Fields("kd_type"))
            Label12.Caption = RTrim(rs.Fields("Nama_type"))
            Label13.Caption = Format(rs.Fields("OTR"), "###,###")
            Combo1.Enabled = True
          '  Combo1.SetFocus
        End If
    End With
End Sub

Private Sub Text16_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text16.Text <> "" Then
            msql = "select * from TPenjualan where Nota='" & Text16.Text & "'"
        
            Set rs = con.Execute(msql)
            Call baruss
            
            With rs
                If Not .EOF Then
                    PESA = MsgBox("Nomor NOTA tersebut telah terisi, anda ingin menampilkan data terebut data tersebut", vbYesNo + vbDefaultButton2 + vbExclamation, "JAYA MOTOR")
                    If PESA = vbYes Then
                      '  If RTrim(!Tanggal_PO) <>   Then
               '         If RTrim(!subsidi) = "Ya" Then
                            Text16.Text = RTrim(!Nota)
                            DTPicker1.Value = Format(!Tanggal, "dd-MM-yy")
                            Text1.Text = RTrim(!nama_pemohon)
                            Label23.Caption = RTrim(!sistem_bayar)
                            Label13.Caption = Format(!Harga_dasar, "###,###")
                            Text3.Text = RTrim(!No_mesin)
                            Text9.Text = RTrim(!DP)
                            Text10.Text = RTrim(!bayarDP)
                            Text4.Text = RTrim(!Warna)
                            DTPicker3.Value = Format(!Tgl_bayar, "dd-MM-yy")
                            Text2.Text = RTrim(!Kd_type)
                            Text5.Text = RTrim(!Disc)
                            DTPicker4.Value = Format(!Tgl_Janjian, "dd-MM-yy")
                            Text15.Text = RTrim(!Alamat)
                            Text17.Text = RTrim(!no_rangka)
                            Text7.Text = RTrim(!kd_Broker)
                            Text7.Enabled = True
                            Command2.Enabled = False
                            Command6.Enabled = True
                            Call types
                            Call leasings
                            Call brokker
                            Call subsisdi
                            Call untensifnya
                            Label42.Caption = "ucha"
                            Call cekPemutihan
                       ' Else
                        '    MsgBox "Segera Laporkan No. Transaksi ini", vbCritical, "JAYA MOTOR"
                         '   Command1_Click
                       ' End If
                '        Else
                 '           MsgBox "Nota tersebut Pada Transaksi Non Subsidi", vbCritical, "JAYA MOTOR"
                  '          Text16.SetFocus
                   '         Text1.Locked = True
                    '        SendKeys "{Home}+{End}"
                     '   End If
                    Else
                        Text16.SetFocus
                        Text1.Locked = True
                        SendKeys "{Home}+{End}"
                    End If
                Else
                    Text1.Locked = False
                    Text18.SetFocus
                    Label24.Caption = "Sudah"
                    DTPicker2.Value = DTPicker1.Value
                    DTPicker2.Enabled = False
                    Command6.Enabled = False
                End If
            End With
            Frame5.Visible = False
            Frame7.Visible = False
        End If
    End If

End Sub

Sub cekPemutihan()
    Dim msql As String
    msql = "select * from TInformasi_01 where no_mesin='" & Text3.Text & "'"
    
    Set rs = con.Execute(msql)
    
    With rs
        If Not .EOF Then
            If Right(RTrim(!Tanggal_PO), 5) = "PUTIH" Then
                MsgBox "Segera Laporkan Transaksi ini", vbCritical, "JAYA MOTOR"
                Text19.Visible = True
                Text19.Text = ""
                Text19.SetFocus
            End If
        End If
    End With
End Sub
Private Sub Text17_GotFocus()
    Dim msql As String
    msql = "select * from TPenjualan where no_mesin='" & Text3.Text & "'"
    
    Set rs = con.Execute(msql)
    
    If Not rs.EOF Then
        MsgBox "NOMOR MESIN TERSEBUT SUDAH ADA YANG MEMILIKI", , "JAYA MOTOR"
        Text3.Enabled = True
        Text3.SetFocus
        SendKeys "{end}"
    Else
        Call cekNosin
    End If
End Sub

Private Sub Text17_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text17.Text <> "" Then
        msql = "select * from TPenjualan where no_rangka='" & Text17.Text & "'"
        
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
            MsgBox "NOMOR RANGKA TERSEBUT SUDAH ADA YANG MEMILIKI", , "JAYA MOTOR"
            Text17.Enabled = True
            Text17.SetFocus
            SendKeys "{Home}+{end}"
        Else
            Text4.Enabled = True
            Text4.SetFocus
        End If
        End If
    End If
End Sub

Private Sub Text18_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text18.Text <> "" Then
            Text1.SetFocus
        End If
    End If
End Sub

Private Sub Text19_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Dim msql As String
        msql = "select * from TLogin where nama='" & frmLogin.Text1.Text & "' and status='Owner' and pass='" & Text19.Text & "'"
        
        Set rs = con.Execute(msql)
        
        With rs
            If .EOF Then
                Command1_Click
            Else
                Text19.Visible = False
            End If
        End With
    End If
End Sub

Private Sub Text2_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text2.Text <> "" Then
        msql = "select * from TType where kd_type='" & Text2.Text & "'"
        
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
          '  If rs.Fields("stok_sisa") <= 0 Then
          '      MsgBox "PERSEDIAN STOK MOTOR TIDAK MENCUKUPI/KOSONG", , "JAYA MOTOR"
          '      Text2.SetFocus
          '      SendKeys "{Home}+{End}"
          '  Else
                Text2.Text = RTrim(rs.Fields("kd_type"))
                Label12.Caption = RTrim(rs.Fields("Nama_type"))
                Label13.Caption = Format(rs.Fields("OTR"), "###,###")
                Text3.Text = RTrim(rs.Fields("Ket_nomesin")) + "-"
'                Text17.Text = RTrim(rs.Fields("Ket_norangka")) + "-"
                Combo1.Enabled = True
                Combo1.SetFocus
                Frame5.Visible = False
                Frame7.Visible = False
           ' End If
        Else
            MsgBox "KODE TERSEBUT TIDAK TERDAFTAR", , "JAYA MOTOR"
            Text2.Text = ""
            Label12.Caption = ""
            Label13.Caption = ""
            Text2.Enabled = True
            Text2.SetFocus
            SendKeys "{Home}+{end}"
        End If
        rs.Close
        End If
    End If
End Sub

Private Sub Text20_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text20.Text <> "" Then
            Text3.SetFocus
        End If
    End If
End Sub

Private Sub Text3_Change()
    If Text3.Text <> "" Then
        Frame5.Visible = True
        Adodc1.RecordSource = "select * from TNoSIN where No_mesin LIKE '" & Text3.Text & "%" & "' and stok >0 ORDER by No_mesin"
        Adodc1.Refresh
    End If
End Sub

Private Sub Text3_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text3.Text <> "" Then
            msql = "select * from TPenjualan where no_mesin='" & Text3.Text & "'"
            
            Set rs = con.Execute(msql)
            
            If Not rs.EOF Then
                MsgBox "NOMOR MESIN TERSEBUT SUDAH ADA YANG MEMILIKI", , "JAYA MOTOR"
                Text3.Enabled = True
                Text3.SetFocus
                SendKeys "{end}"
            Else
                Call cekNosin
            End If
            Frame5.Visible = False
        End If
    End If
End Sub
Sub cekNosin2()
    Dim msql As String
    msql = "select * from TType where Ket_Nomesin= '" & Left(Text3.Text, 5) & "'"
    
    Set rs = con.Execute(msql)
    
    With rs
        If Not .EOF Then
         '   Text2.Text = !Kd_type
          '  Label12.Caption = !Nama_type
            Label13.Caption = Format(!OTR, "###,###")
            SendKeys "{End}"
        Else
            MsgBox "Nomor Mesin belum ada harganya", , "JAYA MOTOR"
          '  Text3.SetFocus
      '      SendKeys "{Home}+{End}"
        End If
    End With
End Sub

Sub cekNosin()
    Dim msql As String
    msql = "select * from TNoSIN where no_mesin='" & Text3.Text & "'"
    
    Set rs = con.Execute(msql)
    
    With rs
        If Not .EOF Then
            Text17.Text = !no_rangka
            Text2.Text = !Kd_type
            'Text2.Text = !TNoSIN.Kd_type
           ' Label12.Caption = !Nama_type
         '   Label13.Caption = Format(!OTR, "###,###")
            Text4.Text = RTrim(!Warna)
            Call cekNosin2
            Text4.SetFocus
            SendKeys "{End}"
        Else
            MsgBox "Nomor Mesin belum terdaftar", , "JAYA MOTOR"
            Text3.SetFocus
            SendKeys "{Home}+{End}"
        End If
    End With
End Sub

Private Sub Text4_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text4.Text <> "" Then
            Combo1.SetFocus
        End If
    End If
End Sub

Private Sub Text5_Change()
    If Text5.Text <> "" Then
        Text5.Text = Format(Text5.Text, "###,###")
        SendKeys "{End}"
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

Private Sub Text5_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text5.Text = "" Then
            Text5.Text = "0"
        End If
        If Combo1.Text = "Cash" Then
            Text9.Text = Format(Label13.Caption, "###,###")
            Text10.Enabled = True
            Text10.SetFocus
            Text13.Text = ""
            Text11.Text = ""
            Text12.Text = ""
            Text14.Text = ""
        Else
            Text13.SetFocus
        End If
    End If
End Sub

Private Sub Text6_GotFocus()
    SendKeys "{Home}+{End}"
End Sub

Private Sub Text6_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        msql = "select * from TLising where kd_lising='" & Text6.Text & "'"
        
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
            Text6.Text = RTrim(rs.Fields("kd_lising"))
            Label16.Caption = RTrim(rs.Fields("Nama_lising"))
            Text7.Enabled = True
            Text7.SetFocus
        Else
            MsgBox "KODE TERSEBUT TIDAK TERDAFTAR", , "JAYA MOTOR"
            Text6.Enabled = True
            Text6.SetFocus
            SendKeys "{Home}+{End}"
            Label16.Caption = ""
        End If
        rs.Close
    End If
End Sub

Private Sub Text7_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        msql = "select * from TBroker where kd_broker='" & Text7.Text & "'"
        
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
            Text7.Text = RTrim(rs.Fields("kd_broker"))
            Label19.Caption = RTrim(rs.Fields("Nama_broker"))
            Text5.SetFocus
            SendKeys "{End}"
        Else
            MsgBox "KODE TERSEBUT TIDAK TERDAFTAR", , "JAYA MOTOR"
            Text7.Enabled = True
            Text7.SetFocus
            SendKeys "{Home}+{End}"
            Label19.Caption = ""
        End If
        rs.Close
      End If
End Sub

Private Sub Text8_Change()
    Text8.Text = Format(Text8.Text, "###,###")
    SendKeys "{End}"
End Sub

Private Sub Text8_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Text3.Enabled = True
        Text3.SetFocus
        SendKeys "{End}"
        If Text8.Text = "" Then
            Text8.Text = "0"
        End If
    End If
End Sub
Private Sub Text8_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text9_Change()
    On Error Resume Next
    Text9.Text = Format(Text9.Text, "###,###")
    SendKeys "{End}"
    If Combo1.Text = "Cash" Then
        Text9.Text = Label13.Caption
        'Text10.Text = Text9.Text
    End If
    batasS = Val(Format(Label13.Caption, "")) ' - (Val(Format(Text5.Text, "")) + Val(Format(Text13.Text, "")))
    If Val(batasS) < Val(Format(Text9.Text, "")) Then
        MsgBox "NILAI UANG MUKA MELEWATI BATAS", , "JAYA MOTOR"
        Text9.SetFocus
        SendKeys "{Home}+{End}"
    End If
End Sub

Private Sub Text9_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text9.Text <> "" Then
            Text10.Enabled = True
            Text10.SetFocus
        End If
    End If
End Sub
Private Sub Text9_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub


