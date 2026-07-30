VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{86CF1D34-0C5F-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCT2.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Object = "{00025600-0000-0000-C000-000000000046}#5.2#0"; "Crystl32.OCX"
Begin VB.Form Form3 
   BackColor       =   &H00EC6962&
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Stok Motor"
   ClientHeight    =   9255
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   8910
   FillColor       =   &H00EC6962&
   ForeColor       =   &H00EC6962&
   Icon            =   "stok.frx":0000
   LinkTopic       =   "Form3"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   9255
   ScaleWidth      =   8910
   ShowInTaskbar   =   0   'False
   Begin VB.ComboBox Combo1 
      Height          =   315
      Left            =   2520
      TabIndex        =   33
      Text            =   "Combo1"
      Top             =   2760
      Width           =   2055
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
      Left            =   2520
      MaxLength       =   15
      TabIndex        =   31
      Text            =   "Text1"
      Top             =   2280
      Width           =   1695
   End
   Begin Crystal.CrystalReport CrystalReport1 
      Left            =   3480
      Top             =   4320
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   348160
      PrintFileLinesPerPage=   60
   End
   Begin VB.TextBox Text6 
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
      Left            =   8040
      Locked          =   -1  'True
      MaxLength       =   15
      TabIndex        =   29
      Text            =   "4"
      Top             =   7440
      Width           =   735
   End
   Begin VB.TextBox Text5 
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
      Left            =   2520
      MaxLength       =   20
      TabIndex        =   27
      Text            =   "4"
      Top             =   1320
      Width           =   2655
   End
   Begin VB.CommandButton Command6 
      BackColor       =   &H00FF8080&
      Height          =   495
      Left            =   6840
      Picture         =   "stok.frx":08CA
      Style           =   1  'Graphical
      TabIndex        =   26
      Top             =   120
      Width           =   495
   End
   Begin MSComCtl2.DTPicker DTPicker1 
      Height          =   375
      Left            =   2520
      TabIndex        =   23
      Top             =   240
      Width           =   1815
      _ExtentX        =   3201
      _ExtentY        =   661
      _Version        =   393216
      Format          =   122290176
      CurrentDate     =   40493
   End
   Begin VB.CommandButton Command10 
      BackColor       =   &H00979B04&
      Caption         =   "Cetak"
      Height          =   1095
      Left            =   4440
      Picture         =   "stok.frx":0D0C
      Style           =   1  'Graphical
      TabIndex        =   21
      ToolTipText     =   "Cetak"
      Top             =   8040
      Visible         =   0   'False
      Width           =   1095
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
      Left            =   2520
      MaxLength       =   20
      TabIndex        =   0
      Text            =   "4"
      Top             =   840
      Width           =   2655
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00979B04&
      Caption         =   "BARU"
      Height          =   1095
      Left            =   360
      Picture         =   "stok.frx":153F
      Style           =   1  'Graphical
      TabIndex        =   19
      Top             =   8040
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Caption         =   "SIMPAN"
      Height          =   1095
      Left            =   1680
      Picture         =   "stok.frx":1BE7
      Style           =   1  'Graphical
      TabIndex        =   18
      Top             =   8040
      Visible         =   0   'False
      Width           =   1095
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00979B04&
      Caption         =   "HAPUS"
      Height          =   1095
      Left            =   3120
      Picture         =   "stok.frx":2475
      Style           =   1  'Graphical
      TabIndex        =   17
      Top             =   8040
      Visible         =   0   'False
      Width           =   1095
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "KELUAR"
      Height          =   1095
      Left            =   7680
      Picture         =   "stok.frx":2BF8
      Style           =   1  'Graphical
      TabIndex        =   16
      Top             =   8040
      Width           =   1095
   End
   Begin MSAdodcLib.Adodc Adodc1 
      Height          =   735
      Left            =   6360
      Top             =   1080
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
      RecordSource    =   "select * from TNoSIN where stok > 0 order by tanggal_datang"
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
   Begin VB.CommandButton Command5 
      BackColor       =   &H00C0C0FF&
      Caption         =   "..."
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   9.75
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   9000
      Style           =   1  'Graphical
      TabIndex        =   14
      Top             =   2160
      Width           =   495
   End
   Begin VB.TextBox Text3 
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
      Left            =   2400
      MaxLength       =   11
      TabIndex        =   13
      Text            =   "Text3"
      Top             =   3990
      Visible         =   0   'False
      Width           =   2655
   End
   Begin VB.TextBox Text2 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00C0C0FF&
      Height          =   375
      Left            =   12600
      MaxLength       =   4
      TabIndex        =   8
      Text            =   "Text2"
      Top             =   2160
      Visible         =   0   'False
      Width           =   1575
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
      Left            =   2520
      MaxLength       =   15
      TabIndex        =   3
      Text            =   "Text1"
      Top             =   1800
      Width           =   2655
   End
   Begin MSDataGridLib.DataGrid DataGrid1 
      Bindings        =   "stok.frx":33A1
      Height          =   3975
      Left            =   120
      TabIndex        =   15
      Top             =   3360
      Width           =   8655
      _ExtentX        =   15266
      _ExtentY        =   7011
      _Version        =   393216
      AllowUpdate     =   0   'False
      BackColor       =   12648447
      ForeColor       =   0
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
      ColumnCount     =   7
      BeginProperty Column00 
         DataField       =   "Tanggal_datang"
         Caption         =   "Tanggal Masuk"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "d. MMM yyyy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   "No_mesin"
         Caption         =   "No. Mesin"
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
         DataField       =   "No_rangka"
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
      BeginProperty Column03 
         DataField       =   "Kd_type"
         Caption         =   "Kode Type"
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
      BeginProperty Column04 
         DataField       =   "Warna"
         Caption         =   "Warna"
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
      BeginProperty Column05 
         DataField       =   "Tgl_pindah"
         Caption         =   "Tanggal Kirim"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd MMM yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column06 
         DataField       =   "Gudang"
         Caption         =   "Dealer"
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
         MarqueeStyle    =   4
         RecordSelectors =   0   'False
         BeginProperty Column00 
            ColumnWidth     =   1184,882
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   1725,165
         EndProperty
         BeginProperty Column02 
            ColumnWidth     =   1590,236
         EndProperty
         BeginProperty Column03 
            ColumnWidth     =   1005,165
         EndProperty
         BeginProperty Column04 
            ColumnWidth     =   854,929
         EndProperty
         BeginProperty Column05 
            ColumnWidth     =   1170,142
         EndProperty
         BeginProperty Column06 
            ColumnWidth     =   1019,906
         EndProperty
      EndProperty
   End
   Begin MSComCtl2.DTPicker DTPicker2 
      Height          =   375
      Left            =   4680
      TabIndex        =   24
      Top             =   240
      Width           =   1815
      _ExtentX        =   3201
      _ExtentY        =   661
      _Version        =   393216
      Format          =   122290176
      CurrentDate     =   40493
   End
   Begin VB.Label Label16 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Dealer"
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
      Left            =   480
      TabIndex        =   32
      Top             =   2850
      Width           =   645
   End
   Begin VB.Label Label15 
      Caption         =   "Label15"
      Height          =   495
      Left            =   6960
      TabIndex        =   30
      Top             =   2040
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label14 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "No. Rangka"
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
      Left            =   480
      TabIndex        =   28
      Top             =   1320
      Width           =   1095
   End
   Begin VB.Label Label13 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "-"
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
      Left            =   4440
      TabIndex        =   25
      Top             =   330
      Visible         =   0   'False
      Width           =   90
   End
   Begin VB.Label Label12 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Tanggal"
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
      Left            =   480
      TabIndex        =   22
      Top             =   240
      Width           =   780
   End
   Begin VB.Label Label11 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "No. Mesin"
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
      Left            =   480
      TabIndex        =   20
      Top             =   840
      Width           =   930
   End
   Begin VB.Label Label10 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00C0C0FF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label10"
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   12600
      TabIndex        =   12
      Top             =   1560
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label9 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00C0C0FF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label9"
      ForeColor       =   &H80000008&
      Height          =   375
      Left            =   12600
      TabIndex        =   11
      Top             =   960
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label8 
      Alignment       =   1  'Right Justify
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label8"
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
      Left            =   3960
      TabIndex        =   10
      Top             =   4680
      Visible         =   0   'False
      Width           =   2655
   End
   Begin VB.Label Label7 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label7"
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
      Left            =   2400
      TabIndex        =   9
      Top             =   3960
      Width           =   4215
   End
   Begin VB.Label Label6 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Stok Masuk"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H000000C0&
      Height          =   195
      Left            =   10560
      TabIndex        =   7
      Top             =   2160
      Visible         =   0   'False
      Width           =   1110
   End
   Begin VB.Label Label5 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Stok Sisa"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H000000C0&
      Height          =   195
      Left            =   10560
      TabIndex        =   6
      Top             =   960
      Visible         =   0   'False
      Width           =   900
   End
   Begin VB.Label Label4 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Stok Awal"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H000000C0&
      Height          =   195
      Left            =   10560
      TabIndex        =   5
      Top             =   1560
      Visible         =   0   'False
      Width           =   960
   End
   Begin VB.Label Label3 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Harga Dasar"
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
      Left            =   360
      TabIndex        =   4
      Top             =   4080
      Visible         =   0   'False
      Width           =   1215
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Warna"
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
      Left            =   480
      TabIndex        =   2
      Top             =   2370
      Width           =   630
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
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   195
      Left            =   480
      TabIndex        =   1
      Top             =   1800
      Width           =   1020
   End
   Begin VB.Image Image1 
      Height          =   14535
      Left            =   -2760
      Picture         =   "stok.frx":33B6
      Stretch         =   -1  'True
      Top             =   -360
      Width           =   20895
   End
End
Attribute VB_Name = "Form3"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim con As ADODB.Connection
Dim rs As ADODB.Recordset

Private Sub Combo1_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Command2.SetFocus
    End If
End Sub

Private Sub Command1_Click()
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text4.Text = ""
    Text5.Text = ""
    Text6.Text = ""
    Text7.Text = ""
    Combo1.Clear
    Combo1.AddItem "JM1"
    Combo1.AddItem "JM2"
    Label7.Caption = ""
    Label8.Caption = ""
    Label9.Caption = ""
    Label10.Caption = ""
    Text3.Visible = False
    Text4.SetFocus
    Call hit_stok
    Call layar
End Sub

Private Sub Command10_Click()
    CrystalReport1.SelectionFormula = "{TNoSIN.tanggal_datang} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') and {TNoSIN.tanggal_datang} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TNoSIN.Stok} > 0"
    CrystalReport1.ReportFileName = App.Path & "\StokMotor.rpt"
    CrystalReport1.RetrieveDataFiles
    CrystalReport1.Destination = crptToWindow
    CrystalReport1.WindowState = crptMaximized
    CrystalReport1.Action = 1
    CrystalReport1.Reset
End Sub

Private Sub Command2_Click()
    Dim msql As String
    If Text4.Text <> "" And Text1.Text <> "" And Text5.Text <> "" Then
        msql = "select * from TNoSIN where no_mesin='" & Text4.Text & "'"
        Set rs = con.Execute(msql)
        
        If Not rs.EOF Then
            msql = "update TNoSIN set " & _
                " kd_type ='" & Text1.Text & "', " & _
                " no_mesin ='" & Text4.Text & "', " & _
                " no_rangka ='" & Text5.Text & "', " & _
                " tanggal_datang ='" & Format(DTPicker1.Value, "MM-dd-yy") & "', " & _
                " warna ='" & Text7.Text & "', " & _
                " Gudang ='" & Combo1.Text & "', " & _
                " tgl_pindah ='" & Format(DTPicker1.Value, "MM-dd-yy") & "', " & _
                " Gudang2 ='" & Combo1.Text & "' " & _
                " where no_mesin='" & Text4.Text & "' and stok > 0"
            con.Execute msql, , adCmdText
        Else
            msql = "Insert Into TNoSIN " _
               & "([No_mesin],[Kd_type],[No_rangka],[Stok],[tanggal_datang],[Warna],[Gudang],[tgl_pindah],[Gudang2]) " _
                   & "VALUES ('" & Text4.Text & "', '" & Text1.Text & "','" & Text5.Text & "','1', '" & Format(DTPicker1.Value, "MM-dd-yy") & "','" & Text7.Text & "', '" & Combo1.Text & "','" & Format(DTPicker1.Value, "MM-dd-yy") & "','" & Combo1.Text & "');"
            con.Execute msql, , adCmdText
        End If
        Command1_Click
    End If
End Sub

Private Sub Command3_Click()
    If Text1.Text <> "" Then
        msql = "select * from TNoSIN where No_mesin='" & Text4.Text & "' and stok > 0"
        Set rs = con.Execute(msql)
    
        If Not rs.EOF Then
            pesan = MsgBox("APAKAH ANDA YAKIN INGIN MENGHAPUS DATA INI ?", vbYesNo, "JAYA MOTOR")
            If pesan = vbYes Then
                msql = "delete from TNoSIN where no_mesin ='" & Text4.Text & "' and stok > 0"
                con.Execute msql, , adCmdText
                MsgBox "DATA TELAH DIHAPUS", , "JAYA MOTOR"
                Command1_Click
            End If
        End If
    End If
End Sub

Private Sub Command4_Click()
    Unload Me
End Sub

Private Sub Command5_Click()
    Text3.Visible = True
    Text3.Text = Label8.Caption
    Text3.SetFocus
    SendKeys "{Home}+{end}"
End Sub

Private Sub Command6_Click()
    Dim msql As String
    msql = "select count(stok) as stoknya from TNoSIN WHERE stok > 0 and tanggal_datang >='" & Format(DTPicker1.Value, "MM-dd-yy") & "' and tanggal_datang <='" & Format(DTPicker2.Value, "MM-dd-yy") & "'"

    Set rs = con.Execute(msql)
    With rs
        If Not .EOF Then
            Text6.Text = !stoknya
        End If
    End With

    Adodc1.RecordSource = "select * from TNoSIN where stok > 0 and tanggal_datang >='" & Format(DTPicker1.Value, "MM-dd-yy") & "' and tanggal_datang <='" & Format(DTPicker2.Value, "MM-dd-yy") & "' order by tanggal_datang"
    Adodc1.Refresh
End Sub

Private Sub DataGrid1_dblClick()
    On Error Resume Next
    Text4.Text = RTrim(Adodc1.Recordset!No_mesin)
    Text1.Text = RTrim(Adodc1.Recordset!Kd_type)
    Text5.Text = RTrim(Adodc1.Recordset!no_rangka)
    Text7.Text = RTrim(Adodc1.Recordset!warna)
    Combo1.Text = RTrim(Adodc1.Recordset!Gudang)
  '  Call look
End Sub

Sub look()
    Dim msql As String
    msql = "select * from TType where kd_type='" & Text1.Text & "'"

    Set rs = con.Execute(msql)

    If Not rs.EOF Then
        Label7.Caption = RTrim(rs.Fields("Nama_type"))
    End If
End Sub

Sub hit_stok()
    Dim msql As String
    msql = "select count(stok) as stoknya from TNoSIN WHERE stok >0"

    Set rs = con.Execute(msql)
    With rs
        If Not .EOF Then
            Text6.Text = !stoknya
        End If
    End With
End Sub

Private Sub Form_Load()
    Set con = New ADODB.Connection
    con.Open "Softtech"
    
    Text1.Text = ""
    Text2.Text = ""
    Text3.Text = ""
    Text4.Text = ""
    Text5.Text = ""
    Text6.Text = ""
    Text7.Text = ""
    
    Label7.Caption = ""
    Label8.Caption = ""
    Label9.Caption = ""
    Label10.Caption = ""
    
    Combo1.Clear
    Combo1.AddItem "JM1"
    Combo1.AddItem "JM2"
    
    DTPicker1.Value = Date
    DTPicker2.Value = Date
    Text3.Visible = False
    Top = 0
    Left = 0
    Call hit_stok
    If frmLogin.Combo1.Text = "Owner" Or frmLogin.Combo1.Text = "Adm 1" Then
        Command2.Visible = True
        Command3.Visible = True
        Command10.Visible = True
    End If
End Sub

Sub layar()
    Dim msql As String
    msql = "select * from TNoSIN where stok > 0 order by tanggal_datang"
    Adodc1.RecordSource = msql
    Adodc1.Refresh
End Sub

Private Sub Form_Unload(Cancel As Integer)
    con.Close
    Set con = Nothing
End Sub

Private Sub Text1_KeyDown(KeyCode As Integer, Shift As Integer)
'1/6/13    Dim msql As String
'1/6/13    If KeyCode = 13 Then
'1/6/13        If Text1.Text <> "" Then
'1/6/13            msql = "select * from TType where kd_type='" & Text1.Text & "'"
        
'1/6/13            Set rs = con.Execute(msql)
        
'1/6/13            If Not rs.EOF Then
'1/6/13                Text1.Text = RTrim(rs.Fields("kd_type"))
'1/6/13                Label7.Caption = RTrim(rs.Fields("Nama_type"))
          '      Label8.Caption = Format(rs.Fields("Harga_dasar"), "###,###")
          '      Label9.Caption = rs.Fields("Stok_sisa")
          '      Label10.Caption = rs.Fields("Stok_awal")
'1/6/13                Text2.Text = ""
'1/6/13                Text2.SetFocus
'1/6/13            Else
'1/6/13                MsgBox "KODE TERSEBUT BELUM TERDAFTAR", , "JAYA MOTOR"
'1/6/13                Text1.SetFocus
'1/6/13                Text2.Text = ""
'1/6/13                Text3.Text = ""
'1/6/13                Label7.Caption = ""
'1/6/13                Label8.Caption = ""
'1/6/13                Label9.Caption = ""
'1/6/13                Label10.Caption = ""
'1/6/13                Text3.Visible = False
'1/6/13                SendKeys "{Home}+{End}"
'1/6/13            End If
'1/6/13        End If
'1/6/13        rs.Close
'1/6/13    End If
    If KeyCode = 13 Then
        If Text1.Text <> "" Then
            Text7.SetFocus
        End If
    End If
End Sub

Private Sub Text2_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Command2.SetFocus
    End If
End Sub

Private Sub Text2_KeyPress(KeyAscii As Integer)
   Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text3_Change()
    Text3.Text = Format(Text3.Text, "###,###")
    SendKeys "{end}"
End Sub

Private Sub Text3_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Text2.SetFocus
    End If
End Sub

Private Sub Text3_KeyPress(KeyAscii As Integer)
    Dim angka As String
    angka = "0123456789"
    
    If KeyAscii > 26 Then
        If InStr(angka, Chr(KeyAscii)) = 0 Then
            KeyAscii = 0
        End If
    End If
End Sub

Private Sub Text4_Change()
    If Text4.Text <> "" Then
        Dim msql As String
        msql = "select count(stok) as stoknya from TNoSIN where No_mesin LIKE '" & Text4.Text & "%" & "' and stok > 0"

        Set rs = con.Execute(msql)
        With rs
            If Not .EOF Then
                Text6.Text = !stoknya
            End If
        End With
        Adodc1.RecordSource = "select * from TNoSIN where No_mesin LIKE '" & Text4.Text & "%" & "' and stok > 0 order by tanggal_datang"
        Adodc1.Refresh
    End If
End Sub

Private Sub Text4_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text4.Text <> "" Then
            Dim msql As String
            Dim msql1 As String
            
            msql = "select * from TNoSIN where no_mesin='" & Text4.Text & "'"
            Set rs = con.Execute(msql)
            
            With rs
                If Not .EOF Then
                    Text1.Text = RTrim(!Kd_type)
                    Text4.Text = RTrim(!No_mesin)
                    Text5.Text = RTrim(!no_rangka)
                    Label15.Caption = "tidak"
                Else
                    Text5.Text = ""
                    Text5.SetFocus
                End If
            End With
        End If
    End If
End Sub

Sub cekNorangka()
    NoRang = Left(Text5.Text, 7)
    msql1 = "select * from TType where ket_norangka = '" & NoRang & "'"
    
    Set rs = con.Execute(msql1)
    
    With rs
        If Not .EOF Then
            Text1.Text = RTrim(!Kd_type)
            Label7.Caption = RTrim(!Nama_type)
            Label15.Caption = "ya"
            If Text4.Text = "" Then
                Text4.SetFocus
            Else
                Command2_Click
            End If
        End If
    End With
End Sub

Sub cekNosin()
'1/6/13    NoSIN = Left(Text4.Text, 5)
'1/6/13    msql1 = "select * from TType where ket_noMesin = '" & NoSIN & "'"
    
    msql1 = "select * from TType where kd_type = '" & Text1.Text & "'"
    Set rs = con.Execute(msql1)
    
    With rs
        If Not .EOF Then
            Label7.Caption = RTrim(!Nama_type)
            Label15.Caption = "ya"
            If Text5.Text = "" Then
                Text5.SetFocus
            Else
                Command2_Click
            End If
        Else
            Text4.Text = ""
        End If
    End With

End Sub

Private Sub Text5_KeyDown(KeyCode As Integer, Shift As Integer)
    If Text5.Text <> "" Then
        If KeyCode = 13 Then
            Dim msql As String
            Dim msql1 As String
            
            msql = "select * from TNoSIN where no_rangka='" & Text5.Text & "'"
            Set rs = con.Execute(msql)
            
            With rs
                If Not .EOF Then
                    MsgBox "No. rangka sudah terpakai", , "Jaya Motor"
                    Text1.Text = RTrim(!Kd_type)
                    Text4.Text = RTrim(!No_mesin)
                    Text5.Text = RTrim(!no_rangka)
                    Label15.Caption = "tidak"
                Else
                    Text1.Text = ""
                    Text1.SetFocus
                End If
            End With
        End If
    End If
End Sub

Sub loadAuto()
    Dim msql As String
    msql = "select * from TTempImport"
    Set rs = con.Execute(msql)
    
    With rs
        If Not .EOF Then
            Do Until .EOF
                Text4.Text = RTrim(!No_mesin)
                Text5.Text = RTrim(!no_rangka)
                Text7.Text = RTrim(!warna)
                Combo1.Text = RTrim(!Gudang)
                Text1.Text = RTrim(!Kd_type)
               ' Call cekNosin
                Command2_Click
                .MoveNext
            Loop
        End If
    End With
End Sub

Private Sub Text7_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text7.Text <> "" Then
            Combo1.SetFocus
        End If
    End If
End Sub
