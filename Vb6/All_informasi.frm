VERSION 5.00
Object = "{CDE57A40-8B86-11D0-B3C6-00A0C90AEA82}#1.0#0"; "MSDATGRD.OCX"
Object = "{86CF1D34-0C5F-11D2-A9FC-0000F8754DA1}#2.0#0"; "Mscomct2.ocx"
Object = "{67397AA1-7FB1-11D0-B148-00A0C922E820}#6.0#0"; "MSADODC.OCX"
Object = "{00025600-0000-0000-C000-000000000046}#5.2#0"; "Crystl32.OCX"
Begin VB.Form Form29 
   BackColor       =   &H00EC6962&
   BorderStyle     =   3  'Fixed Dialog
   Caption         =   "Jurnal Informasi"
   ClientHeight    =   8910
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   18930
   Icon            =   "All_informasi.frx":0000
   LinkTopic       =   "Form29"
   MaxButton       =   0   'False
   MDIChild        =   -1  'True
   MinButton       =   0   'False
   ScaleHeight     =   8910
   ScaleWidth      =   18930
   ShowInTaskbar   =   0   'False
   Begin VB.CommandButton Command25 
      BackColor       =   &H00979B04&
      Caption         =   "Insentif"
      Height          =   375
      Left            =   2400
      Style           =   1  'Graphical
      TabIndex        =   70
      Top             =   8160
      Width           =   2175
   End
   Begin VB.Frame Frame4 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Height          =   1575
      Left            =   4560
      TabIndex        =   58
      Top             =   6000
      Width           =   4335
      Begin VB.CommandButton Command21 
         BackColor       =   &H00979B04&
         Caption         =   "X"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   3720
         Style           =   1  'Graphical
         TabIndex        =   61
         Top             =   840
         Width           =   495
      End
      Begin VB.CommandButton Command20 
         BackColor       =   &H00979B04&
         Caption         =   "Simpan"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   120
         Style           =   1  'Graphical
         TabIndex        =   60
         Top             =   840
         Width           =   3615
      End
      Begin VB.TextBox Text9 
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         Height          =   375
         Left            =   120
         MaxLength       =   20
         MultiLine       =   -1  'True
         TabIndex        =   59
         Text            =   "All_informasi.frx":08CA
         Top             =   360
         Width           =   4095
      End
      Begin VB.Label Label23 
         AutoSize        =   -1  'True
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
         Left            =   1200
         TabIndex        =   63
         Top             =   120
         Width           =   930
      End
      Begin VB.Label Label22 
         AutoSize        =   -1  'True
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
         Left            =   120
         TabIndex        =   62
         Top             =   120
         Width           =   930
      End
   End
   Begin VB.Frame Frame3 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Height          =   1575
      Left            =   120
      TabIndex        =   49
      Top             =   6000
      Width           =   4335
      Begin VB.TextBox Text8 
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         Height          =   375
         Left            =   120
         MaxLength       =   10
         MultiLine       =   -1  'True
         TabIndex        =   52
         Text            =   "All_informasi.frx":08D0
         Top             =   360
         Width           =   4095
      End
      Begin VB.CommandButton Command17 
         BackColor       =   &H00979B04&
         Caption         =   "Simpan"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   120
         Style           =   1  'Graphical
         TabIndex        =   51
         Top             =   840
         Width           =   3615
      End
      Begin VB.CommandButton Command161 
         BackColor       =   &H00979B04&
         Caption         =   "X"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   3720
         Style           =   1  'Graphical
         TabIndex        =   50
         Top             =   840
         Width           =   495
      End
      Begin VB.Label Label21 
         AutoSize        =   -1  'True
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
         Left            =   120
         TabIndex        =   54
         Top             =   120
         Width           =   930
      End
      Begin VB.Label Label20 
         AutoSize        =   -1  'True
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
         Left            =   1200
         TabIndex        =   53
         Top             =   120
         Width           =   930
      End
   End
   Begin VB.Frame Frame2 
      BackColor       =   &H00979B04&
      BorderStyle     =   0  'None
      Height          =   3735
      Left            =   14400
      TabIndex        =   40
      Top             =   3840
      Width           =   4335
      Begin VB.CommandButton Command13 
         BackColor       =   &H00979B04&
         Caption         =   "X"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   3720
         Style           =   1  'Graphical
         TabIndex        =   43
         Top             =   3120
         Width           =   495
      End
      Begin VB.CommandButton Command12 
         BackColor       =   &H00979B04&
         Caption         =   "Simpan"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   1200
         Style           =   1  'Graphical
         TabIndex        =   42
         Top             =   3120
         Width           =   2535
      End
      Begin VB.CommandButton Command14 
         BackColor       =   &H00979B04&
         Caption         =   "Cetak"
         BeginProperty Font 
            Name            =   "MS Sans Serif"
            Size            =   8.25
            Charset         =   0
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   495
         Left            =   120
         Style           =   1  'Graphical
         TabIndex        =   46
         Top             =   3120
         Width           =   1095
      End
      Begin VB.TextBox Text7 
         Appearance      =   0  'Flat
         BackColor       =   &H00FFFFFF&
         Height          =   2655
         Left            =   120
         MaxLength       =   500
         MultiLine       =   -1  'True
         TabIndex        =   41
         Text            =   "All_informasi.frx":08D6
         Top             =   360
         Width           =   4095
      End
      Begin VB.Label Label19 
         AutoSize        =   -1  'True
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
         Left            =   1200
         TabIndex        =   45
         Top             =   120
         Width           =   930
      End
      Begin VB.Label Label18 
         AutoSize        =   -1  'True
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
         Left            =   120
         TabIndex        =   44
         Top             =   120
         Width           =   930
      End
   End
   Begin MSDataGridLib.DataGrid DataGrid3 
      Bindings        =   "All_informasi.frx":08DC
      Height          =   5175
      Left            =   120
      TabIndex        =   68
      Top             =   2400
      Visible         =   0   'False
      Width           =   18615
      _ExtentX        =   32835
      _ExtentY        =   9128
      _Version        =   393216
      AllowUpdate     =   0   'False
      AllowArrows     =   -1  'True
      BackColor       =   16777215
      HeadLines       =   2
      RowHeight       =   13
      WrapCellPointer =   -1  'True
      FormatLocked    =   -1  'True
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   6.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   6.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   23
      BeginProperty Column00 
         DataField       =   "Tanggal"
         Caption         =   "Tanggal"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   "Wilayah"
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
         DataField       =   "Nama"
         Caption         =   "Nama Pemohon"
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
      BeginProperty Column03 
         DataField       =   "Alamat"
         Caption         =   "Alamat"
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
      BeginProperty Column04 
         DataField       =   "Telp"
         Caption         =   "Handphone"
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
         DataField       =   "Buka_faktur"
         Caption         =   "Tanggal Faktur"
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
         DataField       =   "Broker"
         Caption         =   "Link"
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
      BeginProperty Column07 
         DataField       =   "No_Mesin"
         Caption         =   "No Mesin"
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
      BeginProperty Column08 
         DataField       =   "ket_dp"
         Caption         =   "Ket. DP"
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
      BeginProperty Column09 
         DataField       =   "DP"
         Caption         =   "DP"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column10 
         DataField       =   "Subsidi"
         Caption         =   "Subsidi"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column11 
         DataField       =   "Disc"
         Caption         =   "Disc"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column12 
         DataField       =   "Disc_tambahan"
         Caption         =   "Diskon +"
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
      BeginProperty Column13 
         DataField       =   "insentif"
         Caption         =   "Insentif"
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
      BeginProperty Column14 
         DataField       =   "KD_LISING"
         Caption         =   "Leasing"
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
      BeginProperty Column15 
         DataField       =   "Tgl_lunas"
         Caption         =   "Tgl Lunas"
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
      BeginProperty Column16 
         DataField       =   "Pelunasan"
         Caption         =   "Pelunasan"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column17 
         DataField       =   "Tanggal_PO"
         Caption         =   "Status"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   "0"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column18 
         DataField       =   "No_Polisi"
         Caption         =   "No Polisi"
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
      BeginProperty Column19 
         DataField       =   "Nama_Pemilik"
         Caption         =   "Nama Pemilik"
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
      BeginProperty Column20 
         DataField       =   "tgl_biro"
         Caption         =   "Tgl. Biro"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "d MMM yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column21 
         DataField       =   "No_BPKB"
         Caption         =   "No BPKB"
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
      BeginProperty Column22 
         DataField       =   "Tgl_SerahTerima"
         Caption         =   "Tgl Terima"
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
      SplitCount      =   1
      BeginProperty Split0 
         MarqueeStyle    =   3
         SizeMode        =   1
         BeginProperty Column00 
            ColumnWidth     =   734,74
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   345,26
         EndProperty
         BeginProperty Column02 
            ColumnWidth     =   1769,953
         EndProperty
         BeginProperty Column03 
            ColumnWidth     =   1140,095
         EndProperty
         BeginProperty Column04 
            ColumnWidth     =   915,024
         EndProperty
         BeginProperty Column05 
            ColumnWidth     =   1049,953
         EndProperty
         BeginProperty Column06 
            ColumnWidth     =   420,095
         EndProperty
         BeginProperty Column07 
            ColumnWidth     =   1244,976
         EndProperty
         BeginProperty Column08 
            Alignment       =   1
            ColumnWidth     =   929,764
         EndProperty
         BeginProperty Column09 
            Alignment       =   1
            ColumnWidth     =   615,118
         EndProperty
         BeginProperty Column10 
            Alignment       =   1
            ColumnWidth     =   555,024
         EndProperty
         BeginProperty Column11 
            Alignment       =   1
            ColumnWidth     =   420,095
         EndProperty
         BeginProperty Column12 
            Alignment       =   1
            ColumnWidth     =   750,047
         EndProperty
         BeginProperty Column13 
            Alignment       =   1
            ColumnWidth     =   900,284
         EndProperty
         BeginProperty Column14 
            ColumnWidth     =   420,095
         EndProperty
         BeginProperty Column15 
            Alignment       =   2
            ColumnWidth     =   794,835
         EndProperty
         BeginProperty Column16 
            Alignment       =   1
            ColumnWidth     =   959,811
         EndProperty
         BeginProperty Column17 
            ColumnWidth     =   840,189
         EndProperty
         BeginProperty Column18 
            ColumnWidth     =   794,835
         EndProperty
         BeginProperty Column19 
            ColumnWidth     =   900,284
         EndProperty
         BeginProperty Column20 
            ColumnWidth     =   1124,787
         EndProperty
         BeginProperty Column21 
            ColumnWidth     =   645,165
         EndProperty
         BeginProperty Column22 
            Alignment       =   2
            ColumnWidth     =   734,74
         EndProperty
      EndProperty
   End
   Begin VB.CommandButton Command24 
      BackColor       =   &H00979B04&
      Caption         =   "Link"
      Height          =   375
      Left            =   8160
      Style           =   1  'Graphical
      TabIndex        =   67
      Top             =   7680
      Width           =   2175
   End
   Begin MSDataGridLib.DataGrid DataGrid2 
      Bindings        =   "All_informasi.frx":08F1
      Height          =   5175
      Left            =   120
      TabIndex        =   66
      Top             =   2400
      Visible         =   0   'False
      Width           =   18615
      _ExtentX        =   32835
      _ExtentY        =   9128
      _Version        =   393216
      AllowUpdate     =   0   'False
      AllowArrows     =   -1  'True
      BackColor       =   16777215
      HeadLines       =   2
      RowHeight       =   13
      WrapCellPointer =   -1  'True
      FormatLocked    =   -1  'True
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   6.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   6.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   23
      BeginProperty Column00 
         DataField       =   "Tanggal"
         Caption         =   "Tanggal"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd-mmm-yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   "Wilayah"
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
         DataField       =   "Nama"
         Caption         =   "Nama Pemohon"
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
      BeginProperty Column03 
         DataField       =   "Alamat"
         Caption         =   "Alamat"
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
      BeginProperty Column04 
         DataField       =   "Buka_faktur"
         Caption         =   "Tanggal Faktur"
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
         DataField       =   "Broker"
         Caption         =   "Link"
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
      BeginProperty Column06 
         DataField       =   "No_Mesin"
         Caption         =   "No Mesin"
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
      BeginProperty Column07 
         DataField       =   "Warna"
         Caption         =   "Warna "
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
      BeginProperty Column08 
         DataField       =   "ket_dp"
         Caption         =   "Ket. DP"
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
      BeginProperty Column09 
         DataField       =   "DP"
         Caption         =   "DP"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column10 
         DataField       =   "Subsidi"
         Caption         =   "Subsidi"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column11 
         DataField       =   "Disc"
         Caption         =   "Disc"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column12 
         DataField       =   "disc_tambahan"
         Caption         =   "Diskon +"
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
      BeginProperty Column13 
         DataField       =   "insentif"
         Caption         =   "Insentif"
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
      BeginProperty Column14 
         DataField       =   "KD_LISING"
         Caption         =   "Leasing"
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
      BeginProperty Column15 
         DataField       =   "Tgl_lunas"
         Caption         =   "Tgl Lunas"
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
      BeginProperty Column16 
         DataField       =   "Pelunasan"
         Caption         =   "Pelunasan"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column17 
         DataField       =   "Lain_lain"
         Caption         =   "Lain - Lain"
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
      BeginProperty Column18 
         DataField       =   "No_Polisi"
         Caption         =   "No Polisi"
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
      BeginProperty Column19 
         DataField       =   "Nama_Pemilik"
         Caption         =   "Nama Pemilik"
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
      BeginProperty Column20 
         DataField       =   "tgl_biro"
         Caption         =   "Tgl. Biro"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd MMM yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column21 
         DataField       =   "No_BPKB"
         Caption         =   "No BPKB"
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
      BeginProperty Column22 
         DataField       =   "Tgl_SerahTerima"
         Caption         =   "Tgl Terima"
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
      SplitCount      =   1
      BeginProperty Split0 
         MarqueeStyle    =   3
         SizeMode        =   1
         BeginProperty Column00 
            ColumnWidth     =   705,26
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   345,26
         EndProperty
         BeginProperty Column02 
            ColumnWidth     =   1530,142
         EndProperty
         BeginProperty Column03 
            ColumnWidth     =   705,26
         EndProperty
         BeginProperty Column04 
            ColumnWidth     =   1080
         EndProperty
         BeginProperty Column05 
            ColumnWidth     =   510,236
         EndProperty
         BeginProperty Column06 
            ColumnWidth     =   1019,906
         EndProperty
         BeginProperty Column07 
            ColumnWidth     =   360
         EndProperty
         BeginProperty Column08 
            Alignment       =   1
            ColumnWidth     =   900,284
         EndProperty
         BeginProperty Column09 
            Alignment       =   1
            ColumnWidth     =   870,236
         EndProperty
         BeginProperty Column10 
            Alignment       =   1
            ColumnWidth     =   720
         EndProperty
         BeginProperty Column11 
            Alignment       =   1
            ColumnWidth     =   689,953
         EndProperty
         BeginProperty Column12 
            ColumnWidth     =   794,835
         EndProperty
         BeginProperty Column13 
            Alignment       =   1
            ColumnWidth     =   615,118
         EndProperty
         BeginProperty Column14 
            ColumnWidth     =   734,74
         EndProperty
         BeginProperty Column15 
            Alignment       =   2
            ColumnWidth     =   750,047
         EndProperty
         BeginProperty Column16 
            Alignment       =   1
            ColumnWidth     =   764,787
         EndProperty
         BeginProperty Column17 
            Alignment       =   1
            ColumnWidth     =   720
         EndProperty
         BeginProperty Column18 
            ColumnWidth     =   794,835
         EndProperty
         BeginProperty Column19 
            ColumnWidth     =   959,811
         EndProperty
         BeginProperty Column20 
            ColumnWidth     =   975,118
         EndProperty
         BeginProperty Column21 
            ColumnWidth     =   689,953
         EndProperty
         BeginProperty Column22 
            Alignment       =   2
            ColumnWidth     =   870,236
         EndProperty
      EndProperty
   End
   Begin VB.CommandButton Command23 
      BackColor       =   &H00979B04&
      Caption         =   "Surat-Surat"
      Height          =   375
      Left            =   5880
      Style           =   1  'Graphical
      TabIndex        =   65
      Top             =   7680
      Width           =   2175
   End
   Begin VB.CommandButton Command22 
      BackColor       =   &H00979B04&
      Caption         =   "Demo Informasi"
      Height          =   375
      Left            =   5880
      Style           =   1  'Graphical
      TabIndex        =   64
      Top             =   8160
      Width           =   2175
   End
   Begin VB.CommandButton Command19 
      BackColor       =   &H00979B04&
      Caption         =   "Edit Handphone"
      Height          =   375
      Left            =   120
      Style           =   1  'Graphical
      TabIndex        =   57
      Top             =   8160
      Width           =   2175
   End
   Begin VB.CommandButton Command16 
      BackColor       =   &H00979B04&
      Height          =   495
      Left            =   4920
      Picture         =   "All_informasi.frx":0906
      Style           =   1  'Graphical
      TabIndex        =   56
      Top             =   8040
      Visible         =   0   'False
      Width           =   495
   End
   Begin VB.CommandButton Command18 
      BackColor       =   &H00979B04&
      Caption         =   "Tanggal Faktur"
      Height          =   375
      Left            =   2400
      Style           =   1  'Graphical
      TabIndex        =   55
      Top             =   7680
      Width           =   2175
   End
   Begin VB.CommandButton Command15 
      BackColor       =   &H00979B04&
      Caption         =   "Catatan Historis"
      Height          =   375
      Left            =   120
      Style           =   1  'Graphical
      TabIndex        =   47
      Top             =   7680
      Width           =   2175
   End
   Begin VB.CommandButton Command11 
      BackColor       =   &H00979B04&
      Caption         =   "To EXCEL"
      Height          =   1095
      Left            =   4680
      Picture         =   "All_informasi.frx":0D48
      Style           =   1  'Graphical
      TabIndex        =   39
      ToolTipText     =   "Cetak"
      Top             =   7680
      Width           =   1095
   End
   Begin VB.CommandButton Command10 
      BackColor       =   &H00979B04&
      Caption         =   "Cetak"
      Height          =   1095
      Left            =   12600
      Picture         =   "All_informasi.frx":157B
      Style           =   1  'Graphical
      TabIndex        =   38
      ToolTipText     =   "Cetak"
      Top             =   720
      Width           =   1095
   End
   Begin VB.ComboBox Combo3 
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   12240
      Style           =   2  'Dropdown List
      TabIndex        =   36
      Top             =   120
      Width           =   2655
   End
   Begin MSAdodcLib.Adodc Adodc1 
      Height          =   855
      Left            =   7560
      Top             =   120
      Visible         =   0   'False
      Width           =   1455
      _ExtentX        =   2566
      _ExtentY        =   1508
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
      RecordSource    =   "select * from Tinformasi_01 Where Nota='dondon' order by nota"
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
   Begin VB.TextBox Text6 
      Height          =   375
      Left            =   2640
      TabIndex        =   35
      Text            =   "Text6"
      Top             =   600
      Visible         =   0   'False
      Width           =   2295
   End
   Begin VB.TextBox Text5 
      Height          =   495
      Left            =   8160
      TabIndex        =   34
      Text            =   "Text5"
      Top             =   960
      Visible         =   0   'False
      Width           =   2655
   End
   Begin VB.ComboBox Combo2 
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   8160
      Style           =   2  'Dropdown List
      TabIndex        =   32
      Top             =   1560
      Width           =   2655
   End
   Begin VB.TextBox Text4 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   375
      Left            =   8160
      TabIndex        =   31
      Text            =   "Text1"
      Top             =   1920
      Width           =   4815
   End
   Begin VB.CommandButton Command8 
      BackColor       =   &H00C0C0FF&
      Caption         =   "Cetak Kwitansi DP Motor"
      Height          =   375
      Left            =   10560
      Style           =   1  'Graphical
      TabIndex        =   22
      Top             =   8160
      Visible         =   0   'False
      Width           =   2175
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H00FF8080&
      Height          =   1575
      Left            =   720
      TabIndex        =   19
      Top             =   3720
      Width           =   13575
      Begin VB.TextBox Text3 
         Height          =   375
         Left            =   120
         MaxLength       =   100
         TabIndex        =   30
         Text            =   "Text3"
         Top             =   960
         Width           =   12975
      End
      Begin VB.TextBox Text2 
         Appearance      =   0  'Flat
         BackColor       =   &H00C0C0FF&
         Height          =   375
         Left            =   120
         TabIndex        =   20
         Text            =   "Text1"
         Top             =   480
         Width           =   3855
      End
      Begin VB.Label Label6 
         AutoSize        =   -1  'True
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
         ForeColor       =   &H000000C0&
         Height          =   195
         Left            =   120
         TabIndex        =   21
         Top             =   240
         Width           =   930
      End
   End
   Begin VB.CommandButton Command7 
      BackColor       =   &H00C0C0FF&
      Caption         =   "Cetak Kwitansi Harga Motor"
      Height          =   375
      Left            =   120
      Style           =   1  'Graphical
      TabIndex        =   18
      Top             =   8160
      Visible         =   0   'False
      Width           =   2175
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00979B04&
      Caption         =   "KELUAR"
      Height          =   1095
      Left            =   13920
      Picture         =   "All_informasi.frx":1DAE
      Style           =   1  'Graphical
      TabIndex        =   16
      Top             =   720
      Width           =   1095
   End
   Begin VB.CommandButton Command6 
      BackColor       =   &H00C0C0FF&
      Caption         =   "Pengambilan Surat BPKB"
      Height          =   375
      Left            =   10560
      Style           =   1  'Graphical
      TabIndex        =   13
      Top             =   7680
      Visible         =   0   'False
      Width           =   2175
   End
   Begin VB.CommandButton Command5 
      BackColor       =   &H00C0C0FF&
      Caption         =   "Pelunasan Piutang Leasing"
      Height          =   375
      Left            =   2400
      Style           =   1  'Graphical
      TabIndex        =   12
      Top             =   7680
      Visible         =   0   'False
      Width           =   2175
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00C0C0FF&
      Caption         =   "Pelunasan Piutang Broker"
      Height          =   375
      Left            =   120
      Style           =   1  'Graphical
      TabIndex        =   11
      Top             =   7680
      Visible         =   0   'False
      Width           =   2175
   End
   Begin Crystal.CrystalReport CrystalReport1 
      Left            =   10680
      Top             =   240
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   348160
      PrintFileLinesPerPage=   60
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00979B04&
      Caption         =   "Baru"
      Height          =   1095
      Left            =   11400
      Picture         =   "All_informasi.frx":2557
      Style           =   1  'Graphical
      TabIndex        =   10
      Top             =   720
      Width           =   1095
   End
   Begin VB.CommandButton Command9 
      BackColor       =   &H00FF8080&
      Caption         =   "Cetak"
      Height          =   1095
      Left            =   12600
      Picture         =   "All_informasi.frx":2BFF
      Style           =   1  'Graphical
      TabIndex        =   9
      ToolTipText     =   "Cetak"
      Top             =   9240
      Width           =   1095
   End
   Begin VB.TextBox Text1 
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      Height          =   375
      Left            =   2640
      TabIndex        =   8
      Text            =   "Text1"
      Top             =   1920
      Width           =   4815
   End
   Begin VB.ComboBox Combo1 
      BackColor       =   &H00FFFFFF&
      Height          =   315
      Left            =   2640
      Style           =   2  'Dropdown List
      TabIndex        =   6
      Top             =   1560
      Width           =   2655
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00979B04&
      Height          =   495
      Left            =   6960
      Picture         =   "All_informasi.frx":3432
      Style           =   1  'Graphical
      TabIndex        =   5
      Top             =   1080
      Width           =   495
   End
   Begin MSComCtl2.DTPicker DTPicker2 
      Height          =   375
      Left            =   4920
      TabIndex        =   4
      Top             =   1080
      Width           =   1815
      _ExtentX        =   3201
      _ExtentY        =   661
      _Version        =   393216
      Format          =   89063424
      CurrentDate     =   38249
   End
   Begin MSComCtl2.DTPicker DTPicker1 
      Height          =   375
      Left            =   2640
      TabIndex        =   3
      Top             =   1080
      Width           =   1815
      _ExtentX        =   3201
      _ExtentY        =   661
      _Version        =   393216
      Format          =   89063424
      CurrentDate     =   38249
   End
   Begin MSDataGridLib.DataGrid DataGrid1 
      Bindings        =   "All_informasi.frx":3874
      Height          =   5175
      Left            =   120
      TabIndex        =   0
      Top             =   2400
      Width           =   18615
      _ExtentX        =   32835
      _ExtentY        =   9128
      _Version        =   393216
      AllowUpdate     =   0   'False
      AllowArrows     =   -1  'True
      BackColor       =   16777215
      HeadLines       =   2
      RowHeight       =   13
      WrapCellPointer =   -1  'True
      FormatLocked    =   -1  'True
      BeginProperty HeadFont {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   6.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      BeginProperty Font {0BE35203-8F91-11CE-9DE3-00AA004BB851} 
         Name            =   "Tahoma"
         Size            =   6.75
         Charset         =   0
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ColumnCount     =   34
      BeginProperty Column00 
         DataField       =   "Tanggal"
         Caption         =   "Tanggal"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd-mmm-yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column01 
         DataField       =   "Nota"
         Caption         =   "NoTransaksi"
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
         DataField       =   "Wilayah"
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
      BeginProperty Column03 
         DataField       =   "Nama"
         Caption         =   "Nama Pemohon"
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
      BeginProperty Column04 
         DataField       =   "Alamat"
         Caption         =   "Alamat"
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
      BeginProperty Column05 
         DataField       =   "Telp"
         Caption         =   "Handphone"
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
         DataField       =   "Buka_faktur"
         Caption         =   "Tanggal Faktur"
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
      BeginProperty Column07 
         DataField       =   "Broker"
         Caption         =   "Link"
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
      BeginProperty Column08 
         DataField       =   "No_Rangka"
         Caption         =   "No Rangka"
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
      BeginProperty Column09 
         DataField       =   "No_Mesin"
         Caption         =   "No Mesin"
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
      BeginProperty Column10 
         DataField       =   "Type"
         Caption         =   "Type"
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
      BeginProperty Column11 
         DataField       =   "Warna"
         Caption         =   "Warna "
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
      BeginProperty Column12 
         DataField       =   "ket_dp"
         Caption         =   "Ket. DP"
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
      BeginProperty Column13 
         DataField       =   "DP"
         Caption         =   "DP"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column14 
         DataField       =   "Subsidi"
         Caption         =   "Subsidi"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column15 
         DataField       =   "Disc"
         Caption         =   "Disc"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column16 
         DataField       =   "disc_tambahan"
         Caption         =   "Diskon +"
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
      BeginProperty Column17 
         DataField       =   "Insentif"
         Caption         =   "Insentif"
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
      BeginProperty Column18 
         DataField       =   "KD_LISING"
         Caption         =   "Leasing"
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
      BeginProperty Column19 
         DataField       =   "Tgl_lunas"
         Caption         =   "Tgl Lunas"
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
      BeginProperty Column20 
         DataField       =   "Pelunasan"
         Caption         =   "Pelunasan"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "###,###"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column21 
         DataField       =   "Lain_lain"
         Caption         =   "Lain - Lain"
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
      BeginProperty Column22 
         DataField       =   "Tanggal_PO"
         Caption         =   "Status"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   0
            Format          =   "0"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1033
            SubFormatType   =   0
         EndProperty
      EndProperty
      BeginProperty Column23 
         DataField       =   "Kasus2"
         Caption         =   "Kasus DP"
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
      BeginProperty Column24 
         DataField       =   "Tgl_kasus"
         Caption         =   "Tgl. Kasus DP"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "d-MMM-yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column25 
         DataField       =   "kasus"
         Caption         =   "Kasus Leasing"
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
      BeginProperty Column26 
         DataField       =   "Tanggal_kasus"
         Caption         =   "Tgl. Kasus Leasing"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd-mmm-yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column27 
         DataField       =   "No_Polisi"
         Caption         =   "No Polisi"
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
      BeginProperty Column28 
         DataField       =   "Nama_Pemilik"
         Caption         =   "Nama Pemilik"
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
      BeginProperty Column29 
         DataField       =   "tgl_biro"
         Caption         =   "Tgl. Biro"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd MMM yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      BeginProperty Column30 
         DataField       =   "No_BPKB"
         Caption         =   "No BPKB"
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
      BeginProperty Column31 
         DataField       =   "Tgl_SerahTerima"
         Caption         =   "Tgl Terima"
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
      BeginProperty Column32 
         DataField       =   "Refund"
         Caption         =   "Refund"
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
      BeginProperty Column33 
         DataField       =   "Tgl_refund"
         Caption         =   "Tgl. Refund"
         BeginProperty DataFormat {6D835690-900B-11D0-9484-00A0C91110ED} 
            Type            =   1
            Format          =   "dd MMM yy"
            HaveTrueFalseNull=   0
            FirstDayOfWeek  =   0
            FirstWeekOfYear =   0
            LCID            =   1057
            SubFormatType   =   3
         EndProperty
      EndProperty
      SplitCount      =   1
      BeginProperty Split0 
         MarqueeStyle    =   3
         SizeMode        =   1
         BeginProperty Column00 
            ColumnWidth     =   734,74
         EndProperty
         BeginProperty Column01 
            ColumnWidth     =   689,953
         EndProperty
         BeginProperty Column02 
            ColumnWidth     =   255,118
         EndProperty
         BeginProperty Column03 
            ColumnWidth     =   1769,953
         EndProperty
         BeginProperty Column04 
            ColumnWidth     =   1140,095
         EndProperty
         BeginProperty Column05 
            ColumnWidth     =   915,024
         EndProperty
         BeginProperty Column06 
            ColumnWidth     =   1080
         EndProperty
         BeginProperty Column07 
            ColumnWidth     =   420,095
         EndProperty
         BeginProperty Column08 
            ColumnWidth     =   1019,906
         EndProperty
         BeginProperty Column09 
            ColumnWidth     =   1244,976
         EndProperty
         BeginProperty Column10 
            ColumnWidth     =   450,142
         EndProperty
         BeginProperty Column11 
            ColumnWidth     =   374,74
         EndProperty
         BeginProperty Column12 
            Alignment       =   1
            ColumnWidth     =   929,764
         EndProperty
         BeginProperty Column13 
            Alignment       =   1
            ColumnWidth     =   615,118
         EndProperty
         BeginProperty Column14 
            Alignment       =   1
            ColumnWidth     =   555,024
         EndProperty
         BeginProperty Column15 
            Alignment       =   1
            ColumnWidth     =   420,095
         EndProperty
         BeginProperty Column16 
            Alignment       =   1
            ColumnWidth     =   764,787
         EndProperty
         BeginProperty Column17 
            Alignment       =   1
            ColumnWidth     =   750,047
         EndProperty
         BeginProperty Column18 
            ColumnWidth     =   420,095
         EndProperty
         BeginProperty Column19 
            Alignment       =   2
            ColumnWidth     =   794,835
         EndProperty
         BeginProperty Column20 
            Alignment       =   1
            ColumnWidth     =   959,811
         EndProperty
         BeginProperty Column21 
            Alignment       =   1
            ColumnWidth     =   900,284
         EndProperty
         BeginProperty Column22 
            ColumnWidth     =   840,189
         EndProperty
         BeginProperty Column23 
            Alignment       =   1
            ColumnWidth     =   824,882
         EndProperty
         BeginProperty Column24 
            Alignment       =   2
            ColumnWidth     =   569,764
         EndProperty
         BeginProperty Column25 
            Alignment       =   1
            ColumnWidth     =   629,858
         EndProperty
         BeginProperty Column26 
            Alignment       =   2
            ColumnWidth     =   450,142
         EndProperty
         BeginProperty Column27 
            ColumnWidth     =   794,835
         EndProperty
         BeginProperty Column28 
            ColumnWidth     =   900,284
         EndProperty
         BeginProperty Column29 
            ColumnWidth     =   1035,213
         EndProperty
         BeginProperty Column30 
            ColumnWidth     =   645,165
         EndProperty
         BeginProperty Column31 
            Alignment       =   2
            ColumnWidth     =   734,74
         EndProperty
         BeginProperty Column32 
            ColumnWidth     =   989,858
         EndProperty
         BeginProperty Column33 
            ColumnWidth     =   1200,189
         EndProperty
      EndProperty
   End
   Begin VB.Label Label25 
      Caption         =   "Label25"
      Height          =   495
      Left            =   8880
      TabIndex        =   71
      Top             =   4200
      Width           =   1215
   End
   Begin VB.Label Label24 
      Caption         =   "Label24"
      Height          =   495
      Left            =   8880
      TabIndex        =   69
      Top             =   4200
      Width           =   1215
   End
   Begin VB.Label Label17 
      Caption         =   "Label17"
      Height          =   495
      Left            =   7080
      TabIndex        =   48
      Top             =   4200
      Width           =   1215
   End
   Begin VB.Label Label16 
      Caption         =   "Label16"
      Height          =   495
      Left            =   7080
      TabIndex        =   37
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label15 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "dan"
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
      Left            =   7560
      TabIndex        =   33
      Top             =   1560
      Width           =   315
   End
   Begin VB.Label Label14 
      Caption         =   "Label14"
      Height          =   495
      Left            =   7080
      TabIndex        =   29
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label13 
      Caption         =   "Label13"
      Height          =   495
      Left            =   7080
      TabIndex        =   28
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label12 
      Caption         =   "Label12"
      Height          =   495
      Left            =   7080
      TabIndex        =   27
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label11 
      Caption         =   "Label11"
      Height          =   495
      Left            =   7080
      TabIndex        =   26
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label10 
      Caption         =   "Label10"
      Height          =   495
      Left            =   7080
      TabIndex        =   25
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label9 
      Caption         =   "Label9"
      Height          =   495
      Left            =   7080
      TabIndex        =   24
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label8 
      Caption         =   "Label8"
      Height          =   495
      Left            =   7080
      TabIndex        =   23
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label5 
      Caption         =   "Label5"
      Height          =   495
      Left            =   7080
      TabIndex        =   17
      Top             =   4320
      Width           =   1215
   End
   Begin VB.Label Label7 
      Alignment       =   1  'Right Justify
      Appearance      =   0  'Flat
      BackColor       =   &H00FFFFFF&
      BorderStyle     =   1  'Fixed Single
      Caption         =   "Label7"
      BeginProperty Font 
         Name            =   "MS Sans Serif"
         Size            =   8.25
         Charset         =   0
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      ForeColor       =   &H00000000&
      Height          =   375
      Left            =   10920
      TabIndex        =   15
      Top             =   8070
      Width           =   4095
   End
   Begin VB.Label Label4 
      Appearance      =   0  'Flat
      AutoSize        =   -1  'True
      BackColor       =   &H80000005&
      BackStyle       =   0  'Transparent
      Caption         =   "TOTAL Transfer Leasing"
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
      Left            =   8400
      TabIndex        =   14
      Top             =   8160
      Width           =   2040
   End
   Begin VB.Label Label3 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Pencarian Berdasarkan"
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
      Left            =   240
      TabIndex        =   7
      Top             =   1560
      Width           =   1995
   End
   Begin VB.Label Label2 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "---"
      Height          =   195
      Left            =   4680
      TabIndex        =   2
      Top             =   1080
      Width           =   135
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      BackStyle       =   0  'Transparent
      Caption         =   "Tanggal"
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
      Left            =   240
      TabIndex        =   1
      Top             =   1170
      Width           =   675
   End
   Begin VB.Image Image1 
      Height          =   14535
      Left            =   -480
      Picture         =   "All_informasi.frx":3889
      Stretch         =   -1  'True
      Top             =   -120
      Width           =   21855
   End
End
Attribute VB_Name = "Form29"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim con As ADODB.Connection
Dim rs As ADODB.Recordset

Private Sub Combo1_Click()
    Text1.Text = ""
    Text6.Text = ""
    Text4.Text = ""
    Select Case Combo1.ListIndex
        Case 0: Text6.Text = "Tanggal"
        Case 1: Text6.Text = "Nama"
        Case 2: Text6.Text = "Broker"
        Case 3: Text6.Text = "No_Rangka"
        Case 4: Text6.Text = "No_Mesin"
        Case 5: Text6.Text = "Type"
        Case 6: Text6.Text = "Kd_Lising"
        Case 7: Text6.Text = "Tanggal_PO"
        Case 8: Text6.Text = "Tgl_Lunas"
        Case 9: Text6.Text = "No_Polisi"
        Case 10: Text6.Text = "No_BPKB"
        Case 11: Text6.Text = "Tgl_serahterima"
        Case 12: Text6.Text = "Wilayah"
        Case 13: Text6.Text = "Alamat"
        Case 14: Text6.Text = "buka_faktur"
    End Select
End Sub

Private Sub Combo2_Click()
    Text4.Text = ""
    Text5.Text = ""
    Select Case Combo2.ListIndex
        Case 0: Text5.Text = "Nama"
        Case 1: Text5.Text = "Broker"
        Case 2: Text5.Text = "No_Rangka"
        Case 3: Text5.Text = "No_Mesin"
        Case 4: Text5.Text = "Type"
        Case 5: Text5.Text = "Kd_Lising"
        Case 6: Text5.Text = "No_Polisi"
        Case 7: Text5.Text = "No_BPKB"
        Case 8: Text5.Text = "Wilayah"
        Case 8: Text5.Text = "Alamat"
        Case 9: Text5.Text = "Tanggal_PO"
    End Select
End Sub

Private Sub Combo3_Click()
    If Combo3.Text = "JayaMotor 1" Then
        Label16.Caption = "Y"
    ElseIf Combo3.Text = "JayaMotor 2" Then
        Label16.Caption = "Z"
    ElseIf Combo3.Text = "JayaMotor 3" Then
        Label16.Caption = "X"
    ElseIf Combo3.Text = "Other" Then
        Label16.Caption = "W"
    Else
        Label16.Caption = ""
    End If
End Sub

Private Sub Command1_Click()
    Dim msql As String
    Screen.MousePointer = vbHourglass
  '  Call hapus
    msql = "select * from Tinformasi_01 where (" & Text6.Text & ") >='" & Format(DTPicker1.Value, "MM-dd-yy") & "' and (" & Text6.Text & ") <='" & Format(DTPicker2.Value, "MM-dd-yy") & "' and Post='Ya' and nota LIKE '" & "%" & Label16.Caption & "' order by nota,(" & Text6.Text & ")"
   ' Set rs = con.Execute(msql)
    '        With rs
      '          If Not .EOF Then
     '               .MoveFirst
     '               Do Until .EOF
      '                  Label5.Caption = RTrim(!Nota)
      '                  Call simpan
      '                  .MoveNext
      '              Loop
      '          End If
      '      End With

    Text1.Text = ""
    Adodc1.RecordSource = msql
    Adodc1.Refresh
    Screen.MousePointer = vbDefault
End Sub

Private Sub Command10_Click()
    If Text4.Text = "" Then
        If Combo1.Text = "Tanggal Terima BPKB" Then
            CrystalReport1.SelectionFormula = "{TInformasi_01." & Text6.Text & "} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01." & Text6.Text & "} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        ElseIf Combo1.Text = "Tanggal Lunas" Then
            CrystalReport1.SelectionFormula = "{TInformasi_01." & Text6.Text & "} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01." & Text6.Text & "} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        ElseIf Combo1.Text = "Tanggal" Then
            CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.tanggal} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        Else
            CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.tanggal} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01." & Text6.Text & "} LIKE ('" & Text1.Text & "*" & "') and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        End If
    Else
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.tanggal} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01." & Text6.Text & "} LIKE ('" & Text1.Text & "*" & "') and {TInformasi_01." & Text5.Text & "} LIKE ('" & Text4.Text & "*" & "') and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
    End If
    CrystalReport1.ReportFileName = App.Path & "\lprinformasi.rpt"
    CrystalReport1.RetrieveDataFiles
    CrystalReport1.Destination = crptToWindow
    CrystalReport1.WindowState = crptMaximized
    CrystalReport1.Action = 1
    CrystalReport1.Reset
End Sub

Private Sub Command11_Click()
    If Text4.Text = "" Then
        If Combo1.Text = "Tanggal PO" Or Combo1.Text = "Tanggal Terima BPKB" Or Combo1.Text = "Tanggal Lunas" Then
            CrystalReport1.SelectionFormula = "{TInformasi_01." & Text6.Text & "} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.Tgl_lunas} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        ElseIf Combo1.Text = "Tanggal" Then
            CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.tanggal} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        Else
            CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.tanggal} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01." & Text6.Text & "} LIKE ('" & Text1.Text & "*" & "') and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
        End If
    Else
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & DTPicker1.Value & "') and {TInformasi_01.tanggal} <= datevalue('" & DTPicker2.Value & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01." & Text6.Text & "} LIKE ('" & Text1.Text & "*" & "') and {TInformasi_01." & Text5.Text & "} LIKE ('" & Text4.Text & "*" & "') and {TInformasi_01.Nota} LIKE ('" & "*" & Label16.Caption & "')"
    End If
    CrystalReport1.ReportFileName = App.Path & "\lprsemuanya.rpt"
    CrystalReport1.RetrieveDataFiles
    CrystalReport1.Destination = crptToWindow
    CrystalReport1.WindowState = crptMaximized
    CrystalReport1.Action = 1
    CrystalReport1.Reset
End Sub

Private Sub Command12_Click()
    Dim msql As String
    msql = "update TInformasi_01 set " & _
        " kopelan='" & Text7.Text & "' " & _
        " where no_mesin='" & Label19.Caption & "'"
    con.Execute msql, , adCmdText
    Adodc1.Refresh
    Command13_Click
End Sub

Private Sub Command13_Click()
    Frame2.Visible = False
End Sub

Private Sub Command14_Click()
    CrystalReport1.SelectionFormula = "{TInformasi_01.no_mesin}='" & Label19.Caption & "' and {TInformasi_01.no_mesin}={TCicilan.no_mesin}"
    CrystalReport1.ReportFileName = App.Path & "\copelan.rpt"
    CrystalReport1.RetrieveDataFiles
    CrystalReport1.Destination = crptToWindow
    CrystalReport1.WindowState = crptMaximized
    CrystalReport1.Action = 1
    CrystalReport1.Reset
End Sub

Private Sub Command15_Click()
    Form44.Show
    Form44.SetFocus
    Label24.Caption = "yes"
End Sub

Private Sub Command161_Click()
    Frame3.Visible = False
End Sub

Private Sub Command17_Click()
    Dim msql As String
    If Label25.Caption = "bukafaktur" Then
        msql = "update TInformasi_01 set " & _
            " buka_faktur='" & Text8.Text & "' " & _
            " where no_mesin='" & Label20.Caption & "'"
        con.Execute msql, , adCmdText
    ElseIf Label25.Caption = "insentif" Then
        msql = "update TInformasi_01 set " & _
            " insentif='" & Val(Format(Text8.Text, "")) & "' " & _
            " where no_mesin='" & Label20.Caption & "'"
        con.Execute msql, , adCmdText
    End If
    Adodc1.Refresh
    Command161_Click
End Sub

Private Sub Command18_Click()
    Frame3.Visible = True
    Text8.Text = ""
    Label25.Caption = "bukafaktur"
End Sub

Private Sub Command19_Click()
    Frame4.Visible = True
    Text9.Text = ""
    Text9.SetFocus
End Sub

Private Sub Command2_Click()
    DTPicker1.Value = Date
    DTPicker2.Value = Date
    Text1.Text = ""
    Text2.Text = ""
    Text5.Text = ""
    Text6.Text = ""
    Label17.Caption = ""
    Frame1.Visible = False
    Frame2.Visible = False
    Frame3.Visible = False
    Frame4.Visible = False
    DataGrid2.Visible = False
    DataGrid3.Visible = False
    
    Combo1.Clear
    Combo1.AddItem "Tanggal"
    Combo1.AddItem "Nama Konsumen"
    Combo1.AddItem "Link"
    Combo1.AddItem "Nomor Rangka"
    Combo1.AddItem "Nomor Mesin"
    Combo1.AddItem "Type"
    Combo1.AddItem "Leasing"
    Combo1.AddItem "Status"
    Combo1.AddItem "Tanggal Lunas"
    Combo1.AddItem "Nomor Polisi"
    Combo1.AddItem "Nomor BPKB"
    Combo1.AddItem "Tanggal Terima BPKB"
    Combo1.AddItem "Dealer"
    Combo1.AddItem "Alamat"
    Combo1.AddItem "Tanggal Faktur"
    Combo1.Text = "Tanggal"
    
    Combo2.Clear
    Combo2.AddItem "Nama Konsumen"
    Combo2.AddItem "Link"
    Combo2.AddItem "Nomor Rangka"
    Combo2.AddItem "Nomor Mesin"
    Combo2.AddItem "Type"
    Combo2.AddItem "Leasing"
    Combo2.AddItem "Nomor Polisi"
    Combo2.AddItem "Nomor BPKB"
    Combo2.AddItem "Dealer"
    Combo2.AddItem "Alamat"
    
    Adodc1.RecordSource = "select * from TInformasi_01 where nota='uchahunt'"
    Adodc1.Refresh
    Label7.Caption = "0"
End Sub

Private Sub Command20_Click()
    Dim msql As String
    msql = "update TInformasi_01 set " & _
        " telp='" & Text9.Text & "' " & _
        " where no_mesin='" & Label23.Caption & "'"
    con.Execute msql, , adCmdText
    Adodc1.Refresh
    Frame4.Visible = False
End Sub

Private Sub Command21_Click()
    Frame4.Visible = False
End Sub

Private Sub Command22_Click()
    Unload Me
    Form291.Show
    Form291.SetFocus
End Sub

Private Sub Command23_Click()
    If DataGrid2.Visible = True Then
        DataGrid2.Visible = False
        DataGrid3.Visible = False
        Command23.Caption = "Surat-surat"
        Form29.Caption = "Jurnal Informasi"
    Else
        DataGrid2.Visible = True
        Command23.Caption = "Jurnal Informasi"
        Form29.Caption = "Surat-surat"
    End If
End Sub

Private Sub Command24_Click()
    If DataGrid3.Visible = True Then
        DataGrid3.Visible = False
        DataGrid2.Visible = False
        Command24.Caption = "Link"
        Form29.Caption = "Jurnal Informasi"
    Else
        DataGrid3.Visible = True
        Command24.Caption = "Jurnal Informasi"
        Form29.Caption = "Link"
    End If
End Sub

Private Sub Command25_Click()
    Frame3.Visible = True
    Text8.Text = ""
    Label25.Caption = "insentif"
End Sub

Private Sub Command3_Click()
    Form25.Show
    If frmLogin.Text7.Text = "LAPTOP" Then
        If frmLogin.Text1.Text <> "TIALAPTOP" And frmLogin.Text2.Text <> "PRIKITIW" Then
            Form25.Command2.Visible = False
        End If
    End If
    Form25.SetFocus
End Sub

Private Sub Command4_Click()
    Unload Me
End Sub

Private Sub Command5_Click()
    Form15.Show
    If frmLogin.Text7.Text = "LAPTOP" Then
        If frmLogin.Text1.Text <> "TIALAPTOP" And frmLogin.Text2.Text <> "PRIKITIW" Then
            Form15.Command1.Visible = False
            Form15.Command2.Visible = False
        End If
    End If
    Form15.SetFocus
End Sub

Private Sub Command6_Click()
    Form7.Show
    Form7.SetFocus
End Sub

Private Sub Command7_Click()
    Label10.Caption = "hg"
    Frame1.Visible = True
    Text2.Text = ""
    Text3.Text = ""
    Text2.SetFocus
End Sub

Private Sub Command8_Click()
    Label10.Caption = "dp"
    Frame1.Visible = True
    Text2.Text = ""
    Text3.Text = ""
    Text2.SetFocus
End Sub

Private Sub Command9_Click()
    If Combo1.Text = "Tanggal PO" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.Piutang_tempo} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.Piutang_tempo} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya'"
    ElseIf Combo1.Text = "Tanggal Terima BPKB" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.Tgl_serahterima} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.Tgl_serahterima} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya'"
    ElseIf Combo1.Text = "Tanggal Lunas" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.Tgl_lunas} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.Tgl_lunas} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya'"
    ElseIf Combo1.Text = "Nama Konsumen" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Nama} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Nomor Rangka" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.No_rangka} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Nomor Mesin" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.No_mesin} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Link" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.broker} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Type" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Type} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Leasing" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.kd_lising} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Nomor Polisi" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.No_polisi} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Nomor BPKB" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.No_BPKB} LIKE ('" & Text1.Text & "*" & "')"
    ElseIf Combo1.Text = "Dealer" Then
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya' and {TInformasi_01.Wilayah} LIKE ('" & Text1.Text & "*" & "')"
    Else
        CrystalReport1.SelectionFormula = "{TInformasi_01.tanggal} >= datevalue('" & Format(DTPicker1.Value, "MM-dd-yy") & "') & " ') and {TInformasi_01.tanggal} <= datevalue('" & Format(DTPicker2.Value, "MM-dd-yy") & "') and {TInformasi_01.Post}='Ya'"
    End If
    
    CrystalReport1.ReportFileName = App.Path & "\lprinformasi.rpt"
    CrystalReport1.RetrieveDataFiles
    CrystalReport1.Destination = crptToWindow
    CrystalReport1.WindowState = crptMaximized
    CrystalReport1.Action = 1
    CrystalReport1.Reset
End Sub

Private Sub DataGrid1_dblClick()
    On Error Resume Next
    Text7.Text = ""
    Label19.Caption = RTrim(Adodc1.Recordset!No_mesin)
    Label20.Caption = RTrim(Adodc1.Recordset!No_mesin)
    Label23.Caption = RTrim(Adodc1.Recordset!No_mesin)
    Text7.Text = RTrim(Adodc1.Recordset!kopelan)
    If Label24.Caption = "yes" Then
        Form44.LOADEDED
        Form44.SetFocus
    End If
End Sub

Private Sub DataGrid2_DblClick()
    On Error Resume Next
    Text7.Text = ""
    Label19.Caption = RTrim(Adodc1.Recordset!No_mesin)
    Label20.Caption = RTrim(Adodc1.Recordset!No_mesin)
    Label23.Caption = RTrim(Adodc1.Recordset!No_mesin)
    Text7.Text = RTrim(Adodc1.Recordset!kopelan)
End Sub


Private Sub Form_Load()
    Set con = New ADODB.Connection
    con.Open "Softtech"
    DTPicker1.Value = Date
    DTPicker2.Value = Date
    Text1.Text = ""
    Text2.Text = ""
    Text4.Text = ""
    Text6.Text = ""
    Label24.Caption = "no"
    
    Top = 0
    Left = 0
    Frame1.Visible = False
    Frame2.Visible = False
    Frame4.Visible = False
    Combo1.Clear
    Combo1.AddItem "Tanggal"
    Combo1.AddItem "Nama Konsumen"
    Combo1.AddItem "Link"
    Combo1.AddItem "Nomor Rangka"
    Combo1.AddItem "Nomor Mesin"
    Combo1.AddItem "Type"
    Combo1.AddItem "Leasing"
    Combo1.AddItem "Status"
    Combo1.AddItem "Tanggal Lunas"
    Combo1.AddItem "Nomor Polisi"
    Combo1.AddItem "Nomor BPKB"
    Combo1.AddItem "Tanggal Terima BPKB"
    Combo1.AddItem "Dealer"
    Combo1.AddItem "Alamat"
    Combo1.AddItem "Tanggal Faktur"
    Combo1.Text = "Tanggal"
    
    Combo2.Clear
    Combo2.AddItem "Nama Konsumen"
    Combo2.AddItem "Link"
    Combo2.AddItem "Nomor Rangka"
    Combo2.AddItem "Nomor Mesin"
    Combo2.AddItem "Type"
    Combo2.AddItem "Leasing"
    Combo2.AddItem "Nomor Polisi"
    Combo2.AddItem "Nomor BPKB"
    Combo2.AddItem "Dealer"
    Combo2.AddItem "Alamat"
    
    Combo3.Clear
    Combo3.AddItem "JayaMotor 1"
    Combo3.AddItem "JayaMotor 2"
    Combo3.AddItem "JayaMotor 3"
    Combo3.AddItem "Other"
    Combo3.AddItem "Semua Data"
    Combo3.Text = "Semua Data"

    Label7.Caption = ""

    Frame3.Visible = False
End Sub

Private Sub Form_Unload(Cancel As Integer)
    con.Close
    Set con = Nothing
End Sub
Sub hapus()
    Dim msql As String
    msql = "delete from TTempCetak"
    con.Execute msql, , adCmdText
End Sub

Private Sub Text1_Change()
    On Error GoTo tangan
    If Text1.Text <> "" Then
        Screen.MousePointer = vbHourglass
    '    Call hapus
        If Text6.Text <> "" Then
            msql = "select * from TInformasi_01 where tanggal >= '" & Format(DTPicker1.Value, "MM-dd-yy") & "' and tanggal <= '" & Format(DTPicker2.Value, "MM-dd-yy") & "' and (" & Text6.Text & ") LIKE '" & Text1.Text & "%" & "' and Post='Ya' and nota LIKE '" & "%" & Label16.Caption & "' order by TANGGAL"
        End If
     '       Set rs = con.Execute(msql)
     '       With rs
     '           If Not .EOF Then
     '               .MoveFirst
     '               Do Until .EOF
     '                   Label5.Caption = RTrim(!Nota)
     '                   Call simpan
     '                   .MoveNext
     '               Loop
     '           End If
     '       End With
        Adodc1.RecordSource = msql
        Adodc1.Refresh
        Call hit_leasing
            Screen.MousePointer = vbDefault

    End If
    Exit Sub
    
tangan:
    MsgBox "Tentukan dahulu Pencarian berdasarkan object apa", vbExclamation, "Jaya Motor"
    Screen.MousePointer = vbDefault

    Exit Sub
End Sub
Sub hit_leasing()
    Label7.Caption = "0"
    Dim msql2 As String
    msql2 = "select * from TInformasi_01 where tgl_lunas >= '" & Format(DTPicker1.Value, "MM-dd-yy") & "' and tgl_lunas <= '" & Format(DTPicker2.Value, "MM-dd-yy") & "' and kd_lising ='" & Text1.Text & "' order by tanggal,kd_lising"
    Set rs = con.Execute(msql2)
        
    With rs
        If Not .EOF Then
            .MoveFirst
            Do Until .EOF
                Label7.Caption = Val(Label7.Caption) + !Pelunasan
                .MoveNext
            Loop
            Label7.Caption = Format(Label7.Caption, "###,###")
        End If
    End With
End Sub
Private Sub Text1_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        On Error Resume Next
        Dim msql As String
        If Text1.Text <> "" Then
            Select Case Combo1.ListIndex
                Case 0: Text6.Text = "Tanggal"
                Case 1: Text6.Text = "Nama"
                Case 2: Text6.Text = "Broker"
                Case 3: Text6.Text = "No_Rangka"
                Case 4: Text6.Text = "No_Mesin"
                Case 5: Text6.Text = "Type"
                Case 6: Text6.Text = "Kd_Lising"
                Case 7: Text6.Text = "Piutang_tempo"
                Case 8: Text6.Text = "Tgl_Lunas"
                Case 9: Text6.Text = "No_Polisi"
                Case 10: Text6.Text = "No_BPKB"
                Case 11: Text6.Text = "Tgl_serahterima"
                Case 12: Text6.Text = "Wilayah"
            End Select
            msql = "select * from TInformasi_01 where (" & Text6.Text & ") LIKE '" & Text1.Text & "%" & "' and Post='Ya' order by (" & Text6.Text & ")"
            Adodc1.RecordSource = msql
            Adodc1.Refresh
        End If
    End If
End Sub

Sub simpan()
    Dim msql As String
    msql = "select * from TTempCetak where nota='" & Label5.Caption & "'"
    Set rs = con.Execute(msql)
        
    If rs.EOF Then
        msql = "Insert Into TTempCetak " _
               & "([nota]) " _
               & "VALUES ('" & Label5.Caption & "');"
        con.Execute msql, , adCmdText
    End If
End Sub

Sub simpan2()
    Dim msql As String
    msql = "select * from TTerbilang where nota='" & Label8.Caption & "'"
    Set rs = con.Execute(msql)
        
    If rs.EOF Then
        msql = "Insert Into TTerbilang " _
               & "([nota],[Terbilang],[Nama],[total],[keterangan]) " _
               & "VALUES ('" & Label8.Caption & "','" & konvers(Label9.Caption) & "','" & Label12.Caption & "','" & Label9.Caption & "','" & Label13.Caption & "');"
        con.Execute msql, , adCmdText
    End If
End Sub

Private Sub Text2_KeyDown(KeyCode As Integer, Shift As Integer)
    If KeyCode = 13 Then
        If Text2.Text <> "" Then
            Text3.SetFocus
        End If
    End If
End Sub

Sub cariharga()
    Dim msql As String
    msql = "select * from TKreditan where No_Mesin ='" & Text2.Text & "' order by no_mesin"
    Set rs = con.Execute(msql)
        
    With rs
        If Not .EOF Then
            Label9.Caption = !Piutang
            Label12.Caption = RTrim(!kd_lising)
        End If
    End With
End Sub

Sub cariharga2()
    Dim msql As String
    msql = "select * from TType where kd_type ='" & Label14.Caption & "'"
    Set rs = con.Execute(msql)
        
    With rs
        If Not .EOF Then
            Label9.Caption = !Harga_dasar
        End If
    End With
End Sub

Sub hapus2()
    Dim msql As String
    msql = "delete from TTerbilang"
    con.Execute msql, , adCmdText
End Sub

Sub cetak1()
    If Label10.Caption = "dp" Then
        CrystalReport1.ReportFileName = App.Path & "\kwitansi.rpt"
    Else
        CrystalReport1.ReportFileName = App.Path & "\kwitansi2.rpt"
    End If
    CrystalReport1.RetrieveDataFiles
    CrystalReport1.Destination = crptToWindow
    CrystalReport1.WindowState = crptMaximized
    CrystalReport1.Action = 1
    CrystalReport1.Reset
End Sub

Private Sub Text3_KeyDown(KeyCode As Integer, Shift As Integer)
    Dim msql As String
    If KeyCode = 13 Then
        If Text2.Text <> "" Then
            msql = "select * from TInformasi_01 where No_Mesin ='" & Text2.Text & "'"
            Set rs = con.Execute(msql)
        
            With rs
                If Not .EOF Then
                    Call hapus2
                    Adodc1.RecordSource = msql
                    Adodc1.Refresh
                    Label8.Caption = RTrim(!Nota)
                    Label9.Caption = !DP
                    Label12.Caption = RTrim(!Nama)
                    Label14.Caption = RTrim(!Type)
                    Label13.Caption = Text3.Text
                    If Label10.Caption = "hg" Then
                     '   If RTrim(!kd_lising) = "JM" Then
                            Call cariharga2
                      '  Else
                      '      Call cariharga
                      '  End If
                    End If
                    Call simpan2
                    Call cetak1
                Else
                    MsgBox "No. Mesin tidak terdaftar", vbExclamation, "JAYA MOTOR"
                    Frame1.Visible = False
                End If
            End With
        Else
            Frame1.Visible = False
        End If
    End If
End Sub

Private Sub Text4_Change()
    On Error GoTo tangan
    If Text1.Text <> "" And Text4.Text <> "" Then
        Screen.MousePointer = vbHourglass
    '    Call hapus
        Text5.Text = ""
        Dim msql As String
        Select Case Combo2.ListIndex
            Case 0: Text5.Text = "Nama"
            Case 1: Text5.Text = "Broker"
            Case 2: Text5.Text = "No_Rangka"
            Case 3: Text5.Text = "No_Mesin"
            Case 4: Text5.Text = "Type"
            Case 5: Text5.Text = "Kd_Lising"
            Case 6: Text5.Text = "No_Polisi"
            Case 7: Text5.Text = "No_BPKB"
            Case 8: Text5.Text = "Wilayah"
            Case 9: Text5.Text = "Alamat"
            Case 10: Text5.Text = "Tanggal_PO"
        End Select
        If Text5.Text <> "" Then
            msql = "select * from TInformasi_01 where tanggal >= '" & Format(DTPicker1.Value, "MM-dd-yy") & "' and tanggal <= '" & Format(DTPicker2.Value, "MM-dd-yy") & "' and (" & Text6.Text & ") LIKE '" & Text1.Text & "%" & "' and (" & Text5.Text & ") LIKE '" & Text4.Text & "%" & "' and Post='Ya' and nota LIKE '" & "%" & Label16.Caption & "' order by tanggal"
        End If
     '       Set rs = con.Execute(msql)
     '       With rs
     '           If Not .EOF Then
     '               .MoveFirst
     '               Do Until .EOF
     '                   Label5.Caption = RTrim(!Nota)
     '                   Call simpan
     '                   .MoveNext
     '               Loop
     '           End If
     '       End With
        Adodc1.RecordSource = msql
        Adodc1.Refresh
        Call hit_leasing
        Screen.MousePointer = vbDefault

    End If
    Exit Sub
    
tangan:
    MsgBox "Tentukan dahulu Pencarian berdasarkan object apa", vbExclamation, "Jaya Motor"
    Screen.MousePointer = vbDefault

    Exit Sub
End Sub

