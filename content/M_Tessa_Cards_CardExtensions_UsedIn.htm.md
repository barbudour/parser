# CardExtensions.UsedIn - метод
Возвращает признак того, что флаги элемента управления позволяют ему
располагаться в карточках с заданным типом экземпляра.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool UsedIn(
    	this CardControlTypeFlags flags,
    	CardInstanceType instanceType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function UsedIn ( 
    	flags As CardControlTypeFlags,
    	instanceType As CardInstanceType
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool UsedIn(
    	CardControlTypeFlags flags, 
    	CardInstanceType instanceType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member UsedIn : 
            flags : CardControlTypeFlags * 
            instanceType : CardInstanceType -> bool 
#### Параметры
flags [CardControlTypeFlags](T_Tessa_Cards_CardControlTypeFlags.htm)
    Флаги элемента управления.
instanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)
    Тип экземпляра карточки, допустимость которого требуется проверить по флагам.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если флаги элемента управления позволяют ему располагаться в карточках с
заданным типом экземпляра; false в противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardControlTypeFlags](T_Tessa_Cards_CardControlTypeFlags.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardExtensions - ](T_Tessa_Cards_CardExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
