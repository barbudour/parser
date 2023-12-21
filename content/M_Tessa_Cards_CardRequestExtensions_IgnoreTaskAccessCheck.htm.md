# CardRequestExtensions.IgnoreTaskAccessCheck - метод
Возвращает признак того, что для задания с указанным идентификатором не
выполняется проверка прав.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IgnoreTaskAccessCheck(
    	this ICardStoreExtensionContext context,
    	Guid taskRowID
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IgnoreTaskAccessCheck ( 
    	context As ICardStoreExtensionContext,
    	taskRowID As Guid
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IgnoreTaskAccessCheck(
    	ICardStoreExtensionContext^ context, 
    	Guid taskRowID
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IgnoreTaskAccessCheck : 
            context : ICardStoreExtensionContext * 
            taskRowID : Guid -> bool 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст сохранения карточки, в процессе которого сохраняются/завершаются задания.
taskRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор проверяемого задания.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если для задания с указанным идентификатором не выполняется проверка
прав; false в противном случае.
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
