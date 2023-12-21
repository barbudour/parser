# ILinkManager - интерфейс
Объект, выполняющий регистрацию и обработку ссылок.
## __Definition
 **Пространство имён:** [Tessa.Platform.Links](N_Tessa_Platform_Links.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILinkManager
VB __Копировать
     Public Interface ILinkManager
C++ __Копировать
     public interface class ILinkManager
F# __Копировать
     type ILinkManager = interface end
##  __Свойства
[ExecutableAssembly](P_Tessa_Platform_Links_ILinkManager_ExecutableAssembly.htm)|
Сборка с исполняемым приложением, для которого требуется обработать ссылки.  
---|---  
##  __Методы
[HandleAsync](M_Tessa_Platform_Links_ILinkManager_HandleAsync.htm)| Выполняет
обработку ссылки, информация по которой задана в контексте.  
---|---  
[Register](M_Tessa_Platform_Links_ILinkManager_Register.htm)| Регистрирует
обработчик ссылок для заданного действия.  
##  __Методы расширения
[ProcessLinkAsync](M_Tessa_Platform_Links_LinksExtensions_ProcessLinkAsync.htm)|
Выполняет обработку ссылки linkText с безопасным выводом сообщений об ошибках.
Возвращает признак того, что обработка была успешно выполнена.  
(Определяется [LinksExtensions](T_Tessa_Platform_Links_LinksExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Links - пространство имён](N_Tessa_Platform_Links.htm)
