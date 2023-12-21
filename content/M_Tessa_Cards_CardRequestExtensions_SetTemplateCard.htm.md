# CardRequestExtensions.SetTemplateCard(Dictionary<String, Object>, Card) -
метод
Устанавливает карточку шаблона в запросе на создание структуры карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTemplateCard(
    	this Dictionary<string, Object> info,
    	Card card
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTemplateCard ( 
    	info As Dictionary(Of String, Object),
    	card As Card
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetTemplateCard(
    	Dictionary<String^, Object^>^ info, 
    	Card^ card
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTemplateCard : 
            info : Dictionary<string, Object> * 
            card : Card -> unit 
#### Параметры
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Информация, передаваемая в запрос на сохранение карточки.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка шаблона, которую требуется установить в запросе на создание структуры карточки.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[SetTemplateCard -
перегрузка](Overload_Tessa_Cards_CardRequestExtensions_SetTemplateCard.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
