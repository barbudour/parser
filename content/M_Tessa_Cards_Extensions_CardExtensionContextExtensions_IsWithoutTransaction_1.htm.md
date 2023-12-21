#
CardExtensionContextExtensions.IsWithoutTransaction(ICardStoreExtensionContext)
- метод
Возвращает признак того, что используется стратегия обеспечения блокировок без
транзакций.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsWithoutTransaction(
    	this ICardStoreExtensionContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IsWithoutTransaction ( 
    	context As ICardStoreExtensionContext
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IsWithoutTransaction(
    	ICardStoreExtensionContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IsWithoutTransaction : 
            context : ICardStoreExtensionContext -> bool 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст расширения на сохранение карточки.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если используется стратегия обеспечения блокировок без транзакций;
false, если используется стратегия обеспечения блокировок с транзакциями,
нестандартная стратегия или стратегия не используется, например, на клиенте.
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
[CardExtensionContextExtensions -
](T_Tessa_Cards_Extensions_CardExtensionContextExtensions.htm)
[IsWithoutTransaction -
перегрузка](Overload_Tessa_Cards_Extensions_CardExtensionContextExtensions_IsWithoutTransaction.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
