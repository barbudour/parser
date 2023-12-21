# KrPermissionsCheckMode - перечисление
Список режимов проверки прав доступа. Определяет методы проверки прав доступа
в
[IKrPermissionsManager](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum KrPermissionsCheckMode
VB __Копировать
     Public Enumeration KrPermissionsCheckMode
C++ __Копировать
     public enum class KrPermissionsCheckMode
F# __Копировать
     type KrPermissionsCheckMode
##  __Члены
WithoutCard| 0|  При данном событии объект карточки еще не существует, поэтому
не выполняется проверка таблицы условий (т.к. она выполняется в контексте
карточки) и контекстных ролей. Применяется при создании карточки.  
---|---|---  
WithCardID| 1|  При данном событии карточка не передается и загружается из
базы. Применяется при чтении файла, версии файла, удалении карточки.  
WithStoreCard| 2|  При данном событии карточка передаётся с неполными данными
и подразумевается, что актуальные данные карточки находятся в базе.
Применяется при сохранении карточки.  
WithCard| 3|  При данном событии все данные о карточки уже загружены и
актуальны. Применяется при чтении карточки.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
