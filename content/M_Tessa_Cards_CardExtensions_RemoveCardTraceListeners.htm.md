# CardExtensions.RemoveCardTraceListeners - метод
Удаляет объекты, зарегистрированные методом
[RegisterCardTraceListeners(IExtensionContainer, ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Cards_CardExtensions_RegisterCardTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionContainer RemoveCardTraceListeners(
    	this IExtensionContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RemoveCardTraceListeners ( 
    	container As IExtensionContainer
    ) As IExtensionContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionContainer^ RemoveCardTraceListeners(
    	IExtensionContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RemoveCardTraceListeners : 
            container : IExtensionContainer -> IExtensionContainer 
#### Параметры
container [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер, из которого удаляются зарегистрированные объекты.
#### Возвращаемое значение
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)  
Заданный контейнер container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
