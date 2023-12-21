# CardSectionPermissionInfo.SetSectionPermissions - метод
Устанавливает заданные разрешения или запреты для секции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSectionPermissionInfo SetSectionPermissions(
    	CardPermissionFlags flags,
    	bool overwrite = false
    )
VB __Копировать
     Public Function SetSectionPermissions ( 
    	flags As CardPermissionFlags,
    	Optional overwrite As Boolean = false
    ) As CardSectionPermissionInfo
C++ __Копировать
     public:
    CardSectionPermissionInfo^ SetSectionPermissions(
    	CardPermissionFlags flags, 
    	bool overwrite = false
    )
F# __Копировать
     member SetSectionPermissions : 
            flags : CardPermissionFlags * 
            ?overwrite : bool 
    (* Defaults:
            let _overwrite = defaultArg overwrite false
    *)
    -> CardSectionPermissionInfo 
#### Параметры
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
