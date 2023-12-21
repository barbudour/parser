# ICardTypePolicy - интерфейс
Политика, определяющая допустимость имени или идентификатора типа карточки для
выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTypePolicy : IExtensionPolicy
VB __Копировать
     Public Interface ICardTypePolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class ICardTypePolicy : IExtensionPolicy
F# __Копировать
     type ICardTypePolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Свойства
[IsAllowAny](P_Tessa_Cards_Extensions_ICardTypePolicy_IsAllowAny.htm)| Признак
того, что политика разрешает любые типы карточек, в том числе неизвестные на
момент фильтрации.  
---|---  
##  __Методы
[IsAllowed(CardType)](M_Tessa_Cards_Extensions_ICardTypePolicy_IsAllowed_1.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа карточки.  
---|---  
[IsAllowed(String)](M_Tessa_Cards_Extensions_ICardTypePolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для типа
карточки с заданным именем.  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
