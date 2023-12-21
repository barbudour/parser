# CardPermissionInfo.SetFilePermissions - метод
Устанавливает заданные разрешения или запреты для файла с идентификатором
fileID.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardPermissionInfo SetFilePermissions(
    	Guid fileID,
    	CardPermissionFlags flags,
    	bool overwrite = false
    )
VB __Копировать
     Public Function SetFilePermissions ( 
    	fileID As Guid,
    	flags As CardPermissionFlags,
    	Optional overwrite As Boolean = false
    ) As CardPermissionInfo
C++ __Копировать
     public:
    CardPermissionInfo^ SetFilePermissions(
    	Guid fileID, 
    	CardPermissionFlags flags, 
    	bool overwrite = false
    )
F# __Копировать
     member SetFilePermissions : 
            fileID : Guid * 
            flags : CardPermissionFlags * 
            ?overwrite : bool 
    (* Defaults:
            let _overwrite = defaultArg overwrite false
    *)
    -> CardPermissionInfo 
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла, для которого устанавливается разрешение или запрет.
flags [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
     Устанавливаемые разрешения или запреты. Для указания разрешения задавайте только флаг Allow, а для запрета - только флаг Prohibit. 
overwrite [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что требуется заменить все имеющиеся разрешения и запреты.
#### Возвращаемое значение
[CardPermissionInfo](T_Tessa_Cards_CardPermissionInfo.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardPermissionInfo - ](T_Tessa_Cards_CardPermissionInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
