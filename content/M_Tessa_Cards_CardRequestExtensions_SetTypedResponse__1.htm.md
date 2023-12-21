# CardRequestExtensions.SetTypedResponse<TResponse> \- метод
Устанавливает строготипизированный ответ на запрос для универсальных
расширений
[ICardRequestExtension](T_Tessa_Cards_Extensions_ICardRequestExtension.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetTypedResponse<TResponse>(
    	this CardResponse cardResponse,
    	TResponse response
    )
    where TResponse : class, IStorageObjectProvider
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub SetTypedResponse(Of TResponse As {Class, IStorageObjectProvider}) ( 
    	cardResponse As CardResponse,
    	response As TResponse
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename TResponse>
    where TResponse : ref class, IStorageObjectProvider
    static void SetTypedResponse(
    	CardResponse^ cardResponse, 
    	TResponse response
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetTypedResponse : 
            cardResponse : CardResponse * 
            response : 'TResponse -> unit  when 'TResponse : not struct and IStorageObjectProvider
#### Параметры
cardResponse [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Универсальный ответ на запрос к API карточек.
response TResponse
    Строготипизированный ответ на запрос или null, если существующий запрос требуется удалить.
#### Параметры типа
TResponse
     Ссылочный тип строготипизированного ответа на запроса. Должен реализовывать интерфейс [IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm). 
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [CardResponse](T_Tessa_Cards_CardResponse.htm). При вызове метода
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
