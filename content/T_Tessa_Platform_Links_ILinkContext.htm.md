# ILinkContext - интерфейс
Контекст обработчика по открытию ссылок.
## __Definition
 **Пространство имён:** [Tessa.Platform.Links](N_Tessa_Platform_Links.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILinkContext
VB __Копировать
     Public Interface ILinkContext
C++ __Копировать
     public interface class ILinkContext
F# __Копировать
     type ILinkContext = interface end
##  __Свойства
[Action](P_Tessa_Platform_Links_ILinkContext_Action.htm)| Действие, указанное
в ссылке. Действие определяет, какой обработчик ссылки будет вызван.  
---|---  
[CancellationToken](P_Tessa_Platform_Links_ILinkContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[Container](P_Tessa_Platform_Links_ILinkContext_Container.htm)|  Контейнер
Unity, из которого обработчик ссылки может получить сервисы и другие
зависимости.  
[Handled](P_Tessa_Platform_Links_ILinkContext_Handled.htm)|  Признак того, что
ссылка была обработана обработчиком. Если значение установлено равным true, то
окно приложения будет активировано при завершении обработки ссылки.  
[Parameters](P_Tessa_Platform_Links_ILinkContext_Parameters.htm)|  Хеш-таблица
с параметрами ссылки, ключом которой является название параметра, а значением
- строковая интерпретация значения параметра, заданная в ссылке.  
[Session](P_Tessa_Platform_Links_ILinkContext_Session.htm)| Текущая сессия.  
##  __Методы
[ActivateShellAsync](M_Tessa_Platform_Links_ILinkContext_ActivateShellAsync.htm)|
Активирует основное окно приложения. Если окно было свёрнуто, то оно
разворачивается.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Links - пространство имён](N_Tessa_Platform_Links.htm)
