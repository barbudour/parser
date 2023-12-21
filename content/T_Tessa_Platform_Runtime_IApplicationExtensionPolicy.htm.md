# IApplicationExtensionPolicy - интерфейс
Политика, определяющая допустимость идентификатора типа приложения для
выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationExtensionPolicy : IExtensionPolicy
VB __Копировать
     Public Interface IApplicationExtensionPolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class IApplicationExtensionPolicy : IExtensionPolicy
F# __Копировать
     type IApplicationExtensionPolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Свойства
[IsAllowAny](P_Tessa_Platform_Runtime_IApplicationExtensionPolicy_IsAllowAny.htm)|
Признак того, что политика разрешает любые типы приложений, в том числе
неизвестные на момент фильтрации.  
---|---  
##  __Методы
[IsAllowed](M_Tessa_Platform_Runtime_IApplicationExtensionPolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного типа приложения.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
