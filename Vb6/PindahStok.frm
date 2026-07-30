VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{86CF1D34-0C5F-11D2-A9FC-0000F8754DA1}#2.0#0"; "MSCOMCT2.OCX"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Object = "{00025600-0000-0000-C000-000000000046}#5.2#0"; "Crystl32.OCX"
Begin VB.Form Form3a 
   BackColor       =   &H00EC6962&
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "PEMINDAHAN STOK"
   ClientHeight    =   9435
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   9795
   FillColor       =   &H00EC6962&
   ForeColor       =   &H00EC6962&
   Icon            =   "PindahStok.frx":0000
   LinkTopic       =   "Form3"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   9435
   ScaleWidth      =   9795
   ShowInTaskbar   =   0   'False
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
      Left            =   2520
      MaxLength       =   10
      TabIndex        =   34
      Text            =   "4"
      Top             =   3240
      Width           =   1815
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
      Left            =   5520
      MaxLength       =   10
      TabIndex        =   33
      Text            =   "4"
      Top             =   2760
      Width           =   1815
   End
   Begin VB.CommandButton Command6 
      BackColor       =   &H00979B04&
      Caption         =   "Stok Kembali"
      Height          =   495
      Left            =   7680
      Style           =   1  'Graphical
      TabIndex        =   31
      Top             =   2700
      Width           =   1575
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
      Left            =   7680
      Locked          =   -1  'True
      MaxLength       =   15
      TabIndex        =   23
      Text            =   "4"
      Top             =   8040
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
      TabIndex        =   21
      Text            =   "4"
      Top             =   1320
      Width           =   2655
   End
   Begin MSComCtl2.DTPicker DTPicker1 
      Height          =   375
      Left            =   2520
      TabIndex        =   20
      Top             =   240
      Width           =   1815
      _ExtentX        =   3201
      _ExtentY        =   661
      _Version        =   393216
      Format          =   53346304
      CurrentDate     =   40493
   End
   Begin VB.CommandButton Command10 
      BackColor       =   &H00979B04&
      Caption         =   "Cetak"
      Height          =   1095
      Left            =   4320
      Picture         =   "PindahStok.frx":08CA
      Style           =   1  'Graphical
      TabIndex        =   18
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
      Picture         =   "PindahStok.frx":10FD
      Style           =   1  'Graphical
      TabIndex        =   16
      Top             =   8040
      Width           =   1095
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Caption         =   "PINDAH"
      Height          =   1095
      Left            =   1560
      Picture         =   "PindahStok.frx":17A5
      Style           =   1  'Graphical
      TabIndex        =   15
      Top             =   8040
      Visible         =   0   'False
      Width           =   1095
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00979B04&
      Caption         =   "HAPUS"
      Height          =   1095
      Left            =   3120
      Picture         =   "PindahStok.frx":2033
      Style           =   1  'Graphical
      TabIndex        =   14
      Top             =   8040
      Visible         =   0   'False
      Width           =   1095
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "KELUAR"
      Height          =   1095
      Left            =   8520
      Picture         =   "PindahStok.frx":27B6
      Style           =   1  'Graphical
      TabIndex        =   13
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
      TabIndex        =   12
      Top             =   2160
      Visible         =   0   'False
      Width           =   495
   End
   Begin VB.TextBox Text2 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00C0C0FF&
      Height          =   375
      Left            =   12600
      MaxLength       =   4
      TabIndex        =   7
      Text            =   "Text2"
      Top             =   2160
      Visible         =   0   'False
      Width           =   1575
   End
   Begin MSDataGridLib.DataGrid DataGrid1 
      Bindings        =   "PindahStok.frx":2F5F
      Height          =   4095
      Left            =   120
      TabIndex        =   32
      Top             =   3720
      Width           =   9495
      _ExtentX        =   16748
      _ExtentY        =   7223
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
      ColumnCount     =   9
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
      BeginProperty Column02 
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
      BeginProperty Column03 
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
      BeginProperty Column04 
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
      BeginProperty Column05 
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
      BeginProperty Column06 
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
      BeginProperty Column07 
         DataField       =   "Gudang2"
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
      BeginProperty Column08 
         DataField       =   "driver"
         Caption         =   "Driver"
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
            ColumnWidth     =   1049,953
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   1019,906
         EndProperty
         BeginProperty Column02 
            ColumnWidth     =   1275,024
         EndProperty
         BeginProperty Column03 
            ColumnWidth     =   1379,906
         EndProperty
         BeginProperty Column04 
            ColumnWidth     =   1005,165
         EndProperty
         BeginProperty Column05 
            ColumnWidth     =   854,929
         EndProperty
         BeginProperty Column06 
            ColumnWidth     =   1170,142
         EndProperty
         BeginProperty Column07 
            ColumnWidth     =   1019,906
         EndProperty
         BeginProperty Column08 
            ColumnWidth     =   1395,213
         EndProperty
      EndProperty
   End
   Begin VB.Label Label21 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Driver"
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
      TabIndex        =   35
      Top             =   3360
      Width           =   615
   End
   Begin VB.Label Label20 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "20"
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
      Left            =   5880
      TabIndex        =   30
      Top             =   4200
      Width           =   1215
   End
   Begin VB.Label Label18 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "18"
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
      Left            =   2520
      TabIndex        =   29
      Top             =   2760
      Width           =   1215
   End
   Begin VB.Label Label17 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "17"
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
      Left            =   2520
      TabIndex        =   28
      Top             =   2280
      Width           =   1695
   End
   Begin VB.Label Label19 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "19"
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
      Left            =   2520
      TabIndex        =   27
      Top             =   1800
      Width           =   3135
   End
   Begin VB.Label Label13 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "--Link->>>"
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
      Left            =   4320
      TabIndex        =   26
      Top             =   2880
      Width           =   1080
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
      TabIndex        =   25
      Top             =   2850
      Width           =   645
   End
   Begin VB.Label Label15 
      Caption         =   "Label15"
      Height          =   495
      Left            =   6960
      TabIndex        =   24
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
      TabIndex        =   22
      Top             =   1410
      Width           =   1095
   End
   Begin VB.Label Label12 
      AutoSize        =   -1  'True
      BackColor       =   &H00C0C0FF&
      BackStyle       =   0  'Transparent
      Caption         =   "Tanggal Kirim"
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
      TabIndex        =   19
      Top             =   330
      Width           =   1350
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
      TabIndex        =   17
      Top             =   930
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
      TabIndex        =   11
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
      TabIndex        =   10
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
      TabIndex        =   9
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
      TabIndex        =   8
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
      TabIndex        =   6
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
      TabIndex        =   5
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
      TabIndex        =   4
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
      TabIndex        =   3
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
      Top             =   1890
      Width           =   1020
   End
   Begin VB.Image Image1 
      Height          =   14535
      Left            =   -2760
      Picture         =   "PindahStok.frx":2F74
      Stretch         =   -1  'True
      Top             =   -360
      Width           =   20895
   End
End
Attribute VB_Name = "Form3a"
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
    Label7.Caption = ""
    Label8.Caption = ""
    Label9.Caption = ""
    Label10.Caption = ""
    Label17.Caption = ""
    Label18.Caption = ""
    Label19.Caption = ""
    Label20.Caption = ""
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
        
        With rs
            If Not .EOF Then
                If RTrim(!Gudang) = RTrim(!Gudang2) Then
                    msql = "update TNoSIN set " & _
                        " tgl_pindah ='" & Format(DTPicker1.Value, "MM-dd-yy") & "', " & _
                        " Gudang2 ='" & Text1.Text & "', " & _
                        " Driver ='" & Text3.Text & "' " & _
                        " where no_mesin='" & Text4.Text & "' and stok > 0"
                    con.Execute msql, , adCmdText
                End If
            End If
        End With
        Adodc1.Refresh
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
    If Text4.Text <> "" And Text5.Text <> "" Then
        msql = "select * from TNoSIN where no_mesin='" & Text4.Text & "'"
        Set rs = con.Execute(msql)
        
        With rs
            If Not .EOF Then
                pesan = MsgBox("APAKAH ANDA YAKIN INGIN MENGEMBALIKAN STOK MOTOR TERSEBUT ?", vbYesNo, "JAYA MOTOR")
                If pesan = vbYes Then
                    If RTrim(!Gudang) <> RTrim(!Gudang2) Then
                        msql = "update TNoSIN set " & _
                            " tgl_pindah =tanggal_datang, " & _
                            " Gudang2 ='" & Label18.Caption & "', " & _
                            " Driver ='' " & _
                            " where no_mesin='" & Text4.Text & "' and stok > 0"
                        con.Execute msql, , adCmdText
                    End If
                End If
            End If
        End With
        Command1_Click
    End If
End Sub

Private Sub DataGrid1_dblClick()
    On Error Resume Next
    Text4.Text = RTrim(Adodc1.Recordset!No_mesin)
    Label19.Caption = RTrim(Adodc1.Recordset!Kd_type)
    Text5.Text = RTrim(Adodc1.Recordset!no_rangka)
    Label17.Caption = RTrim(Adodc1.Recordset!Warna)
    Label18.Caption = RTrim(Adodc1.Recordset!Gudang)
    Call look
    Text1.SetFocus
End Sub

Sub look()
    Dim msql As String
    msql = "select * from TType where kd_type='" & Label19.Caption & "'"

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
    Text4.Text = ""
    Text3.Text = ""
    Text5.Text = ""
    Text6.Text = ""
    
    Label7.Caption = ""
    Label8.Caption = ""
    Label9.Caption = ""
    Label10.Caption = ""
    Label17.Caption = ""
    Label18.Caption = ""
    Label19.Caption = ""
    Label20.Caption = ""
    
    DTPicker1.Value = Date
    Top = 0
    Left = 0
    Call hit_stok
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
    Dim msql As String
    If KeyCode = 13 Then
        If Text1.Text <> "" Then
            msql = "select * from TBroker where kd_broker='" & Text1.Text & "'"
        
            Set rs = con.Execute(msql)
        
            If Not rs.EOF Then
                Text3.SetFocus
            Else
                MsgBox "KODE TERSEBUT BELUM TERDAFTAR", , "JAYA MOTOR"
            End If
        End If
        rs.Close
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



Private Sub Text3_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        Command2_Click
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
                    Label19.Caption = RTrim(!Kd_type)
                    Label17.Caption = RTrim(!Warna)
                    Label18.Caption = RTrim(!Gudang)
                    Text4.Text = RTrim(!No_mesin)
                    Text5.Text = RTrim(!no_rangka)
                Else
                    MsgBox "Data salah"
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
    NoSIN = Left(Text4.Text, 5)
    msql1 = "select * from TType where ket_noMesin = '" & NoSIN & "'"
    
    Set rs = con.Execute(msql1)
    
    With rs
        If Not .EOF Then
            Text1.Text = RTrim(!Kd_type)
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
                    Label19.Caption = RTrim(!Kd_type)
                    Label17.Caption = RTrim(!Warna)
                    Label18.Caption = RTrim(!Gudang)
                    Text4.Text = RTrim(!No_mesin)
                    Text5.Text = RTrim(!no_rangka)
                Else
                    MsgBox "Data salah"
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
                Text7.Text = RTrim(!Warna)
                Combo1.Text = RTrim(!Gudang)
                Call cekNosin
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
