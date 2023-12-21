# BusinessProcessCardHelper.FillNewVersionRow - метод
Метод для заполнения полей строки новой версии процесса
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.Cards](N_Tessa_Extensions_Platform_Server_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void FillNewVersionRow(
    	ISession session,
    	CardRow newRow,
    	int? version = null,
    	bool? isDefault = null,
    	int? parentVersion = null
    )
VB __Копировать
     Public Shared Sub FillNewVersionRow ( 
    	session As ISession,
    	newRow As CardRow,
    	Optional version As Integer? = Nothing,
    	Optional isDefault As Boolean? = Nothing,
    	Optional parentVersion As Integer? = Nothing
    )
C++ __Копировать
     public:
    static void FillNewVersionRow(
    	ISession^ session, 
    	CardRow^ newRow, 
    	Nullable<int> version = nullptr, 
    	Nullable<bool> isDefault = nullptr, 
    	Nullable<int> parentVersion = nullptr
    )
F# __Копировать
     static member FillNewVersionRow : 
            session : ISession * 
            newRow : CardRow * 
            ?version : Nullable<int> * 
            ?isDefault : Nullable<bool> * 
            ?parentVersion : Nullable<int> 
    (* Defaults:
            let _version = defaultArg version null
            let _isDefault = defaultArg isDefault null
            let _parentVersion = defaultArg parentVersion null
    *)
    -> unit 
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Текущая сессия
newRow [CardRow](T_Tessa_Cards_CardRow.htm)
    Новая строка
version
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
(Optional)
    Номер версии
isDefault
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
    Версия должна использоваться по умолчанию
parentVersion
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
(Optional)
    Номер родительской версии, если задан
##  __См. также
#### Ссылки
[BusinessProcessCardHelper -
](T_Tessa_Extensions_Platform_Server_Cards_BusinessProcessCardHelper.htm)
[Tessa.Extensions.Platform.Server.Cards - пространство
имён](N_Tessa_Extensions_Platform_Server_Cards.htm)
