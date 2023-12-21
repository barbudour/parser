# CardRequestExtensions.SetWarningIfEntryNotFoundFlag - метод
Устанавливает флаг, указывающий на то, что в случае отсутствия строковой
секции в БД, будет сгенерировано предупреждение, а не ошибка.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetWarningIfEntryNotFoundFlag(
    	this CardGetRequest request,
    	bool flag
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetWarningIfEntryNotFoundFlag ( 
    	request As CardGetRequest,
    	flag As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetWarningIfEntryNotFoundFlag(
    	CardGetRequest^ request, 
    	bool flag
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetWarningIfEntryNotFoundFlag : 
            request : CardGetRequest * 
            flag : bool -> unit 
#### Параметры
request [CardGetRequest](T_Tessa_Cards_CardGetRequest.htm)
flag [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
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
