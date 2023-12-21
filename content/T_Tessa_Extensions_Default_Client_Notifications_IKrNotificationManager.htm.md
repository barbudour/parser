# IKrNotificationManager - интерфейс
Объект, управляющий уведомлениями по новым заданиям.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Client.Notifications](N_Tessa_Extensions_Default_Client_Notifications.htm)  
 **Сборка:** Tessa.Extensions.Default.Client (в
Tessa.Extensions.Default.Client.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrNotificationManager
VB __Копировать
     Public Interface IKrNotificationManager
C++ __Копировать
     public interface class IKrNotificationManager
F# __Копировать
     type IKrNotificationManager = interface end
##  __Методы
[CanCheckTasksAsync](M_Tessa_Extensions_Default_Client_Notifications_IKrNotificationManager_CanCheckTasksAsync.htm)|
Возвращает признак того, что уведомления по заданиям включены.  
---|---  
[CheckTasksAsync](M_Tessa_Extensions_Default_Client_Notifications_IKrNotificationManager_CheckTasksAsync.htm)|
Проверяет новые задания и отображает уведомления, если они есть. Метод
вызывается в потоке UI, но фактическое отображение должно быть асинхронное.  
[InitializeAsync](M_Tessa_Extensions_Default_Client_Notifications_IKrNotificationManager_InitializeAsync.htm)|
Подготавливаем инфраструктуру для периодического затягивания информации по
новым заданиям. При этом сам запрос [CheckTasksAsync(Boolean,
CancellationToken)](M_Tessa_Extensions_Default_Client_Notifications_IKrNotificationManager_CheckTasksAsync.htm)
выполнять не требуется.  
[ShutdownAsync](M_Tessa_Extensions_Default_Client_Notifications_IKrNotificationManager_ShutdownAsync.htm)|
Освобождает инфраструктуру для периодического затягивания информации по новым
заданиям.  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Client.Notifications - пространство
имён](N_Tessa_Extensions_Default_Client_Notifications.htm)
