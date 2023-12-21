# ExtensionExtensions.RegisterDefaults - метод
Регистрирует стратегии и политики по умолчанию для этапов
[Initialize](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Regulate](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Resolve](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Filter](T_Tessa_Extensions_ExtensionStrategyStage.htm),
[Execute](T_Tessa_Extensions_ExtensionStrategyStage.htm) и
[TearDown](T_Tessa_Extensions_ExtensionStrategyStage.htm).
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionContainer RegisterDefaults(
    	this IExtensionContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterDefaults ( 
    	container As IExtensionContainer
    ) As IExtensionContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionContainer^ RegisterDefaults(
    	IExtensionContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterDefaults : 
            container : IExtensionContainer -> IExtensionContainer 
#### Параметры
container [IExtensionContainer](T_Tessa_Extensions_IExtensionContainer.htm)
    Контейнер, в котором проводится регистрация.
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
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
