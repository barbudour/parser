# CardExtensions.MakeGlobal(CardTypeControl, CardGlobalReferencesContext,
CardSerializableObject[]) - метод
Сделать указанный объект глобальным.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void MakeGlobal(
    	this CardTypeControl obj,
    	CardGlobalReferencesContext context,
    	params CardSerializableObject[] objectsPath
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub MakeGlobal ( 
    	obj As CardTypeControl,
    	context As CardGlobalReferencesContext,
    	ParamArray objectsPath As CardSerializableObject()
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void MakeGlobal(
    	CardTypeControl^ obj, 
    	CardGlobalReferencesContext^ context, 
    	... array<CardSerializableObject^>^ objectsPath
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member MakeGlobal : 
            obj : CardTypeControl * 
            context : CardGlobalReferencesContext * 
            objectsPath : CardSerializableObject[] -> unit 
#### Параметры
obj [CardTypeControl](T_Tessa_Cards_CardTypeControl.htm)
    Объект.
context
[CardGlobalReferencesContext](T_Tessa_Cards_CardGlobalReferencesContext.htm)
    Контекст метаданных.
objectsPath
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)[]
    Перечень объектов, составляющих путь до контрола.
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
[MakeGlobal - перегрузка](Overload_Tessa_Cards_CardExtensions_MakeGlobal.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
