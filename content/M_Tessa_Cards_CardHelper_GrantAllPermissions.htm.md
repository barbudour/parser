# CardHelper.GrantAllPermissions - метод
Выдаёт все возможные разрешения для заданной карточки и её вложенных карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void GrantAllPermissions(
    	Card card,
    	bool removeOtherPermissions = false,
    	bool excludeCards = false,
    	bool excludeFiles = false,
    	bool excludeTasks = false
    )
VB __Копировать
     Public Shared Sub GrantAllPermissions ( 
    	card As Card,
    	Optional removeOtherPermissions As Boolean = false,
    	Optional excludeCards As Boolean = false,
    	Optional excludeFiles As Boolean = false,
    	Optional excludeTasks As Boolean = false
    )
C++ __Копировать
     public:
    static void GrantAllPermissions(
    	Card^ card, 
    	bool removeOtherPermissions = false, 
    	bool excludeCards = false, 
    	bool excludeFiles = false, 
    	bool excludeTasks = false
    )
F# __Копировать
     static member GrantAllPermissions : 
            card : Card * 
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
    Карточка, для которой требуется выдать все возможные разрешения.
removeOtherPermissions
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
     Признак того, что требуется удалить любые другие разрешения, кроме устанавливаемых. Гарантирует, что в заданном карточке и её вложенных карточках не останется явных запретов. 
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
