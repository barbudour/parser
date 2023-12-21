# CardRowPermissionInfo.SetRowPermissions - метод
Устанавливает заданные разрешения или запреты для строки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRowPermissionInfo SetRowPermissions(
    	CardPermissionFlags flags,
    	bool overwrite = false
    )
VB __Копировать
     Public Function SetRowPermissions ( 
    	flags As CardPermissionFlags,
    	Optional overwrite As Boolean = false
    ) As CardRowPermissionInfo
C++ __Копировать
     public:
    CardRowPermissionInfo^ SetRowPermissions(
    	CardPermissionFlags flags, 
    	bool overwrite = false
    )
F# __Копировать
     member SetRowPermissions : 
            flags : CardPermissionFlags * 
            ?overwrite : bool 
    (* Defaults:
            let _overwrite = defaultArg overwrite false
    *)
    -> CardRowPermissionInfo 
#### Параметры
flags [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
     Устанавливаемые разрешения или запреты. Для указания разрешения задавайте только флаг Allow, а для запрета - только флаг Prohibit. 
overwrite [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что требуется заменить все имеющиеся разрешения и запреты.
#### Возвращаемое значение
[CardRowPermissionInfo](T_Tessa_Cards_CardRowPermissionInfo.htm)  
Текущий объект для цепочки вызовов.
##  __См. также
#### Ссылки
[CardRowPermissionInfo - ](T_Tessa_Cards_CardRowPermissionInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
