#define   Name       "LoDB"
#define   Progname   "lodb"
#define   Version    "Beta-0.0.2"
#define   Publisher  "Lostudio"
#define   URL        "https://github.com/lo-proger"
#define   ExeName    "lodb.exe"

[Setup]
AppId={{4D4F4248-1FCA-46F9-A7FA-97C5982213C5}

AppName={#Name}
AppVersion={#Version}
AppPublisher={#Publisher}
AppPublisherURL={#URL}
AppSupportURL={#URL}
AppUpdatesURL={#URL}

DefaultDirName={userpf}\{#Progname}
DefaultGroupName={#Name}

OutputDir=C:\Users\Digma Pro\Documents\github\loDB
OutputBaseFileName=LoDB_Installer

//SetupIconFile=C:\Users\Digma Pro\Documents\github\loDB\icon.ico

Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"; 
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"; 

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Digma Pro\Documents\github\loDB\Beta\0.0.2\bin\lodb.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Digma Pro\Documents\github\loDB\Beta\0.0.2\file\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]

Name: "{group}\{#Name}"; Filename: "{app}\{#ExeName}"

Name: "{commondesktop}\{#Name}"; Filename: "{app}\{#ExeName}"; Tasks: desktopicon
