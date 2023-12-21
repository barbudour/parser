# CardRequestExtensions.SetTaskAccessCheckIsIgnored - метод
Устанавливает признак того, что для задания с указанным идентификатором не
выполняется проверка прав.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTaskAccessCheckIsIgnored(
    	this ICardStoreExtensionContext context,
    	Guid taskRowID,
    	bool isIgnored = true
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTaskAccessCheckIsIgnored ( 
    	context As ICardStoreExtensionContext,
    	taskRowID As Guid,
    	Optional isIgnored As Boolean = true
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTaskAccessCheckIsIgnored(
    	ICardStoreExtensionContext^ context, 
    	Guid taskRowID, 
    	bool isIgnored = true
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTaskAccessCheckIsIgnored : 
            context : ICardStoreExtensionContext * 
            taskRowID : Guid * 
            ?isIgnored : bool 
    (* Defaults:
            let _isIgnored = defaultArg isIgnored true
    *)
    -> unit 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст сохранения карточки, в процессе которого сохраняются/завершаются задания.
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор задания, для которого устанавливается признак.
isIgnored [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что для задания с указанным идентификатором не выполняется проверка прав.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
