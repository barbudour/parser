# CardRequestExtensions.SetTypedRequest<TRequest> \- метод
Устанавливает строготипизированный запрос для универсальных расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTypedRequest<TRequest>(
    	this CardRequest cardRequest,
    	TRequest request
    )
    where TRequest : class, IStorageObjectProvider
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTypedRequest(Of TRequest As {Class, IStorageObjectProvider}) ( 
    	cardRequest As CardRequest,
    	request As TRequest
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename TRequest>
    where TRequest : ref class, IStorageObjectProvider
    static void SetTypedRequest(
    	CardRequest^ cardRequest, 
    	TRequest request
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTypedRequest : 
            cardRequest : CardRequest * 
            request : 'TRequest -> unit  when 'TRequest : not struct and IStorageObjectProvider
#### Параметры
cardRequest [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Универсальный запрос к API карточек.
request TRequest
    Строготипизированный запрос или null, если существующий запрос требуется удалить.
#### Параметры типа
TRequest
     Ссылочный тип строготипизированного запроса. Должен реализовывать интерфейс [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm). 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardRequest](T_Tessa_Cards_CardRequest.htm). При вызове метода
для экземпляра следует опускать первый параметр. Дополнительные сведения см. в
разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CardRequestExtensions - ](T_Tessa_Cards_CardRequestExtensions.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
