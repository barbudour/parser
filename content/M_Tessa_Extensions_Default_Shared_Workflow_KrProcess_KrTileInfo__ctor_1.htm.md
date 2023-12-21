# KrTileInfo(Guid, String, String, String, TileSize, String, Boolean, Boolean,
String, Boolean, String, Int32, IEnumerable<KrTileInfo>) - конструктор
Инициализирует новый экземпляр класса
[KrTileInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTileInfo.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public KrTileInfo(
    	Guid id,
    	string name,
    	string caption,
    	string icon,
    	TileSize tileSize,
    	string tooltip,
    	bool isGlobal,
    	bool askConfirmation,
    	string confirmationMessage,
    	bool actionGrouping,
    	string buttonHotkey,
    	int order,
    	IEnumerable<KrTileInfo> nestedTiles
    )
VB __Копировать
     Public Sub New ( 
    	id As Guid,
    	name As String,
    	caption As String,
    	icon As String,
    	tileSize As TileSize,
    	tooltip As String,
    	isGlobal As Boolean,
    	askConfirmation As Boolean,
    	confirmationMessage As String,
    	actionGrouping As Boolean,
    	buttonHotkey As String,
    	order As Integer,
    	nestedTiles As IEnumerable(Of KrTileInfo)
    )
C++ __Копировать
     public:
    KrTileInfo(
    	Guid id, 
    	String^ name, 
    	String^ caption, 
    	String^ icon, 
    	TileSize tileSize, 
    	String^ tooltip, 
    	bool isGlobal, 
    	bool askConfirmation, 
    	String^ confirmationMessage, 
    	bool actionGrouping, 
    	String^ buttonHotkey, 
    	int order, 
    	IEnumerable<KrTileInfo^>^ nestedTiles
    )
F# __Копировать
     new : 
            id : Guid * 
            name : string * 
            caption : string * 
            icon : string * 
            tileSize : TileSize * 
            tooltip : string * 
            isGlobal : bool * 
            askConfirmation : bool * 
            confirmationMessage : string * 
            actionGrouping : bool * 
            buttonHotkey : string * 
            order : int * 
            nestedTiles : IEnumerable<KrTileInfo> -> KrTileInfo
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
name [String](https://learn.microsoft.com/dotnet/api/system.string)
caption [String](https://learn.microsoft.com/dotnet/api/system.string)
icon [String](https://learn.microsoft.com/dotnet/api/system.string)
tileSize [TileSize](T_Tessa_Platform_TileSize.htm)
tooltip [String](https://learn.microsoft.com/dotnet/api/system.string)
isGlobal [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
askConfirmation
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
confirmationMessage
[String](https://learn.microsoft.com/dotnet/api/system.string)
actionGrouping
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
buttonHotkey [String](https://learn.microsoft.com/dotnet/api/system.string)
order [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
nestedTiles
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KrTileInfo](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTileInfo.htm)>
## __См. также
#### Ссылки
[KrTileInfo -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTileInfo.htm)
[KrTileInfo -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrTileInfo__ctor.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
