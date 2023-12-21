# CardAnyRequestTypePolicy.IsAllowed - метод
Возвращает признак того, что выполнение методов расширения допустимо для
универсального запроса с заданным типом.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool IsAllowed(
    	Guid requestType
    )
VB __Копировать
     Public Function IsAllowed ( 
    	requestType As Guid
    ) As Boolean
C++ __Копировать
     public:
    virtual bool IsAllowed(
    	Guid requestType
    ) sealed
F# __Копировать
     abstract IsAllowed : 
            requestType : Guid -> bool 
    override IsAllowed : 
            requestType : Guid -> bool 
#### Параметры
requestType [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Тип универсального запроса к сервису карточек.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если выполнение методов расширения допустимо для универсального запроса
с заданным типом; false в противном случае.
#### Реализации
[ICardRequestTypePolicy.IsAllowed(Guid)](M_Tessa_Cards_Extensions_ICardRequestTypePolicy_IsAllowed.htm)  
##  __См. также
#### Ссылки
[CardAnyRequestTypePolicy -
](T_Tessa_Cards_Extensions_CardAnyRequestTypePolicy.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
