# CardRequestExtensions.SetForbidFileStoreChanging - метод
Устанавливает признак того, что для файлов сохраняемой карточки запрещено
изменять местоположение контента при сохранении.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetForbidFileStoreChanging(
    	this CardStoreRequest request,
    	bool value
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetForbidFileStoreChanging ( 
    	request As CardStoreRequest,
    	value As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void SetForbidFileStoreChanging(
    	CardStoreRequest^ request, 
    	bool value
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetForbidFileStoreChanging : 
            request : CardStoreRequest * 
            value : bool -> unit 
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
     Запрос на сохранение карточки, для которого требуется установить признак того, что для файлов сохраняемой карточки запрещено изменять местоположение контента при сохранении. 
value [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак того, что для файлов сохраняемой карточки запрещено изменять местоположение контента при сохранении. 
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
