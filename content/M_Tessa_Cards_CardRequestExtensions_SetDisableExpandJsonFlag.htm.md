# CardRequestExtensions.SetDisableExpandJsonFlag - метод
Устанавливает флаг, указывающий на то, что при экспорте карточки не нужно
разворачивать JSON-поля карточки из строки в Dictionary<string, object>.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetDisableExpandJsonFlag(
    	this CardGetRequest request,
    	bool flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetDisableExpandJsonFlag ( 
    	request As CardGetRequest,
    	flag As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetDisableExpandJsonFlag(
    	CardGetRequest^ request, 
    	bool flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetDisableExpandJsonFlag : 
            request : CardGetRequest * 
            flag : bool -> unit 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
    Запрос на загрузку карточки.
flag [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Устанавливаемое значение флага.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm). При вызове
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
