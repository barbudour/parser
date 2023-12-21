# CardSectionPermissionInfo.SetFieldPermissions - метод
Устанавливает заданные разрешения или запреты для поля секции с именем
fieldName.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSectionPermissionInfo SetFieldPermissions(
    	string fieldName,
    	CardPermissionFlags flags,
    	bool overwrite = false
    )
VB __Копировать
     Public Function SetFieldPermissions ( 
    	fieldName As String,
    	flags As CardPermissionFlags,
    	Optional overwrite As Boolean = false
    ) As CardSectionPermissionInfo
C++ __Копировать
     public:
    CardSectionPermissionInfo^ SetFieldPermissions(
    	String^ fieldName, 
    	CardPermissionFlags flags, 
    	bool overwrite = false
    )
F# __Копировать
     member SetFieldPermissions : 
            fieldName : string * 
            flags : CardPermissionFlags * 
            ?overwrite : bool 
    (* Defaults:
            let _overwrite = defaultArg overwrite false
    *)
    -> CardSectionPermissionInfo 
#### Параметры
fieldName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя поля, для которого устанавливается разрешение или запрет.
flags [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
     Устанавливаемые разрешения или запреты. Для указания разрешения задавайте только флаг Allow, а для запрета - только флаг Prohibit. 
overwrite [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что требуется заменить все имеющиеся разрешения и запреты.
#### Возвращаемое значение
[CardSectionPermissionInfo](T_Tessa_Cards_CardSectionPermissionInfo.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardSectionPermissionInfo - ](T_Tessa_Cards_CardSectionPermissionInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
