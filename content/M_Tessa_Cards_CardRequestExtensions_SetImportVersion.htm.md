# CardRequestExtensions.SetImportVersion - метод
Устанавливает оригинальную версию импортируемой карточки, которую требуется
восстановить.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetImportVersion(
    	this CardStoreRequest request,
    	int version
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetImportVersion ( 
    	request As CardStoreRequest,
    	version As Integer
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetImportVersion(
    	CardStoreRequest^ request, 
    	int version
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetImportVersion : 
            request : CardStoreRequest * 
            version : int -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на импорт карточки.
version [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Оригинальная версия импортируемой карточки, которую требуется восстановить.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
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
