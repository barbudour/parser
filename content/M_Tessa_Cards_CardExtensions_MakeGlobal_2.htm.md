# CardExtensions.MakeGlobal(IEnumerable<CardTypeControl>,
CardGlobalReferencesContext, CardSerializableObject[]) - метод
Сделать контролы типа карточки глобальными.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void MakeGlobal(
    	this IEnumerable<CardTypeControl> controls,
    	CardGlobalReferencesContext context,
    	params CardSerializableObject[] objectsPath
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub MakeGlobal ( 
    	controls As IEnumerable(Of CardTypeControl),
    	context As CardGlobalReferencesContext,
    	ParamArray objectsPath As CardSerializableObject()
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void MakeGlobal(
    	IEnumerable<CardTypeControl^>^ controls, 
    	CardGlobalReferencesContext^ context, 
    	... array<CardSerializableObject^>^ objectsPath
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member MakeGlobal : 
            controls : IEnumerable<CardTypeControl> * 
            context : CardGlobalReferencesContext * 
            objectsPath : CardSerializableObject[] -> unit 
#### Параметры
controls
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)>
    Контролы.
context
[CardGlobalReferencesContext](T_Tessa_Cards_CardGlobalReferencesContext.htm)
    Контекст метаданных.
objectsPath
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)[]
    Перечень объектов, составляющих путь до блока.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)>.
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
