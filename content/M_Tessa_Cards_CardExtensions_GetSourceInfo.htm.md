# CardExtensions.GetSourceInfo - метод
Метод для поулчения информации об источнике данных контрола с учетом возможной
регистрации кастомного метода для получения источника данных в
[ICardControlTypeRegistry](T_Tessa_Cards_ICardControlTypeRegistry.htm)
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardControlSourceInfo GetSourceInfo(
    	this CardTypeControl control
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function GetSourceInfo ( 
    	control As CardTypeControl
    ) As CardControlSourceInfo
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardControlSourceInfo^ GetSourceInfo(
    	CardTypeControl^ control
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member GetSourceInfo : 
            control : CardTypeControl -> CardControlSourceInfo 
#### Параметры
control [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
    Метаинформация с настройками контрола
#### Возвращаемое значение
[CardControlSourceInfo](T_Tessa_Cards_CardControlSourceInfo.htm)  
Возвращает информцию об источнике данных контрола
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm). При вызове
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
