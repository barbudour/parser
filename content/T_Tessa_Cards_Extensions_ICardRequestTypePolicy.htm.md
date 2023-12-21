# ICardRequestTypePolicy - интерфейс
Политика, определяющая допустимость имени универсального запроса к сервису
карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardRequestTypePolicy : IExtensionPolicy
VB __Копировать
     Public Interface ICardRequestTypePolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class ICardRequestTypePolicy : IExtensionPolicy
F# __Копировать
     type ICardRequestTypePolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Методы
[IsAllowed](M_Tessa_Cards_Extensions_ICardRequestTypePolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
универсального запроса с заданным типом.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
