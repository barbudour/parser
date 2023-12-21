# IServiceRouteSettings - интерфейс
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServiceRouteSettings
VB __Копировать
     Public Interface IServiceRouteSettings
C++ __Копировать
     public interface class IServiceRouteSettings
F# __Копировать
     type IServiceRouteSettings = interface end
##  __Свойства
[ActiveRoute](P_Tessa_Platform_Runtime_IServiceRouteSettings_ActiveRoute.htm)|
Текущий активный маршрут, по которому клиент подключается к веб-сервисам. По
умолчанию равен [ServiceRoute.Default].  
---|---  
[Info](P_Tessa_Platform_Runtime_IServiceRouteSettings_Info.htm)|
Дополнительная информация для маршрутизации, которая может использоваться в
реализациях интерфейсов сервисов.  
## __Методы
[GetSupportedRoutes](M_Tessa_Platform_Runtime_IServiceRouteSettings_GetSupportedRoutes.htm)|
Возвращает коллекцию маршрутов, которые поддерживаются текущей конфигурацией
сервера.  
---|---  
[IsRouteSupported](M_Tessa_Platform_Runtime_IServiceRouteSettings_IsRouteSupported.htm)|
Возвращает признак того, что заданный маршрут поддерживается текущей
конфигурацией сервера.  
[SetRouteSupported](M_Tessa_Platform_Runtime_IServiceRouteSettings_SetRouteSupported.htm)|
Устанавливает признак того, что заданный маршрут поддерживается текущей
конфигурацией сервера.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
