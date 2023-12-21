# CardExtensions.ToCardTableType - метод
Преобразует перечисление значение перечисления
[SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm) к типу
[CardTableType](T_Tessa_Cards_CardTableType.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardTableType ToCardTableType(
    	this SchemeTableContentType contentType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ToCardTableType ( 
    	contentType As SchemeTableContentType
    ) As CardTableType
C++ __Копировать
     public:
    [ExtensionAttribute]
    static CardTableType ToCardTableType(
    	SchemeTableContentType contentType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ToCardTableType : 
            contentType : SchemeTableContentType -> CardTableType 
#### Параметры
contentType
[SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm)
    Значение перечисления, которое требуется преобразовать.
#### Возвращаемое значение
[CardTableType](T_Tessa_Cards_CardTableType.htm)  
Преобразованное значение перечисления.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[SchemeTableContentType](T_Tessa_Scheme_SchemeTableContentType.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
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
