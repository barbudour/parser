# GenericExtensions.IfTrue - метод
Выполняет action если conditional равен true
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IfTrue(
    	this bool conditional,
    	[NotNullAttribute] Action action
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function IfTrue ( 
    	conditional As Boolean,
    	<NotNullAttribute> action As Action
    ) As Boolean
C++ __Копировать
     public:
    [ExtensionAttribute]
    static bool IfTrue(
    	bool conditional, 
    	[NotNullAttribute] Action^ action
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member IfTrue : 
            conditional : bool * 
            [<NotNullAttribute>] action : Action -> bool 
#### Параметры
conditional [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Проверяемое условие 
action [Action](https://learn.microsoft.com/dotnet/api/system.action)
     Действие выполняемое если conditional True 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Возвращает значение полученное в качестве параметра conditional
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[GenericExtensions - ](T_Tessa_Applications_GenericExtensions.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
