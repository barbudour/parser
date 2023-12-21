# IPlugin - интерфейс
Интерфейс плагина.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPlugin
VB __Копировать
     Public Interface IPlugin
C++ __Копировать
     public interface class IPlugin
F# __Копировать
     type IPlugin = interface end
##  __Заметки
Вежливая остановка может происходить при остановке хоста, запущенного как
сервис Windows, или при вводе команды остановки в хосте, запущенном в консоли
(при закрытии окна консоли или при завершении процесса хоста через диспетчер
вежливой остановки не производится). При этом все запущенные плагины имеют
некоторое время, определяемое настройками хоста (порядка 30 секунд), для того,
чтобы корректно завершить свою работу. Если метод
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm)
не успел выполнить все действия за заданное время, то процесс плагина будет
принудительно остановлен.
## __Методы
[EntryPointAsync](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)|
Асинхронный метод, вызываемый хостом при запуске плагина.  
---|---  
## __Методы расширения
[LoadConfig](M_Chronos_Contracts_PluginExtensions_LoadConfig.htm)|  Загружает
первый используемый конфигурационный файл для заданного плагина, и возвращает
загруженный XML-документ.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
---|---  
[LoadConfig](M_Chronos_Contracts_PluginExtensions_LoadConfig_1.htm)|
Загружает конфигурационный файл для заданного плагина и указанного пути к
файлу относительно папки, в которой расположена сборка с плагином, и
возвращает загруженный XML-документ.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
[TryLoadConfig](M_Chronos_Contracts_PluginExtensions_TryLoadConfig.htm)|
Загружает первый используемый конфигурационный файл для заданного плагина, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
[TryLoadConfig](M_Chronos_Contracts_PluginExtensions_TryLoadConfig_1.htm)|
Загружает конфигурационный файл для заданного плагина и указанного пути к
файлу относительно папки, в которой расположена сборка с плагином, и
возвращает загруженный XML-документ или null, если файл отсутствовал по
заданному пути.  
(Определяется [PluginExtensions](T_Chronos_Contracts_PluginExtensions.htm))  
##  __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
