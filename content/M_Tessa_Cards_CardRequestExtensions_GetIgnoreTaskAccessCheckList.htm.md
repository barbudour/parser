# CardRequestExtensions.GetIgnoreTaskAccessCheckList - метод
Возвращает массив, содержащий список идентификаторов заданий, для которых не
выполняется проверка на права. Массив всегда не равен null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Guid[] GetIgnoreTaskAccessCheckList(
    	this ICardStoreExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetIgnoreTaskAccessCheckList ( 
    	context As ICardStoreExtensionContext
    ) As Guid()
C++ __Копировать
     public:
    [ExtensionAttribute]
    static array<Guid>^ GetIgnoreTaskAccessCheckList(
    	ICardStoreExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetIgnoreTaskAccessCheckList : 
            context : ICardStoreExtensionContext -> Guid[] 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст сохранения карточки, в процессе которого сохраняются/завершаются задания.
#### Возвращаемое значение
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]  
Массив, содержащий список идентификаторов заданий, для которых не выполняется
проверка на права. Массив всегда не равен null.
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
