# CardComponentHelper.GetInvalidInstanceTypeResponse<TResponse> \- метод
Возвращает запрос с сообщением об ошибке валидации, обозначающей
несоответствие типа экземпляра для заданного типа карточки cardType и
ожидаемого типа экземпляра expectedInstanceType.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static TResponse GetInvalidInstanceTypeResponse<TResponse>(
    	Object validationObject,
    	CardType cardType,
    	CardInstanceType expectedInstanceType
    )
    where TResponse : new(), CardResponseBase
VB __Копировать
     Public Shared Function GetInvalidInstanceTypeResponse(Of TResponse As {New, CardResponseBase}) ( 
    	validationObject As Object,
    	cardType As CardType,
    	expectedInstanceType As CardInstanceType
    ) As TResponse
C++ __Копировать
     public:
    generic<typename TResponse>
    where TResponse : gcnew(), CardResponseBase
    static TResponse GetInvalidInstanceTypeResponse(
    	Object^ validationObject, 
    	CardType^ cardType, 
    	CardInstanceType expectedInstanceType
    )
F# __Копировать
     static member GetInvalidInstanceTypeResponse : 
            validationObject : Object * 
            cardType : CardType * 
            expectedInstanceType : CardInstanceType -> 'TResponse  when 'TResponse : new() and CardResponseBase
#### Параметры
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object)
    Объект, от имени которого выполняется валидация.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, тип экземпляра которого задан неверно.
expectedInstanceType [CardInstanceType](T_Tessa_Cards_CardInstanceType.htm)
    Ожидаемый тип экземпляра.
#### Параметры типа
TResponse
     Тип запроса к сервису карточек, наследуемый от [CardResponseBase](T_Tessa_Cards_CardResponseBase.htm) и содержащий конструктор по умолчанию. 
#### Возвращаемое значение
TResponse  
Ответ на запрос к сервису карточек, содержащий сообщение об ошибке.
##  __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
