# CardExtensions.AppliesRequiredToControl - метод
Возвращает признак того, что валидатор устанавливает признак "Обязательно для
заполнения" для заданного элемента управления control.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool AppliesRequiredToControl(
    	this CardTypeValidator validator,
    	CardTypeControl control
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AppliesRequiredToControl ( 
    	validator As CardTypeValidator,
    	control As CardTypeControl
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool AppliesRequiredToControl(
    	CardTypeValidator^ validator, 
    	CardTypeControl^ control
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AppliesRequiredToControl : 
            validator : CardTypeValidator * 
            control : CardTypeControl -> bool 
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Валидатор, для которого выполняется проверка.
control [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
    Элемент управления, для которого выполняется проверка.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если валидатор устанавливает признак "Обязательно для заполнения" для
заданного элемента управления control; false в противном случае.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm). При
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
