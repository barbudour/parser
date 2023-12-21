# CardHelper.SetAllCardPermissions - метод
Устанавливает указанные разрешения для карточки, её файлов и заданий.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetAllCardPermissions(
    	Card card,
    	CardPermissionFlags cardPermissions,
    	CardPermissionFlags filePermissions,
    	bool removeOtherPermissions = false,
    	bool excludeCards = false,
    	bool excludeFiles = false,
    	bool excludeTasks = false
    )
VB __Копировать
     Public Shared Sub SetAllCardPermissions ( 
    	card As Card,
    	cardPermissions As CardPermissionFlags,
    	filePermissions As CardPermissionFlags,
    	Optional removeOtherPermissions As Boolean = false,
    	Optional excludeCards As Boolean = false,
    	Optional excludeFiles As Boolean = false,
    	Optional excludeTasks As Boolean = false
    )
C++ __Копировать
     public:
    static void SetAllCardPermissions(
    	Card^ card, 
    	CardPermissionFlags cardPermissions, 
    	CardPermissionFlags filePermissions, 
    	bool removeOtherPermissions = false, 
    	bool excludeCards = false, 
    	bool excludeFiles = false, 
    	bool excludeTasks = false
    )
F# __Копировать
     static member SetAllCardPermissions : 
            card : Card * 
            cardPermissions : CardPermissionFlags * 
            filePermissions : CardPermissionFlags * 
            ?removeOtherPermissions : bool * 
            ?excludeCards : bool * 
            ?excludeFiles : bool * 
            ?excludeTasks : bool 
    (* Defaults:
            let _removeOtherPermissions = defaultArg removeOtherPermissions false
            let _excludeCards = defaultArg excludeCards false
            let _excludeFiles = defaultArg excludeFiles false
            let _excludeTasks = defaultArg excludeTasks false
    *)
    -> unit 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, для которой требуется явно запретить все возможные разрешения.
cardPermissions [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Разрешения, которые требуется установить для карточек и заданий.
filePermissions [CardPermissionFlags](T_Tessa_Cards_CardPermissionFlags.htm)
    Разрешения, которые требуется установить для файлов.
removeOtherPermissions
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что требуется удалить любые другие разрешения, кроме устанавливаемых. Гарантирует, что в заданном карточке и её вложенных карточках не останется явных разрешений. 
excludeCards [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что следует отключить расчёт прав основной карточки.
excludeFiles [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что следует отключить расчёт прав файлов.
excludeTasks [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что следует отключить расчёт прав заданий.
##  __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
