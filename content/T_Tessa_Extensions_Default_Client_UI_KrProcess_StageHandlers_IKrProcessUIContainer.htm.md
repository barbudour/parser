# IKrProcessUIContainer - интерфейс
Объект, содержащий информацию о UI обработчиках этапов подсистемы маршрутов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrProcessUIContainer
VB __Копировать
     Public Interface IKrProcessUIContainer
C++ __Копировать
     public interface class IKrProcessUIContainer
F# __Копировать
     type IKrProcessUIContainer = interface end
##  __Методы
[RegisterUIHandler(Type)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrProcessUIContainer_RegisterUIHandler.htm)|
Регистрирует UI обработчик этапа для любого типа этапа.  
---|---  
[RegisterUIHandler(StageTypeDescriptor,
Type)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrProcessUIContainer_RegisterUIHandler_1.htm)|
Регистрирует UI обработчик этапа для типа этапа с заданным дескриптором.  
[RegisterUIHandler<T>()](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrProcessUIContainer_RegisterUIHandler__1.htm)|
Регистрирует UI обработчик этапа для любого типа этапа.  
[RegisterUIHandler<T>(StageTypeDescriptor)](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrProcessUIContainer_RegisterUIHandler__1_1.htm)|
Регистрирует UI обработчик этапа для типа этапа с заданным дескриптором.  
[ResolveUIHandlers](M_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers_IKrProcessUIContainer_ResolveUIHandlers.htm)|
Возвращает список зарегистрированных UI обработчиков для типа этапа с
указанным идентификатором и обработчиков, выполняющихся для любого типа этапа.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.UI.KrProcess.StageHandlers - пространство
имён](N_Tessa_Extensions_Default_Client_UI_KrProcess_StageHandlers.htm)
