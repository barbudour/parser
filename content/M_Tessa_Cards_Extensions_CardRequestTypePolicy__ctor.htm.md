# CardRequestTypePolicy - конструктор
Создаёт экземпляр класса с указанием списка допустимых типов универсальных
запросов к сервису карточек для выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRequestTypePolicy(
    	params Guid[] requestTypes
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray requestTypes As Guid()
    )
C++ __Копировать
     public:
    CardRequestTypePolicy(
    	... array<Guid>^ requestTypes
    )
F# __Копировать
     new : 
            requestTypes : Guid[] -> CardRequestTypePolicy
#### Параметры
requestTypes [Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
     Список допустимых типов универсальных запросов к сервису карточек для выполнения методов расширения. Значения null недопустимы. 
## __См. также
#### Ссылки
[CardRequestTypePolicy - ](T_Tessa_Cards_Extensions_CardRequestTypePolicy.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
