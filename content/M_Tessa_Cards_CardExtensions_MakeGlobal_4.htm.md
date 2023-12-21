# CardExtensions.MakeGlobal(IEnumerable<CardTypeNamedForm>,
CardGlobalReferencesContext) - метод
Сделать формы типа карточки глобальными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void MakeGlobal(
    	this IEnumerable<CardTypeNamedForm> forms,
    	CardGlobalReferencesContext context
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub MakeGlobal ( 
    	forms As IEnumerable(Of CardTypeNamedForm),
    	context As CardGlobalReferencesContext
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void MakeGlobal(
    	IEnumerable<CardTypeNamedForm^>^ forms, 
    	CardGlobalReferencesContext^ context
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member MakeGlobal : 
            forms : IEnumerable<CardTypeNamedForm> * 
            context : CardGlobalReferencesContext -> unit 
#### Параметры
forms
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeNamedForm](T_Tessa_Cards_CardTypeNamedForm.htm)>
    Формы.
context
[CardGlobalReferencesContext](T_Tessa_Cards_CardGlobalReferencesContext.htm)
    Контекст метаданных.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeNamedForm](T_Tessa_Cards_CardTypeNamedForm.htm)>.
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
[MakeGlobal - перегрузка](Overload_Tessa_Cards_CardExtensions_MakeGlobal.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
