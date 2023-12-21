# ICardFileTypePolicy - интерфейс
Политика, определяющая допустимость имени или идентификатора типа файла для
выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileTypePolicy : IExtensionPolicy
VB __Копировать
     Public Interface ICardFileTypePolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class ICardFileTypePolicy : IExtensionPolicy
F# __Копировать
     type ICardFileTypePolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Свойства
[IsAllowAny](P_Tessa_Cards_Extensions_ICardFileTypePolicy_IsAllowAny.htm)|
Признак того, что политика разрешает любые типы файлов, в том числе
неизвестные на момент фильтрации.  
---|---  
##  __Методы
[IsAllowed(CardType)](M_Tessa_Cards_Extensions_ICardFileTypePolicy_IsAllowed_1.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа файла.  
---|---  
[IsAllowed(String)](M_Tessa_Cards_Extensions_ICardFileTypePolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для типа
файла с заданным именем.  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
