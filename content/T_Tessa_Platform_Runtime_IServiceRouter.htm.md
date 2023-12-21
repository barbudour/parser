# IServiceRouter - интерфейс
Объект, выполняющий получение экземпляров сервисов, актуальных для текущего
или заданного маршрута. Используется на клиенте для некоторых сервисов, для
которых требуется обеспечить обратную совместимость.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServiceRouter
VB __Копировать
     Public Interface IServiceRouter
C++ __Копировать
     public interface class IServiceRouter
F# __Копировать
     type IServiceRouter = interface end
##  __Методы
[GetActiveService<T>](M_Tessa_Platform_Runtime_IServiceRouter_GetActiveService__1.htm)|
Возвращает экземпляр сервиса для текущего активного маршрута. Если экземпляр
не удалось получить (т.к. он не зарегистрирован), то выбрасывается исключение
[Tessa.Platform.Runtime.ServiceNotFoundException].  
---|---  
[GetService<T>](M_Tessa_Platform_Runtime_IServiceRouter_GetService__1.htm)|
Возвращает экземпляр сервиса для заданного маршрута route. Если экземпляр не
удалось получить (т.к. он не зарегистрирован), то выбрасывается исключение
[Tessa.Platform.Runtime.ServiceNotFoundException].  
[Invalidate](M_Tessa_Platform_Runtime_IServiceRouter_Invalidate.htm)|  Очищает
кэш со всеми созданными экземплярами маршрутизируемых сервисов, чтобы они
могли быть инициализированы повторно.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
