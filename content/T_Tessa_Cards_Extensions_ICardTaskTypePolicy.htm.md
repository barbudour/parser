# ICardTaskTypePolicy - интерфейс
Политика, определяющая допустимость имени или идентификатора типа задания для
выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTaskTypePolicy : IExtensionPolicy
VB __Копировать
     Public Interface ICardTaskTypePolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class ICardTaskTypePolicy : IExtensionPolicy
F# __Копировать
     type ICardTaskTypePolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Свойства
[IsAllowAny](P_Tessa_Cards_Extensions_ICardTaskTypePolicy_IsAllowAny.htm)|
Признак того, что политика разрешает любые типы заданий, в том числе
неизвестные на момент фильтрации.  
---|---  
##  __Методы
[IsAllowed(CardType)](M_Tessa_Cards_Extensions_ICardTaskTypePolicy_IsAllowed_1.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа задания.  
---|---  
[IsAllowed(String)](M_Tessa_Cards_Extensions_ICardTaskTypePolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для типа
задания с заданным именем.  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
