# IServerInitializer - интерфейс
Объект, возвращающий данные для инициализации клиента. Такие данные обычно
собираются на сервере.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServerInitializer
VB __Копировать
     Public Interface IServerInitializer
C++ __Копировать
     public interface class IServerInitializer
F# __Копировать
     type IServerInitializer = interface end
##  __Методы
[GetInitializationResponseAsync](M_Tessa_Platform_Initialization_IServerInitializer_GetInitializationResponseAsync.htm)|
Возвращает ответ на запрос по инициализации клиента. При этом не формируется
поток инициализации, все возвращаемые данные содержатся в запросе.  
---|---  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
